# Package: my_minipackage

Exercise of the Python Piscine from 42AI.

## 1. Build the package
`sh build.sh`

This script will install the dependencies and create the needed resources for a later installation.

## 2. Installing the package
To check if the package has properly installed:
* `python3 -m pip list`
* `python3 -m pip show -v my_minipack`

To uninstall the package: `python3 -m pip uninstall my_minipack -y`.

### 2.1. Installation from .tar
`python3 -m pip install ./dist/my_minipack-1.0.0.tar.gz`.

### 2.2. Installation from .whl
`python3 -m pip install ./dist/my_minipack-1.0.0-py3-none-any.whl`.

## 3. Testing
### 3.1. progressbar

````
from my_minipack.progressbar import *
ret = 0
X = range(100, 200)
for elem in ft_progress(X):
    ret += (elem + 3) % 5
    time.sleep(0.1)
````
### 3.2. logger
````
from my_minipack.logger import *
machine = CoffeeMachine()
for i in range(0, 5):
    machine.make_coffee()
machine.add_water(70)
````
