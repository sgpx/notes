#include <iostream>
#include <string>

class calc {
	int val;
	public: 
		calc(int x) {
			this->val = x;
		}

		~calc() {
			std::cout << "destructor called for calc " << this->val << std::endl;
		}

		void add(int x) {
			this->val += x;
		}
		void print() {
			std::cout << this->val << std::endl;
		}
};

int main() {
	calc * a = new calc(2);
	a->add(5);
	a->print();
	delete a;
	calc b = calc(5);
	b.print();
	return 0;
}
