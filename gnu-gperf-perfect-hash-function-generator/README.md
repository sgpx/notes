# gperf

generates a perfect hash function with zero collisions

# example

```
$ cat > a.txt
jan
feb
mar
$ gperf a.txt > hash_func.c
```

```
$ cat > a.txt
jan,feb,mar,apr,may,jun
$ gperf -e , a.txt > hash_func.c
```
