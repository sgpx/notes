# sprintf_s() : secure MSVC alternative to sprintf()

requires size of buffer

`sprintf_s(buf, bufSize, "%d %d", foo, bar)`

to disable sprintf_s() warning define `#define _CRT_SECURE_NO_WARNINGS 1`

# change console application entry file

- open `ConsoleApplication1\ConsoleApplication1\ConsoleApplication1.vcxproj`
- replace `ConsoleApplication1.cpp` with `my-file-name.ext` in XPath `/Project/ItemGroup[2]/ClCompile@Include`

# VS 2022 development environment variables

VS 2022 Community Edition

`C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat`

# VS 2019 development environment variables

32bit

`C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\Common7\Tools\VsDevCmd.bat`

64bit (x64)

"c:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

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

# generate assembly

```
cl.exe /FA a.c
dir a.asm
```

# link.exe - MSVC Linker

## target architecture

use `/MACHINE:X64` or `/MACHINE:X86`

## examples

`link.exe /out:a.exe /entry:main /subsystem:console a.obj kernel32.lib user32.lib msvcrt.lib ucrt.lib`

# `direct.h` - windows header for manipulating file system directories

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

# ml.exe - MSVC assembler

`ml /?`
