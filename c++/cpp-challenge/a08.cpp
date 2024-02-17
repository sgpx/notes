#include <iostream>

int main() {
	int a[5], tot = 0;
	for(int i=0; i<5; i++) {
		std::cin >> a[i];
		std::cout << a[i] << std::endl;
		tot += a[i];
	}
	std::cout << tot << std::endl;
	return 0;
}
