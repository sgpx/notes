make sure every AppState.addEventListener has an event type and onchange parameter otherwise it can cause the whole app to crash

# CAUSE

leaving a 

```
AppState.addEventListener()
```

in the code
