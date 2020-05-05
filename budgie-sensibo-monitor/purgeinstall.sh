#!/bin/bash

cd build
sudo ninja uninstall
cd ..
rm -rf build
mkdir build && cd build
meson --buildtype plain --prefix=/usr --libdir=/usr/lib
sudo ninja install
cd ..