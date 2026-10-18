# (make dcl recover from input errors)

## error 1 

```
>>> int x(
syntax error
>>> int x()
int :
```

happens because the new gettoken() call is made inside the previous dcl() call
