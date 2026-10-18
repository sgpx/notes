#include <iostream>
#include <string>

class StringHolder {
	public:
		std::string target;
		StringHolder(std::string s) {
			target = s;
		}
		StringHolder(const StringHolder& other) {
			std::cout << "copy constructor called" << std::endl;
			target = other.target;
		}
		StringHolder(StringHolder&& other) noexcept {
			std::cout << "move constructor called"<< std::endl;
			target = std::move(other.target);
		}
		~StringHolder() = default ; 
};

int main() {
	StringHolder sh1("foobar");
	StringHolder sh2 = sh1;
	std::cout << sh2.target << std::endl;
	StringHolder sh3 = std::move(sh1);
}
