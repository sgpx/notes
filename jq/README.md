# jq

```
$ echo '{"a":"b"}' | jq '.'
{
  "a": "b"
}
```

# file

`jq '.' a.json`

# key

```
$ echo '{"a":"b"}' | jq '.a'
"b"
```

# raw string

```
$ echo '{"a":"b"}' | jq -r '.a'
b
```

# parse quoted JSON string

```
$ echo '{"a":"{\"c\": 1}"}' | jq '.a | fromjson | .' 
{
  "c": 1
}
$ echo '{"a":"{\"c\": 1}"}' | jq '.a | fromjson | .c' 
1
```

# object to key-value pairs

`jq '. | to_entries' a.json`

# mapping

`jq '.dependencies | to_entries | map (.key)' package.json`

gives an array of packages

# iterating

```
$ echo '["a", "b", "c"]' | jq '.[]'
"a"
"b"
"c"
$ echo '["a", "b", "c"]' | jq '.[0]'
"a"
$ echo '["a", "b", "c"]' | jq '.[1:2]'
[
  "b"
]
$ echo '["a", "b", "c"]' | jq '.[1:]'
[
  "b",
  "c"
]
$ echo '["a", "b", "c"]' | jq '.[0:2]'
[
  "a",
  "b"
]
```

# pipe wget output to jq

`wget https://jsonplaceholder.typicode.com/posts -q -O - | jq '.[0]'`

# gets keys of object

```
jq -r '.dependencies | keys | .[]' package.json
```

```
$ echo '{"a":{"pkgs":{"p1":1,"p2":2,"p3":3}}}' | jq '.a.pkgs'
{
  "p1": 1,
  "p2": 2,
  "p3": 3
}
$ echo '{"a":{"pkgs":{"p1":1,"p2":2,"p3":3}}}' | jq '.a.pkgs | keys'
[
  "p1",
  "p2",
  "p3"
]
$ echo '{"a":{"pkgs":{"p1":1,"p2":2,"p3":3}}}' | jq '.a.pkgs | keys | .[]'
"p1"
"p2"
"p3"
$ echo '{"a":{"pkgs":{"p1":1,"p2":2,"p3":3}}}' | jq -r '.a.pkgs | keys | .[]'
p1
p2
p3
```

# keys with spaces

```
$ echo '{"foo bar":"baz"}' | jq '."foo bar"'
baz
```
