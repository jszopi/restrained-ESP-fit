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

### Original `resp` code

Code history prior to `v2.2` was not preserved (or rather, reconstructed, considering lack of a version controlled repo).
The original code for `v2.2` and `v2.4` can be found verbatim in the first two git commits of this repo.
They can be accessed through the corresponding git tags, namely [here for `v2.2`](https://github.com/jszopi/restrained-ESP-fit/tree/v2.2) and [here for `v2.4`](https://github.com/jszopi/restrained-ESP-fit/tree/v2.4).
Also see the corresponding Releases for details on how the code was retrieved ([`v2.2`](https://github.com/jszopi/restrained-ESP-fit/releases/tag/v2.2), [`v2.4`](https://github.com/jszopi/restrained-ESP-fit/releases/tag/v2.4))

Later iterations of this project moved the original `resp` code into the `resp` subdirectory.
As the wrapping code evolves, packages will continue to be produced for versions `2.2.z`, `2.4.z` and any future `resp` versions from upstream.

## Independent evolution

In order to allow for independent evolution of the program, the name of the project, `restrained-ESP-fit` is different from `resp`.
The version numbering of the project will reflect the separation from the `resp` version numbers, most likely by using a new major version, i.e. starting from `3.0.0`.
These versions of the project may alter the calculation logic (the results should be identical, barring potential bug fixes) and the interface to the program.
I am hoping to rewrite this program in Python in order to encourage users to experiment with their own fitting methods and constraints.

# Usage

## Install

In addition to a publicly available source code, this project is available on the Python Package Index (PyPI).
This is partly due to the planned rewrite in Python.
I also found the binary distribution format for Python ("wheels") a simpler alternative to distributing the project over each operating system's package manager.
The project is currently available for most Linux distributions and macOS X.
It should be possible for the Windows binaries to be available too; please open an issue if that would be useful to you.

In order to install this project, you only have to run:

```sh
pip3 install restrained-ESP-fit
```

`pip3` will prefer installing from a binary distribution, if one compatible with your operating system is available.
If one is not available, `pip3` will attempt to compile the Fortran code locally.
This may or may not work, depending on whether the build dependencies can be found on your system.

### Request compatible binaries

One of the aims of this projects is for local compilation not be necessary.
If installation failed, please open an issue including the output of `pip3 -v install restrained-ESP-fit` and the version numbers of your operating system, Python installation and `pip3`.
Hopefully, all that's required is the project maintainer adding your operating system to the CI/CD pipeline without requiring any changes on your side.

### Compile from source

If you don't want to wait for compatible binaries to be provided, you can try to get the compilation from source working on your end.
One reason why the compilation may have failed is that `gfortran` is not in your `$PATH`.
You may need to use a different compiler by setting the `RESP_COMPILER` environment variable prior to invoking pip.
Refer to the [CI/CD recipe](./.github/workflows/main.yml) for what value may be suitable for your operating system.
For example, on macOS X:

```sh
RESP_COMPILER=/usr/local/bin/gfortran-11 pip3 install restrained-ESP-fit
```

For the sake of producing portable binaries, the `resp` program can be linked statically by setting `RESP_STATIC` environment variable to "1".
The libraries linked statically are `libgfortran` and `libquadmath`.
You are required to provide the path to where these static libraries can be found by setting the `RESP_VPATH` variable.
Notice that linking statically uses a different Makefile, and its default compiler is `gcc` instead of `gfortran`.

### Install alternate version

For reproducibility, you may need to install another version of `restrained-ESP-fit`.
For example, there are some input format differences between `resp` versions `2.2` and `2.4`.
To install the latest patch version of `2.2`, run:


```sh
pip3 install 'restrained-ESP-fit>=2.2.0,<2.3.0'
```

## Run

Currently, the only interface to the program is invoking the `restrained-ESP-fit` script.
Its interface is identical to that of the corresponding `resp` program, e.g. for `v2.4.z`:

```
restrained-ESP-fit [-O] -i input -e espot [-o output -p punch -q qin -t qout -w qwts -s esout -j espdb -y esqpotpdb -z esmpotpdb]
```

More detailed usage instructions are only available for v2.2 and are hosted at https://upjv.q4md-forcefieldtools.org/RED/resp/ (if link is down, get your browser to display [the repo version](https://github.com/jszopi/restrained-ESP-fit/blob/v2.2/resp-2.2.html)).
The usage of v2.4 is likely very similar, but so far I have identified at least one discrepancy in the expected input format.
v2.4 was also distributed with the [`README-2.4.txt` file](https://github.com/jszopi/resp/blob/v2.4.1/resp/README-2.4.txt) file.

Subsequent patch versions may introduce Python bindings, at first with arguments corresponding directly to the command line options and subsequently a more Pythonic interface.

# Contributing

`resp` has been the effort of multiple people; this fork is merely a spare time project of one developer.
Due to the maturity of `resp`, the maintenance workload should be manageable, but any new features may come slowly.
If you'd like to help out, please get in touch.
The design of a Pythonic API and a later Python rewrite are interesting challenges that would definitely benefit from more help.

## Development

Development takes place on the `master` branch.
The `resp` version currently being wrapped on `master` is `2.4`, but this may change to a newer minor version if one is released upstream.
To continue producing packages wrapping multiple `resp` versions, branches `v2.2.z` and `v2.4.z` will be updated with any new developments from `master`.
These will likely cease to be supported when the development of version `3.0` starts.

--- 

¹ C. I. Bayly, P. Cieplak, W. D. Cornell and P. A. Kollman, *J. Phys. Chem.*, 1993, **97**, 10269–10280

² U. C. Singh and P. A. Kollman, *J. Comput. Chem.*, 1984, **5**, 129–145
