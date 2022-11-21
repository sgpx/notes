# DNS

# A record

indicates IPv4 host server IP address of current domain

# AAAA record

indicates IPv6 host server IP address of current domain


# CNAME record

maps alias to real name (canonical name)

must always point to another domain

example

```
NAME                    TYPE   VALUE
--------------------------------------------------
bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23

```

# MX record

indicates mail exchange server address of current domain

# TXT record

stores custom information like verification codes to prove ownership
