# read

built into the shell

## view the manpage

```
man zshbuiltins
/read # to find the read command
# press "n" for next occurence
```

## `-d` delimiter

stops reading at first occurence of specified delimiter

## read and split an array

```sh
$ IFS="," read -rA x <<< "5,6,7"
$ for i in {1..3}; do echo $i = ${x[i]}; done
1 = 5
2 = 6
3 = 7
```
