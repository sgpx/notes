# output downloaded file as `-O`

`wget -v https://repo1.maven.org/maven2/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.jar -O x.jar`

# resume interrupted download `-c`

```
$ wget ftp://1.2.3.4:5678/a.tgz
^C
$ wget -c ftp://1.2.3.4:5678/a.tgz
```
