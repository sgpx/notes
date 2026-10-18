# GNU mailutils

# setup (ubuntu)

```
sudo apt install -y mailutils
```

# send email

```
echo $mail_body | mail -s $mail_subject target@destination.com
```
# add custom FROM sender name header

```
mail -s "mysubject" -a "From: mywebsite Admin <admin@mywebsite.com>"
```
