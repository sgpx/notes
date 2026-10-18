# pulseaudio

# GUI controller

`sudo apt install -y pavucontrol-qt`

# change resample method

```
sudo echo "resample-method: speex-float-10" >> /etc/pulse/daemon.conf
sudo pulseaudio -k
pulseaudio --start
```

```
sudo pulseaudio -k
pulseaudio --start --resample-method speex-float-10
```
