# .deb

are .tar.gz files with control.tar.gz and data.tar.xz inside

`control` from control.tar.gz contains list of dependencies

```
$ ls
alpine-pico_2.21+dfsg1-1build1_amd64.deb
$ tar xvzf alpine-pico_2.21+dfsg1-1build1_amd64.deb 
x debian-binary
x control.tar.xz
x data.tar.xz
$ ls
alpine-pico_2.21+dfsg1-1build1_amd64.deb	data.tar.xz
control.tar.xz					debian-binary
$ tar xvzf control.tar.xz 
x ./
x ./control
x ./md5sums
x ./postinst
x ./prerm
$ ls
alpine-pico_2.21+dfsg1-1build1_amd64.deb	data.tar.xz					postinst
control						debian-binary					prerm
control.tar.xz					md5sums
$ more control
Package: alpine-pico
Source: alpine
Version: 2.21+dfsg1-1build1
Architecture: amd64
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Installed-Size: 763
Depends: libc6 (>= 2.14), libtinfo5 (>= 6)
Section: editors
Priority: optional
Homepage: http://alpine.freeiz.com/alpine/
Description: Simple text editor from Alpine, a text-based email client
 "pico" is a simple but powerful text editor.  It was originally the pine
 composer,  the editor used by the pine email client for writing email messages.
 .
 It has gained popularity since its initial use in that context and is now used
 as a stand-alone editor by many users.
 .
 It is similar to but less powerful than GNU Nano, an editor created with the
 pico interface when the pico license was non-free.

```

