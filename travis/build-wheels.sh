#!/bin/bash

# Based on https://github.com/pypa/python-manylinux-demo/blob/84dc72039a0c85c1c960e024f024fd3d37387634/travis/build-wheels.sh

set -e -u -x

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /io/wheelhouse/
    fi
}


# Compile wheels
for PYBIN in /opt/python/*/bin; do
    # "${PYBIN}/pip" install -r /io/dev-requirements.txt
    "${PYBIN}/pip" wheel /io/ --no-deps -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install python-manylinux-demo --no-index -f /io/wheelhouse
    # (cd "$HOME"; "${PYBIN}/nosetests" pymanylinuxdemo)
done
