#include <string>
#include <iostream>

int main()
{
    std::string c1 = "lol";
    std::string c2 = std::move(c1);

    std::cout << "c1: " << c1 << std::endl;
    std::cout << "c2: " << c2 << std::endl;

    return 0;
}