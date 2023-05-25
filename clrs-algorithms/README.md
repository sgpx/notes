# CLRS

## ch1

- algorithm is a procedure that takes some input and produces some output

```
def sort(*args):
	return sorted(args)
```

`y = sort(3,4,1,2)`

input: `sort(3,4,1,2)`
output: `y` = `[1,2,3,4]`

- `instance of problem`: valid input satisfying constraints imposed on the problem
- `halt`: stop computing

- algorithm is correct or `valid` if for every `instance` of the problem it `halts` and provides the right solution (i.e. `solves` the problem)
- incorrect algorithms can be useful if their error rate is controlled

- `dynamic programming` used to solve problems to find similarity between DNA 
- cryptography is based on numerical algorithms and number theory

- real world problems can be solved by modeling them as linear programs

- `NP-complete` problems: problems for which no efficient algorithm is proven to exist

### exercises

- 1.1-1

-- real world example that requires sorting: sorting playing cards in hand
-- example of finding shortest distance between two points: food delivery

- 1.1-2

-- measures to consider other than speed: memory usage, CPU usage, etc

- 1.1-3

-- data structure you have seen: array
-- strength: easy to access and sort
-- weakness: searching for elements can take time

- 1.1-4

-- shortest path vs traveling salesman
-- similarity: finds shortest route in a graph
-- difference: traveling salesman must come back to initial point, but shortest path does not

- 1.1-5

-- real world problem for which _only_ the best solution will do: trajectory calculation for space probes, route optimization for trucks and ships
-- real world problem for which _approximately_ the best is good enough: sorting playing cards, any sort problem with small input set

- 1.1-6

-- real world problem in which entire input is available before solving: compressing and decompressing files
-- real world problem in which entire input is not available before solving: route optimization with real time traffic added as a parameter

- 1.2-1

-- application that uses algorithimic content at application level: archivers use algorithms to decompress and extract archives

- 1.2-2

-- input size `sz` = n, steps in insertion sort `si` = `8*n**2`, steps in merge sort = `sm` = `64*n*log(n, base=2)`

```
>>> from math import log
>>> n = 10**5
>>> si = lambda x : 8*(x**2)
>>> sm = lambda x : 64*x*log(x,2)
>>> for i in range(1,n):
...     if si(i) < sm(i): res.append([si(i), sm(i), i])
>>> res
[[32, 128.0, 2], [72, 304.312800138462, 3], [128, 512.0, 4], [200, 743.0169903639559, 5], [288, 992.6256002769239, 6], [392, 1257.6950050818066, 7], [512, 1536.0, 8], [648, 1825.876800830772, 9], [800, 2126.033980727912, 10], [968, 2435.4398595206576, 11], [1152, 2753.2512005538483, 12], [1352, 3078.7658454933885, 13], [1568, 3411.3900101636127, 14], [1800, 3750.614971784178, 15], [2048, 4096.0, 16], [2312, 4447.15957128037, 17], [2592, 4803.753601661543, 18], [2888, 5165.4798563474, 19], [3200, 5532.067961455824, 20], [3528, 5903.274616214654, 21], [3872, 6278.879719041314, 22], [4232, 6658.683199315923, 23], [4608, 7042.502401107697, 24], [5000, 7430.169903639559, 25], [5408, 7821.531690986778, 26], [5832, 8216.445603738475, 27], [6272, 8614.780020327225, 28], [6728, 9016.412726956774, 29], [7200, 9421.229943568356, 30], [7688, 9829.125479807562, 31], [8192, 10240.0, 32], [8712, 10653.760380085054, 33], [9248, 11070.31914256074, 34], [9800, 11489.593957956724, 35], [10368, 11911.507203323086, 36], [10952, 12335.985569809354, 37], [11552, 12762.9597126948, 38], [12168, 13192.363938280172, 39], [12800, 13624.135922911648, 40], [13448, 14058.216460117852, 41], [14112, 14494.549232429308, 42], [14792, 14933.080604940173, 43]]
>>> answer = [i[-1] for i in res] # values
>>> print(answer)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
```

- 1.2-3

-- running time of algorithm 1 `rt1(n)` = `100*(n**2)`
-- running time of algorithm 2 `rt2(n)` = `2**n`
-- find smallest value of n for which `rt1(n) < rt2(n)`

```

>>> for i in range(1,10**5):
...     if rt1(i) < rt2(i): print(i); break
... 
15
>>> rt1(14),rt2(14)
(19600, 16384)
>>> rt1(15),rt2(15)
(22500, 32768)
```

```
100*(n*n) < 2^n
log2(100*n^2) < log2(2^n)
log2(100) + 2*log2(n) < n
6.64 + 2*log2(n) < n
n - 2*log2(n) > 6.64

let, f(k) = k - 2*log2(k) 
if k = 2, f(k) = 2 - 2*log2(2) = 2 - 2 = 0
if k = 4, f(k) = 4 - 2*log2(4) = 4 - 4 = 0
if k = 8, f(k) = 8 - 2*3*log2(2) = 8 - 6 = 2
if k = 16, f(k) = 16 - 2*4 = 16 - 8 = 8
if k = 32, f(k) = 32 - 2*5 = 32 - 10 = 22

since f(k) lies between 2 and 8, t1 lies between 8 and 16
8 < t1 < 16
f(12) = 12 - 2*log2(12) = 4.83
f(14) = 14 - 2*log2(14) = 6.38 (< 6.64)

therefore value = 14+1 = 15
```

- problem 1-1

```
f(n) = t
log2(n) = t
n = 2^t
```

-- time = 1s, t = 1000, n = 2^1000

