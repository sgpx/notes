# install git LFS on ubuntu

`sudo apt install -y git-lfs`

# get commit diff

`git diff`

# get remote url

`git remote origin get-url`

# set remote url

`git remote origin set-url https://abc.xyz/efgh.git`

# erase credentials

`git clean credentials`

# MACOS github private repository not found authentication workaround

`git clone https://$myusername:$mypassword@github.com/myusername/myrepo`


# reset to previous commit (revert all un-committed changes)

`git reset --hard`

# clone a repo with submodules

`git clone https://github.com/sgpx/musicdb --recursive`

# get submodule contents manually

`git submodule update --init`

# setup with URL

```bash
git init
git remote add origin https://git.xyz.com/blah.git
git add . && git commit -m foobar
git push --set-upstream origin main
```
