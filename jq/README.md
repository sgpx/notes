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

