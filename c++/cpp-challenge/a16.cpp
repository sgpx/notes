#include <memory>
#include <iostream>

class my_class {
	int val;
	public:
		my_class(int a): val(a) {}

		void print() const {
			std::cout << this->val << std::endl;
		}
};

int main() {
	auto m = std::shared_ptr<my_class>(new my_class(5));
	auto m2 = m;
	m2->print();
	return 0;
}
