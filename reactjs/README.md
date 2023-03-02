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