-- time = 1m, t = 60*1000, n = 2^(60000)

-- time = 1h, t = 3600*1000, n = 2^(3600000)

-- time = 1d, t = 86400 * 1000, n = 2^(86400*1000)

-- time = 1 month, t = 30 * 86400 * 1000, n = 2^(30 * 86400 * 1000)

-- time = 1 year, t = 12 * 30 * 86400 * 1000, n = 2^(12 * 30 * 86400 * 1000)

-- time = 1 century, t = 12 * 30 * 86400 * 1000, n = 2^(100 * 12 * 30 * 86400 * 1000)

```
f(n) = t
sqrt(n) = t
n = t^2
```

-- time = 1s, t = 1000, n = 1000^2

-- time = 1m, t = 60*1000, n = (60000)^2

-- time = 1h, t = 3600*1000, n = (3600000)^2

```
f(n) = t
n = t
```

```
f(n) = t
n*log2(n) = t
```

-- time = 1s, t = 1000, n = 140.25 approx

-- time = 1m, t = 60*1000, n = 4896

## ch2

- sorting

-- input: sequence of n numbers A = (a1, a2, ... an)

-- output: permutation A' = (a1', a2', ..., an') where a1' < a2' < ... < an'

-- numbers to be sorted are also known as `keys`

-- keys are associated with data called `satellite data`

-- `key` + `satellite data` = `record`

- insertion sort

-- efficient for sorting small number of elements

```
def insertion_sort(a : list) -> list:
	for i in range(1,len(a)):
		key = a[i]
		j = i - 1
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key
	return a
```

```
def insertion_sort(a : list) -> list:
        for i in range(1,len(a)):
		print(a)
		print(f"\n\ni : {i}, a[i] : {a[i]}")
		print("a:", a)
		print("\n\nkey i:", i)
                key = a[i]
                j = i - 1
		print(f"j : {j}, a[j] : {a[j]}")
                while j >= 0 and a[j] > key:
			print(f"inside loop j : {j}, a[j] : {a[j]}")
			print(f"setting a[j+1] {j+1} as a[j] {j}")
			print(a)
			print("a:", a)
			print("key j:", j)
                        a[j+1] = a[j]
			print(a)
                        j -= 1
		print(f"setting j+1 : {j+1}, a[j+1] : {a[j+1]}, key : {key}")
                a[j+1] = key
		print(a)
        return a
```

example progression

```
[4, 5, 1, 2]
[4, 5, 5, 2]
[4, 4, 5, 2]
[1, 4, 5, 2]
[1, 4, 5, 5]
[1, 4, 4, 5]
[1, 2, 4, 5]
```

`loop invariant`: property of a program that is true before and after each loop iteration

to show use of a loop invariant, show three things:

1. initialization: condition is true prior to first iteration of the loop
2. maintenance: true before an iteration of the loop, true before the next iteration
3. termination: loop terminates and when it terminates the invariant gives a useful property that shows algorithm is correct

when first two properties hold, loop invariant is true prior to every iteration of the loop

loop invariant proof is a type of mathematical induction

to prove a property holds, you prove base step and inductive stepp

showing the invariant holds before the first iteration corresponds to the base step

showing that the invariant holds from iteration to iteration corresponds to inductive step

in loop invariant induction stops when loop terminates

### exercises

- 2.1-1

```
>>> arr = [31, 41, 59, 26, 41, 58]
>>> insertion_sort(arr)
a: [31, 41, 59, 26, 41, 58]
a: [31, 41, 59, 59, 41, 58]
a: [31, 41, 41, 59, 41, 58]
a: [26, 31, 41, 59, 41, 58]
a: [26, 31, 41, 41, 59, 58]
```
- 2.1-2

```
def sum_array(a):
	res = 0
	for i in a:
		res += i
	return res
```

# big O notation O(n)

worst case time complexity

O(f(n)) = g(n) such that there exists c > 0 for which c*g(n) >= f(n) for all values of n>0
O(4n^3 + n^2) = n^3 because 

4n^3 + n^2 =< kn^3

(k-4)*(n^3) >= 1n^2

(k-4)*n >= 1

(5-4)*n >= 1

# big omega notation omega(n)

best case time complexity

omega(f(n)) = g(n) such that there exists c > 0 such that g(n) <= c*f(n)

f(n) = 4n^3 + n^2

g(n) = n^3

n^3 <= k(4*n^3 + n^2)

(1-4k)n^3 <= n^2

(1-4k)n <= 1

taking n = 1, fits for any k >= 0

# theta notation theta(n)

omega(f(n)) = g(n) such that g(n) = O(f(n)) and g(n) = omega(f(n))

# greedy algorithms

try to find a localized optimum solution, which may eventually lead to globally optimized solutions

example 1: use denominations of 1,2,5,10 coins to get 18 with the fewest number of coins

greedy solution:

1. pick the highest possible number (10), balance = 18 - 10 = 8
2. pick the highest possible number (5), balance = 8 - 5 = 3
3. pick the highest possible number (2), balance = 3 - 2 = 1
4. pick the highest possible number (1), balance = 0

example 2: use denominations of 1,7,10 coins to get 18

greedy solution: 10 + 7 + 1

example 3: use denominations of 1,7,10 coins to get 15

greedy solution: 10 + 1 + 1 + 1 + 1 + 1

optimal solution: 7 + 7 + 1

greedy example: djisktra's MST

# divide and conquer

divide the problem into smaller subproblems, recursively merge the solutions back

divide and conquer example: merge sort

# dynamic programming

divide problem into smaller subproblems, solve subproblems independently and use the solution of one subproblem to help with the other subproblems

e.g. tower of hanoi, fibonacci
