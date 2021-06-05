[![Build Status](https://github.com/jszopi/restrained-ESP-fit/actions/workflows/main.yml/badge.svg)](https://github.com/jszopi/restrained-ESP-fit/actions?query=branch%3Amaster)
<!-- TODO: Add PyPI badge -->

# restrained-ESP-fit

This is a fork of the `resp` program commonly used in computational chemistry for fitting partial atomic charges to values of the provided molecular Electrostatic Potential (ESP) field around a molecule.
The method was first described by Bayly et al.¹ using the MK mesh of sampling the ESP field² but the program can generally fit charges to any mesh of points.
The mesh needs to be produced independently; see the [jszopi/repESP](https://github.com/jszopi/repESP) repo for some helpers, including extracting ESP fitting points from the output of the Gaussian program and wrapping the calls to the `resp` program in a Python library.
The program can also be used to fit partial charges to the ESP without any restraints.

History prior to version 2.2 was not preserved (or rather, reconstructed, considering lack of a version controlled repo).
This version was downloaded in May 2020 from https://upjv.q4md-forcefieldtools.org/RED/ together with other programs in q4md-fft tools 2.0.
The original README for this version can be found in the [`README-2.4.txt` file](https://github.com/jszopi/resp/blob/master/README-2.4.txt) — see for build instructions.
Usage instructions are only available for version 2.2 and are hosted at https://upjv.q4md-forcefieldtools.org/RED/resp/ (if link is down, get your browser to display [the repo version](https://github.com/jszopi/resp/blob/566c9207b87ed37c6a8b2e47a581704db762f16c/resp-2.2.html)).
Use the `restrained_ESP_fit` script to invoke the program, as the name `resp` is now deprecated. 

I am hoping to rewrite this program in Python in order to encourage users to experiment with their own fitting methods.
The code will thus soon be available in PyPI, possibly under a less generic name.
Please open a PR if you'd like it to be available in your system's package manager.

# Usage

## Install

### Install from source

<!-- TODO: This section only pertains to environment variables, add more complete instructions. -->
The original `resp` program can be compiled with different Fortran compilers and flags.
These options are currently not exposed from the Python installer; please open an issue if you would benefit from being able to control these options.

A few options are exposed when the `resp` program is to be linked statically, primarily for the purpose of CD of binary wheels.
If the `RESP_STATIC` variable is set to "1" during installation, the `resp` binary will be compiled while statically linking the libgfortran and libquadmath libraries.
You are required to provide the path to where these static libraries can be found by setting the `RESP_VPATH` variable.
<!-- TODO: This can be done by setting PATH or aliasing, the only reason I exposed it as an environment variable was because I could get it to work in Travis. -->
`gcc` will be used as the compiler and if the one in you `$PATH` isn't suitable, you can override it by setting `RESP_COMPILER`.
<!-- TODO: How was this allowed in macOS if it doesn't follow the gcc interface? -->
This will be necessary on macOS, where `gcc` after major version 4 actually invoke clang, which isn't compatible with the flags used in the build.

--- 

¹ C. I. Bayly, P. Cieplak, W. D. Cornell and P. A. Kollman, *J. Phys. Chem.*, 1993, **97**, 10269–10280

² U. C. Singh and P. A. Kollman, *J. Comput. Chem.*, 1984, **5**, 129–145
