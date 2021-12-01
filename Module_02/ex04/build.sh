#!/bin/sh

echo "=== REMOVING MYMINIPACK ==="
python3 -m pip uninstall myminipack -y
rm -rf dist
echo "\n\n=== INSTALLING NEEDED PACKAGES ==="
echo "[ It will also be done when creating the source distribution... ]"
echo "\n=> setuptools"
python3 -m pip install --upgrade setuptools
echo "\n=> wheel"
python3 -m pip install --upgrade wheel
echo "\n\n=== LISTING INSTALLED PACKAGES ==="
python3 -m pip list
echo "\n\n=== CHECKING CONFIGURATION ==="
python3 setup.py check 2> err_setup.txt
err_setup=$(cat err_setup.txt)
rm -rf err_setup
if [ "$err_setup" != "" ]
then
    echo "FAILED INSTALLATION ON THE PACKAGE"
    echo "\tThe setup.py contains the following error:\n\t"$err_setup
    exit 1
fi
echo "\n\n=== CREATING SOURCE DISTRIBUTION ==="
echo "\n=> wheel"
python3 setup.py bdist_wheel
echo "\n=> dist"
python3 setup.py sdist
echo "\n\n=== REMOVING UNEEDED FILES ==="
rm -rf build
rm -rf myminipack.egg-info
echo "\n\n=== INSTALLING MINIPACK ==="
echo "\n=> wheel"
pip install ./dist/myminipack-1.0.0-py3-none-any.whl
echo "=== LISTING INSTALLED PACKAGES ==="
python3 -m pip list
echo "=== UNINSTALLING MYMINIPACK ==="
python3 -m pip uninstall myminipack -y
echo "\n=> dist"
pip install ./dist/myminipack-1.0.0.tar.gz
echo "=== LISTING INSTALLED PACKAGES ==="
python3 -m pip list
echo "=== UNINSTALLING MYMINIPACK ==="
python3 -m pip uninstall myminipack -y