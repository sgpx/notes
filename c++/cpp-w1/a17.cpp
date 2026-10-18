#include <iostream>
#include <functional>

void sayHello(int x) {
	std::cout << "hello: " << x*2  << std::endl;
}

int main() {
	std::function<void(int)> func = sayHello;
	func(5);
}
