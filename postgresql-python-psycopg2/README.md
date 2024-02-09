# psycopg2

requires libpq

# installation (macOS)

requires libpq binaries in `$PATH`

(ALSO REQUIRES libcrypto* and libssl* to be in the same path as libpq/lib/libpq.dylib, copy from homebrew cellar or make from source and copy)

```
brew install libpq
echo 'export PATH=$PATH:/opt/homebrew/opt/libpq/bin/' > ~/.zshrc
PATH=$PATH:/opt/homebrew/opt/libpq/bin/ pip3 install psycopg2
```

# example

```python


import psycopg2 as p
db_url = "postgres://abc:xyz@foobar.net:5432/mydb"

connection = p.connect(db_url)
cursor = connection.cursor()

cursor.execute("select * from mytable")
rows = cursor.fetchall()
print("query output: ",rows)

```
