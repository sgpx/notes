## recursion

# base case

condition that stops the recursive calls and allows the function to return a result without making more recursive calls

# call stack

region of memory

serves as a mechanism for managing function calls

operates on a Last In, First Out (LIFO) basis

exceeding stack space causes stack overflow

# stack frame

data structure used to store info about function calls in call stack

contains info about function params, local variables, return address and info that needs to be saved across functions


## bubble sort

swap elements in order during passes

time complexity: O(n^2)

```
let a = [6,4,5,10,1]
let i = 0, j = 0;
let ns = true;
while(true) {
	console.log("loop ", ++j);
	if(i < a.length - 1 && a[i] > a[i+1]) {
		let tmp = a[i];
		a[i] = a[i+1];
		a[i+1] = tmp;
		ns = false;
	}
	i += 1;
	if(i === a.length){
		if(ns) break;
		i = 0;
		ns = true;
	}
}

console.log(a);
```

## selection sort
