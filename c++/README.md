# classes

```
#include <iostream>
#include <string>

class calc {
	int val;
	public: 
		calc(int x) : val(x) {}

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
```

# unique_ptr

```
#include <memory>
#include <iostream>

void fxn(std::unique_ptr<int> &ptr) {
    std::cout << *ptr << std::endl;	
}

int main() {
    std::unique_ptr<int> ptr(new int(42));
    fxn(ptr);
    std::cout << *ptr << std::endl;
    return 0;
}
```

# shared_ptr

```
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
```

# weak_ptr

```
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
```

# template classes

```
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

int main() {
	Rect<int> r1(4,3);
	Rect<float> r2(2.1, 5.3);
	r1.print();
	r2.print();
	return 0;
}

```
