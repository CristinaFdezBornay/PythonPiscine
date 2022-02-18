#!/bin/sh

echo "\n\n=== INSTALLING NEEDED PACKAGES"
echo "\n=> pip"
python3 -m pip install --upgrade pip
echo "\n=> build"
python3 -m pip install --upgrade build
echo "\n=> wheel"
python3 -m pip install --upgrade wheel

echo "\n\n=== BUILDING MY_MINIPACK"
python3 -m build
