# avoid letsencrypt cert chain not verified error

```
sudo certbot certonly -d mywebsite.com
sudo cp /etc/letsencrypt/live/mywebsite.com/fullchain.pem cert-with-chain.pem
sudo cat /etc/letsencrypt/live/mywebsite.com/cert.pem >> cert-with-chain.pem
```

# expressjs middleware priority

```
app.get("/api/", (_, res) => res.send("OK"));
app.use(expressStatic("public"));
```

# firefox CORS TypeError SameOrigin error

check if an HTTPS endpoint is being called from an HTTP hosted page

# SCP/SFTP gives `received message too long`

newlines after export in bashrc can cause bash to echo environment variables when it loads

bashrc motd etc have to be silent for noninteractive sessions in order to not interfere with scp

```
.bashrc, .bash_profile, .cshrc, .profile, etc., have to be silent for non-interactive sessions or they interfere with the sftp / scp connection protocol. 
```

https://unix.stackexchange.com/questions/61580/sftp-gives-an-error-received-message-too-long-and-what-is-the-reason

# /bin/bash not found while chroot-ing

use `bincp` or copy all object dependenies to chroot equivalent folders

```
$ ldd /bin/bash
```

# Z_OK undeclared error while building binutils

install [zlib](zlib.net)

# df cannot find filesystems after util-linux upgrade on 2.6

downgrade util-linux to the chronologically closest release

# "C compiler cannot create executables" build error

```
LD_LIBRARY_PATH=/usr/local/lib ./configure
LD_LIBRARY_PATH=/usr/local/lib make -j11
sudo LD_LIBRARY_PATH=/usr/local/lib make install
```

# android emulator QEMU 0.0.0.0/127.0.0.1/ipaddr not reachable connection refused

use `http://10.0.2.2:PORT/` instead

# podman time sync fix

kill -9 $gvproxy_pid
kill -9 $qemu_pid

# node-sass 5.0 compile error with "remove_cv_t" in `v8-internal.h`

macOS

```
sed -i s/remove_cv_t/remove_cv/g /var/folders/sn/XXXXXXXXX/T/.node-gyp/16.15.0/include/node/v8-internal.h
```

# EAS expo fix "package.json was not found" error

folder name should be the same as name of the project listed in package.json
