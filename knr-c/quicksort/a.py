#!/usr/bin/env python3

def strcmp(x : str, y : str):
	i = 0
	lx = len(x)
	while (x[i] == y[i]) and (i < lx):
		i += 1
	if i == lx:
		return 0
	print(x[i], y[i], ord(x[i]), ord(y[i]))
	res = ord(x[i]) - ord(y[i])
	if res == 0: return 0
	elif res > 0: return 1
	else: return -1	

def swap(arr : list, i : int, j : int):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp

def part(arr : list, low : int, high : int):
	print("part")
	pivot = arr[high]
	i = low - 1
	j = low
	while (j <= high - 1):
		if (arr[j] < pivot):
			i += 1
			swap(arr, i, j)	
		j += 1
	swap(arr, i+1, high)
	return (i + 1)

def qsort(arr : list, low : int, high :int):
	print("qsort")
	if low >= high:
		return
	pindex = part(arr, low, high)
	qsort(arr, low, pindex - 1)
	qsort(arr, pindex + 1, high)

		
if __name__ == "__main__":
	xarr = ["xyz", "abc", "jkl", "pqrs", "hij"]
	qsort(xarr, 0, 4)
	print(xarr)
