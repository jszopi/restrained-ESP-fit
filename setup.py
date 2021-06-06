from setuptools import setup
import distutils.command.build
from distutils.dir_util import copy_tree
import os
import shutil
import subprocess
import tempfile

with open("README.md", "r") as fh:
    long_description = fh.read()


class build_(distutils.command.build.build):

    def run(self):
        print("Running build")

        with tempfile.TemporaryDirectory() as tmpdir:
            copy_tree("resp", tmpdir)
            shutil.rmtree(f"{tmpdir}/build", ignore_errors=True)
            if os.environ.get("RESP_STATIC") == "1":
                if os.environ.get("RESP_VPATH") is None:
                    raise RuntimeError("Requested static linking of `resp` but the environment variable RESP_VPATH is not set.")
                shutil.copy("Makefile-resp-static", f"{tmpdir}/Makefile")
            subprocess.run(["make"], cwd=tmpdir).check_returncode()
            copy_tree(tmpdir, "restrained_ESP_fit/build")

        distutils.command.build.build.run(self)


config = {
    'name': 'restrained-ESP-fit',
    'description': 'Fitting partial charges to molecular Electrostatic Potential field',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'maintainer': 'Jan Szopinski',
    'maintainer_email': 'jszopi@users.noreply.github.com',
    'url': 'https://github.com/jszopi/restrained-ESP-fit',
    'license': 'GPLv3',
    'packages': ["restrained_ESP_fit"],
    'package_data': {"restrained_ESP_fit": ["build/resp"]},
    # Hacky? Causes the `resp` binary to be included in bdist_wheel but not in sdist
    'include_package_data': True,
    'entry_points': {
        'console_scripts': ["restrained-ESP-fit=restrained_ESP_fit.resp_wrapper:main"],
    },
    'cmdclass': {'build': build_},
    # Removing the local version as PyPI doesn't allow it
    'use_scm_version': {"local_scheme": "no-local-version"},
    'setup_requires': ["setuptools_scm"],
    'python_requires': ">=3",
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    'keywords': ["restrained molecular electrostatic potential ESP fitting RESP atomic partial charges"]
}

setup(**config)
