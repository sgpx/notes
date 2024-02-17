#include <iostream>
#include <string>

class Rect {
	int l;
	int b;

	public:
		Rect(int a, int c) : l(a), b(c)  {}
		void print() {
			std::cout << "l:" << l << std::endl; 
			std::cout << "b:" << b << std::endl; 
		}
};

class Square : public Rect {
	public:
		Square(int s) : Rect(s,s) {
			
		}
};

int main() {
	Square s = Square(5);
	s.print();
	return 0;
}
