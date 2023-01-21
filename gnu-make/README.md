# make

# Makefile example

```
all:
	cc a.c -o a.out -lcurl

clean:
	rm -v $(find . -iname "*.out")
```
