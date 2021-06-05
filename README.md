[![Build Status](https://github.com/jszopi/restrained-ESP-fit/actions/workflows/main.yml/badge.svg)](https://github.com/jszopi/restrained-ESP-fit/actions?query=branch%3Amaster)
<!-- TODO: Add PyPI badge -->

# restrained-ESP-fit

This is a fork of the `resp` program commonly used in computational chemistry for fitting partial atomic charges to values of the provided molecular Electrostatic Potential (ESP) field around a molecule.
The method was first described by Bayly et al.¹ using the MK mesh of sampling the ESP field² but the program can generally fit charges to any mesh of points.
The mesh needs to be produced independently; see the [jszopi/repESP](https://github.com/jszopi/repESP) repo for some helpers, including extracting ESP fitting points from the output of the Gaussian program and wrapping the calls to the `resp` program in a Python library.
The program can also be used to fit partial charges to the ESP without any restraints.

# Versioning

The purpose of this fork is twofold: easier distribution of the original `resp` program as well as evolution independent from it.

## Relation to `resp`

Multiple versions of `resp` have appeared over the years and this project aims to make available the code for the newer versions.
Versions `2.y.z` of this project will wrap the corresponding `resp 2.y` code without even a trivial modification.
The patch version (the `z`) will be incremented upon changes to the wrapping code and CI/CD pipeline.
If the `resp` program ever comes to use a patch version, the changes will be included in the next patch version of this project.
While this will cause the version number to no longer have verbatim correspondence, this state should be acceptable, as users the upstream project should never introduce significant changes in a patch release and clients shouldn't have to pin a patch version.

Code history prior to v2.2 was not preserved (or rather, reconstructed, considering lack of a version controlled repo).

## Independent evolution

In order to allow for independent evolution of the program, the name of the project, `restrained-ESP-fit` is different from `resp`.
The version numbering of the project will reflect the separation from the `resp` version numbers, most likely by using a new major version, i.e. starting from `3.0.0`.
These versions of the project may alter the calculation logic (the results should be identical, barring potential bug fixes) and the interface to the program.
I am hoping to rewrite this program in Python in order to encourage users to experiment with their own fitting methods and constraints.

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
