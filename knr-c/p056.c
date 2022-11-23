#include <stdio.h>

int binsearch(int x, int v[], int n){
	int low = 0;
	int high = n - 1;

	int mid = 0;

	while(low <= high && x != v[mid]){
		mid = (low + high) / 2;
		printf("x : %d\n", x);
		printf("low : %d, mid : %d, high : %d\n", low, mid, high);
		printf("v[low] : %d, v[mid] : %d, v[high] : %d\n", v[low], v[mid], v[high]);
		if(x < v[mid]){
			high = mid - 1;
		}
		else {
			low = mid + 1;
		}
	}

	return x == v[mid] ? mid : -1;
}

int old_binsearch(int x, int v[], int n){
	int low = 0;
	int high = n - 1;

	int mid;

	while(low <= high){
		mid = (low + high) / 2;
		printf("low : %d, mid : %d, high : %d\n", low, mid, high);
		printf("v[low] : %d, v[mid] : %d, v[high] : %d\n", v[low], v[mid], v[high]);
		if(x < v[mid]){
			printf("x = %d < v[mid=%d] = %d\n", x, mid, v[mid]);
			high = mid - 1;
		}
		else if(x > v[mid]){
			printf("x = %d > v[mid=%d] = %d\n", x, mid, v[mid]);
			low = mid + 1;
		}
		else {
			return mid;
		}
	}

	return -1;
}

int main(){
	int arr[6] = { 1, 2, 3, 4, 5, 6};
	int r1 = binsearch(4, arr, 6);
	printf("r1 : %d\n", r1);
}	
