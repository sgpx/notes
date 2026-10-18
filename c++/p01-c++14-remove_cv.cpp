#include <type_traits>
#include <iostream>

int main()
{
	using my_type = std::remove_cv<const int>::type;
	my_type my_int = 5;

	my_int = 6;

	std::cout << my_int << std::endl;

	return 0;
}
