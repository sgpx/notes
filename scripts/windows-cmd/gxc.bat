cdate.bat > tmp.txt
set /p commitdate=<tmp.txt
del tmp.txt
gx %commitdate%

