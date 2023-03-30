#!/bin/bash

python -m pip install --upgrade pip
python -m pip install --upgrade pip wheel setuptools
python -m pip install --upgrade build
cd ex04/my_minipack
python -m build


