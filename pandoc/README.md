# install

`pip3 install pandoc`


# example

```
for i in {0..99}; do pandoc --from gfm --to html --standalone --metadata title="Example $i" ex$i.md > ex$i.html; done
```

```
pandoc --from gfm --to docx --standalone --metadata title="Report" s1.md -o s.docx
```
