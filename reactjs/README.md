# setstate function parameter

used to guarantee that snapshot of previous state is updated, if state change relies on previous state

```
// use
setState(state => state+1);
// instead of
setState(state+1);
```
