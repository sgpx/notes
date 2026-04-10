#include <iostream>
#include <functional>

void sayHello() {
	std::cout << "hello" << std::endl;
}

int main() {
	std::function<void()> func = sayHello;
	func();
}
