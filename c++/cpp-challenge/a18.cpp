#include <stdexcept>
#include <cstdio>

int main() {
	try {
		printf("running..");
		throw(123);
	}
	catch(int err) {
		printf("error : %d\n", err);
	}
}
