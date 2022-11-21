# redirect all args

a.bat

```batch
C:\a.exe %*
```

# refresh environment variables without exiting shell

`refreshenv`

```
C:\Windows\system32>refreshenv
Refreshing environment variables from registry for cmd.exe. Please wait...Finished..
```

# set environment variables

`set MYVAR="myvalue"`

# get date and time

`echo %DATE%`

`echo %TIME%`

# get args for batch file

`echo %1%` => first argument

# do not display output the executed command to CMD

example.bat

```batch
@echo 123
echo 456
```

```
C:\>a.bat
123

C:\>echo 456
456
```
