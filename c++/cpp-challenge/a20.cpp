#include <iostream>
#include <string>

template <class T>class Rect {
	T l;
	T b;

	public:
		Rect(T x, T y) : l(x), b(y)  {}
		void print() {
			std::cout << "l:" << l << std::endl; 
			std::cout << "b:" << b << std::endl; 
		}
};

template <class T>class Square : Rect {
	T side;

	public:
		Square(T side) : Rect(side, side) {
		}
}

int main() {
	Rect<int> r1(4,3);
	Rect<float> r2(2.1, 5.3);
	r1.print();
	r2.print();
	return 0;
}
