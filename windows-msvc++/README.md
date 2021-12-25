# VS 2019 development environment variables

`C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\Common7\Tools\VsDevCmd.bat`

# cl.exe - MSVC Optimizing Compiler

## compile

`cl.exe /EHsc foobar.cpp`

## compile to c++14/17/XX standard

`cl.exe /EHsc /std:c++17 foobar.cpp`

# linking libaries automatically with pragma comment

```c++
#pragma comment(lib,"user32.lib")
#include <cstdio>

int main()
{
	printf("linked to user32.dll\n);
	return 0;
}
```


## `direct.h` - windows header for manipulating file system directories

```c
#include <direct.h>
#include <stdio.h>

int main()
{
	int maxlen = 1024;
	char * xyz = "";
	_getcwd(xyz,maxlen);
	printf("%s\n",xyz);
	return 0;
}
```
