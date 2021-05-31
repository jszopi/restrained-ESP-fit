#!/usr/bin/env python3

import argparse
import subprocess
import sys


def get_lib_name_from_line(line):
    lib_maybe_as_path = line[: line.find(" ")]
    lib_with_version = lib_maybe_as_path[lib_maybe_as_path.rfind("/") + 1 :]
    lib = lib_with_version[: lib_with_version.find(".")]
    return lib


def get_lib_names_from_lines(lines):
    return [get_lib_name_from_line(line) for line in lines]


def parse_ldd_output(stdout):
    lines = [line.strip() for line in stdout.split("\n")][:-1]
    lines = [line for line in lines if "=>" in line]
    return get_lib_names_from_lines(lines)


def validate_otool_output(lines):
    if lines[0][0].isspace():
        raise ValueError("First line starts with whitespace")
    for line in lines[1:]:
        if line[0] != "\t":
            raise ValueError("Subsequent line is not indented")


def parse_otool_output(stdout):
    lines = stdout.split("\n")[:-1]

    try:
        validate_otool_output(lines)
    except ValueError as e:
        print(
            f"ERROR: otool output validation failed: {e}:\n\t{stdout!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    lines = [line.strip() for line in lines][1:]
    return get_lib_names_from_lines(lines)


LINK_DEPS_UTIL_DEPENDENT_OPTIONS = {
    "ldd": {
        "invocation": ["ldd"],
        "parser": parse_ldd_output,
        "supported_versions": [
            "ldd (Ubuntu GLIBC 2.27-3ubuntu1.4) 2.27",
        ],
    },
    "otool": {
        "invocation": ["otool", "-L"],
        "parser": parse_otool_output,
        "supported_versions": ["llvm-otool(1): Apple Inc. version cctools-977.1"],
    },
}


def parse_args():

    parser = argparse.ArgumentParser(
        description="Check if only expected libraries are linked dynamically"
    )

    parser.add_argument(
        "link_deps_util",
        choices=LINK_DEPS_UTIL_DEPENDENT_OPTIONS.keys(),
        help="The invocation of the object file inspection tool",
    )

    parser.add_argument("object_file", help="The object file to be inspected")

    parser.add_argument(
        "expected_list",
        nargs="+",
        help="The list of expected dynamically-linked libraries",
    )

    return parser.parse_args()


def ensure_supported_link_deps_util(link_deps_util):

    try:
        result = subprocess.run(
            [link_deps_util, "--version"], capture_output=True, check=True, text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.stderr}", file=sys.stderr)
        sys.exit(e.returncode)

    output = result.stdout if link_deps_util != "otool" else result.stderr
    first_line = output.split("\n")[0]

    if (
        first_line
        not in LINK_DEPS_UTIL_DEPENDENT_OPTIONS[link_deps_util]["supported_versions"]
    ):
        print(
            f"ERROR: Validation hasn't been tested against the output of:\n\t{first_line!r}",
            file=sys.stderr,
        )
        sys.exit(1)


def get_dynamic_libraries(link_deps_util, object_file):

    ensure_supported_link_deps_util(link_deps_util)

    invocation = LINK_DEPS_UTIL_DEPENDENT_OPTIONS[link_deps_util]["invocation"]
    command = [*invocation, object_file]
    try:
        result = subprocess.run(command, capture_output=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.stderr}", file=sys.stderr)
        sys.exit(e.returncode)

    print(f"{link_deps_util} output:\n{result.stdout}")
    parser = LINK_DEPS_UTIL_DEPENDENT_OPTIONS[link_deps_util]["parser"]
    return parser(result.stdout)


def compare_lib_lists(actual, expected):
    actual = sorted(list(set(actual)))
    expected = sorted(list(set(expected)))

    if actual == expected:
        print(f"Dynamically-linked libraries are as expected")
        return True
    else:
        print(
            f"Actual libraries differ from expected:\n\t{sorted(actual)}\nvs.\n\t{sorted(expected)}",
            file=sys.stderr,
        )
        return False


if __name__ == "__main__":

    args = parse_args()

    dynamic_libs = get_dynamic_libraries(args.link_deps_util, args.object_file)

    success = compare_lib_lists(dynamic_libs, args.expected_list)

    sys.exit(0 if success else 1)
