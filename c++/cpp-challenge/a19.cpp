#include <stdexcept>
#include <cstdio>

template<int n> struct xyz {
	enum { val = 2*xyz<n-1>::val };
};

template<> struct xyz<0> {
	enum {val = 1};
};

int main() {
	long a = xyz<5>::val;
	printf("%ld\n", a);
}
