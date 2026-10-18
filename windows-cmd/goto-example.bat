echo off
cls
goto blah1

:blah1
echo blah1 %TIME%
goto :blah2

:blah2
echo blah2 %TIME%
goto :blah1
