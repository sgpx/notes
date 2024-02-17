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
	auto m2 = std::weak_ptr<my_class>(m);
	auto m3 = m2.lock();

	if(m3) {
		m3->print();
	}
	else std::cout<< "Expired" << std::endl;

	m.reset();
	auto m4 = std::weak_ptr<my_class>(m);
	auto m5 = m4.lock();
	if(m5) {
		m5->print();
	}
	else std::cout<< "Expired" << std::endl;

	return 0;
}
