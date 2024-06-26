# nginx cannot find files 404

```
sudo chown -R www-data /var/www/html
```

# nextjs automatic margin added to body tag

```
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  );
}
```
# next head html tag client side error

do not use `<html lang="en" />` inside `<Head>` from `next/head`

# connect to wifi via command line on macOS

```
networksetup -setairportnetwork en0 mynetworkSSID mypassword
```

# error `<qpa/qplatformdialoghelper.h>` missing while building LXQT components

on ubuntu 22.04 LTS

`sudo apt install -y qtbase5-private-dev`

# disable touchpad lock while pressing keyboard buttons

see `../xinput/touchpad-disable-lock-while-keypress.sh`

```
xinput --list
xinput list-props $device_id | grep -i "disable while typing"
xinput set-prop $device_id $prop_id 0

# expo go not launching in iOS simulator (FBScene failed)

update macOS and xcode

# android `findViewById(R.id.my_element) must not be null`

make sure layout is inflated before trying to access view objects with findViewById

```
// this will cause null pointer errors
findViewById(R.id.something) 
setContentView(R.layout.activity_main)

// this will work
setContentView(R.layout.activity_main)
findViewById(R.id.something)
```

# express + nextjs trailing slash and MIME issue

using nextJS request handler solves this issue

```
const nextJsHandler = nextJsApp.getRequestHandler();
app.use('/', (req, res) => nextJsHandler(req, res));
app.use('/', (req, res) => nextJsApp.render(req, res));
```


```
app.use('/', (req, res) => nextJsApp.render(req, res, req.path, req.query));
```

fails to work for trailing slashes probably because of how express routing works for paths/subpaths

this works sometimes

```
app.use('*', (req, res) => nextJsApp.render(req, res, req.path, req.query));
```

but will cause problems with other routes and may mess up the application


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
