# qt

native UI library

# mingw-w64

define project in `.pro` file

use qmake to generate `Makefile` of make/cmake

# generate qmake project file

run `qmake -project` inside source folder

# bootstrapping the qpushbutton example with only the cpp file (mingw)

```batch
mkdir ..\main
copy main.cpp ..\main
qmake -project
echo QT += widgets >> main.pro
qmake
gmake
cd releases
main.exe
```
