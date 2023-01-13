# CPanel WHM API setup

0. login to cpanel
1. go to [security] > [manage api tokens]
2. create API token

# SSH setup (mac)

valid for version 102.0.24

0. login to cpanel
1. go to [security] > [ssh access]
2. click "generate a new key"
3. enter key name (default : id_rsa) and key passphrase
4. generate key and then authorize the key
5. download public key (id_rsa.pub) and private key (id_rsa)
6. copy id_rsa and id_rsa.pub to ~/.ssh/
6. add public key with ip address to ~/.ssh/known_hosts
7. in ssh_config (usually located at /opt/homebrew/etc/ssh/ssh_config) add the following lines
```
IdentityFile ~/.ssh/id_rsa
Host *
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedKeyTypes +ssh-rsa
```
8. `chmod 600 id_rsa`
9. `ssh-add ~/.ssh/id_rsa` to avoid repeated passphrase prompts
10. `ssh -v $username@$ip_address` or `ssh -i $private_key_path $username@$ip_address`
