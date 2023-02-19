# serve

# setup

`npm i -g serve`

`yarn add serve`

# examples

serve a directory

```
serve -s build/
```

serve a directory at port 443 over https

```
sudo npx serve -p 443 -s www --ssl-key /etc/letsencrypt/live/mywebsite.com/privkey.pem --ssl-cert /etc/letsencrypt/live/mywebsite.com/cert.pem &
```
