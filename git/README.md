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
