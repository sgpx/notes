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

template <class T>class Square : public Rect<T> {
	T side;

	public:
		Square(T side) : Rect<T>(side, side), side(side) {
		}
};

int main() {
	Square<float> s1(4.5);
	s1.print();
	return 0;
}
