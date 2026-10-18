# try_files

```
    location / {
        try_files $uri $uri/ /index.html;
    }
```

# timeout

```

{

    client_body_timeout 12s;
    client_header_timeout 12s;
    keepalive_timeout 65s;
    send_timeout 30s;

    # Proxy timeouts (if you're using proxying)
    proxy_read_timeout 300s;
    proxy_connect_timeout 300s;
    proxy_send_timeout 300s;


}
```
# client_max_body_size

```
    client_max_body_size 10mb;
```
