# pkg-config

get info about installed libraries

## setup

```bash
sudo apt install -y pkg-config
```

## example

list all libraries

```bash
$ sudo apt install -y libyaml-dev
$ pkg-config --list-all
yaml-0.1         LibYAML - Library to parse and emit YAML
```

compile and link cairo with C program

```bash
$ pkg-config --cflags --libs cairo-svg
-I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/aarch64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/uuid -I/usr/include/freetype2 -I/usr/include/libpng16 -lcairo

$ gcc $(pkg-config --cflags cairo-svg) foo.c $(pkg-config --libs cairo-svg) -o foo.out
```

## list all installed libraries

`pkg-config --list-all`

## get compiler flags

```bash
$ pkg-config --cflags cairo-svg
-I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/aarch64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/uuid -I/usr/include/freetype2 -I/usr/include/libpng16
```

## get linker flags

```bash
$ pkg-config --libs cairo-svg
-lcairo
```

## installed `.pc` files location

```bash
ls /usr/share/pkgconfig/*.pc
```
