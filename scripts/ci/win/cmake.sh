#!/bin/bash

pwd
where cl.exe
export CC=cl.exe
export CXX=cl.exe
cmake .. -G "Ninja" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX="$CONDA_PREFIX" \
    -DWITH_TESTS=ON \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DCMAKE_LIBRARY_PATH:FILEPATH="$CONDA_PREFIX/Library/lib" \
    -DCMAKE_INCLUDE_PATH:FILEPATH="$CONDA_PREFIX/Library/include" \
    -DOPENSSL_ROOT_DIR="$CONDA_PREFIX/Library" \
    -DPython3_ROOT_DIR:FILEPATH="$CONDA_PREFIX" \
    -DPython3_FIND_STRATEGY=LOCATION \
    -DBUILD_PLUGIN_CPD=OFF \
    -DBUILD_PLUGIN_ICEBRIDGE=ON \
    -DBUILD_PLUGIN_HDF=ON \
    -DBUILD_PLUGIN_MRSID=OFF \
    -DBUILD_PLUGIN_NITF=ON \
    -DBUILD_PLUGIN_PGPOINTCLOUD=ON \
    -DBUILD_PLUGIN_I3S=ON \
    -DBUILD_PLUGIN_DRACO=ON \
    -DBUILD_PLUGIN_RIVLIB=OFF \
    -DENABLE_CTEST=OFF \
    -DWITH_LZMA=OFF \
    -DLIBLZMA_LIBRARY:FILEPATH="$CONDA_PREFIX/Library/lib/liblzma.lib" \
    -DHDF5_DIR:FILEPATH="$CONDA_PREFIX/Library/cmake" \
    -DWITH_ZLIB=ON \
    -Dgtest_force_shared_crt=ON \
    -DBUILD_PGPOINTCLOUD_TESTS=OFF
