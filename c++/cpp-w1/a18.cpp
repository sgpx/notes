#include <iostream>
#include <functional>


int main() {
	std::function<void(int)> func = [](int a) {
		std::cout << a*5 << std::endl;
	};

	func(11);
}
