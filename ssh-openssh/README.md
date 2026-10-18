# ssh_config

ref: https://linux.die.net/man/5/ssh_config

location: `/etc/ssh/ssh_config`, `/opt/homebrew/etc/ssh/ssh_config`, etc

```
IdentityFile ~/.ssh/id_rsa
Host *
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedKeyTypes +ssh-rsa
```

---

# ssh-keygen

## create public/private key pairs

`ssh-keygen -t rsa -f my_key`

`ssh-keygen -t ed25519 -f my_key`

`ssh-keygen -t ed25519 -f my_key -P mypassphrase`

```
$ ssh-keygen -t ed25519 -f my_key -P mypassphrase & ls
my_key
my_key.pub
```

---

# ssh-add

## add identity to ssh-agent

`ssh-add my_key`

## list 

`ssh-add -l`

## delete key

`ssh-add -d my_key`

## delete all keys

`ssh-add -D`

---

# ssh-agent

ssh authentication agent program. holds private keys in memory for reuse

