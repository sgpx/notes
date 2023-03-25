# check component performance with `<React.Profiler>`

```
import React from "react";

const MyComponent = () => <div>123</div>;

const logMetrics = (
  id, // the "id" prop of the Profiler tree that has just committed
  phase, // either "mount" (if the tree just mounted) or "update" (if it re-rendered)
  actualDuration, // time spent rendering the committed update
  baseDuration, // estimated time to render the entire subtree without memoization
  startTime, // when React began rendering this update
  commitTime, // when React committed this update
  interactions // the Set of interactions belonging to this update
) =>
  console.log({
    id,
    phase,
    actualDuration,
    baseDuration,
    startTime,
    commitTime,
    interactions,
  });

const App = () => (
  <React.Profiler onRender={logMetrics}>
    <MyComponent />
  </React.Profiler>
);

export default App;
```

# css modules

component scoped CSS classes, must be named as `myModule.module.css`

```
.myClass
{
	background-color: green;
}
```

```
import myModule from "./myModule.module.css";

const App = () => <div className={myModule.myClass}></div>;
```

# reactdom portal

render react elements to another HTML target that is not #root

# refs

used to access and manipulate HTML elements

```
const MyComponent = () => {
  const myRef = useRef();
  const fxn = () => console.log(myRef.current.value);
  return <div><input ref={myRef} /><button onClick={fxn} >submit</button></div>;
}
```

# setstate function parameter

used to guarantee that snapshot of previous state is updated, if state change relies on previous state

```
// use
setState(state => state+1);
// instead of
setState(state+1);
```
