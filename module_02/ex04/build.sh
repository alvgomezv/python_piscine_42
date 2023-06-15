#!/bin/bash

python -m pip install --upgrade pip wheel setuptools  build
cd ./my_minipack
python setup.py sdist bdist_wheel


