# commands

```
sudo systemctl start example.service

sudo systemctl restart example.service

sudo systemctl stop example.service
```

# install a service

```
cp ./example.service /etc/systemd/system/example.service

sudo systemctl daemon-reload

sudo systemctl restart example
```

# logs

`journalctl -u example.service`

`journalctl -u example.service -n 50`

