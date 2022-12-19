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
