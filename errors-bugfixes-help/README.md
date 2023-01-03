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
