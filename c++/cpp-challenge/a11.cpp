#include <iostream>
#include <string>

int main() {
	std::string s;
	std::cin >> s;
	int i = 0, l = s.length();
	std::string ns = "";
	while(l > 0) {
		ns += s[--l];
	}
	std::cout << ns << std::endl;
	return 0;
}
