#include <algorithm>
#include <vector>
#include <cstdio>

void sort_ex1() {
	std::vector<int> v = { 5, 1, 3 };
	std::sort(v.begin(), v.end(), std::greater<int>());
	for(auto i = v.begin(); i != v.end(); ++i) {
		printf("%d\n", *i);		
	}
	printf("---\n");	
}

void sort_ex2() {
	std::vector<int> v = { 5, 1, 3 };
	std::sort(v.begin(), v.end(), std::less<int>());
	for(auto i = v.begin(); i != v.end(); ++i) {
		printf("%d\n", *i);		
	}
	printf("---\n");		
}

void sort_ex3() {
	std::vector<int> v = { 5, 1, 3 };
	std::sort(v.begin(), v.end());
	for(auto i = v.begin(); i != v.end(); ++i) {
		printf("%d\n", *i);		
	}
	printf("---\n");	
}

void find_ex4() {
	std::vector<double> d = { 1.5, 2.3, -3.5, 0, 2 };
	auto res = std::find(d.begin(), d.end(), -3.5);
	auto r2 = std::distance(d.begin(), res);
	printf("%f\n", *res);
	printf("%d\n", (int)r2);
}

int main() {
	sort_ex1();	
	sort_ex2();	
	sort_ex3();
	find_ex4();
	return 0;	
}
