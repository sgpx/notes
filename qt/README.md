# qt

native UI library

# mingw-w64

define project in `.pro` file

use qmake to generate `Makefile` of make/cmake

# generate qmake project file

run `qmake -project` inside source folder

# bootstrapping the qpushbutton example with only the cpp file (mingw)

```batch
mkdir example
copy qpushbutton_example_mingw-w64\main.cpp example\main.cpp
cd example
qmake -project
echo QT += widgets >> example.pro
qmake
gmake
cd release
example.exe
```
