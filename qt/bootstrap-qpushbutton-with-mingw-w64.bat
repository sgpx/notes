mkdir example
copy qpushbutton_example_mingw-w64\main.cpp example\main.cpp
cd example
qmake -project
echo QT += widgets >> example.pro
qmake
gmake
cd release
example.exe