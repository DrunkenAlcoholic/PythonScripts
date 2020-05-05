#!/bin/bash

mkdir build && cd build
meson --buildtype plain --prefix=/usr --libdir=/usr/lib
sudo ninja install
cd ..