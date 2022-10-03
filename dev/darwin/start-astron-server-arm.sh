#!/bin/sh
cd ../../dependencies/astron

# This assumes that your astrond build is located in the
# "astron/darwin" directory.
./astrond-darwin-arm --loglevel info ./config/cluster.yml
