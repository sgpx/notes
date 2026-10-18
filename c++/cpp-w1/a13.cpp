/*

Problem:
Create a class StringWrapper that wraps around std::string.
Implement a move constructor and move assignment operator.

*/
#include <vector>
#include <algorithm>
#include <iostream>

class StringWrapper
{

public:
    std::string mystr;

    StringWrapper(std::string s)
    {
        mystr = s;
    }
    StringWrapper(StringWrapper &&other) noexcept
    {
        mystr = std::move(other.mystr);
    }

    ~StringWrapper() = default;


    StringWrapper &operator=(StringWrapper &&other) noexcept {
        if(this != &other) {
            mystr = std::move(other.mystr);
        }
        return *this;
    }


};

int main()
{
    std::string foo = "foo";
    StringWrapper a(foo);
    StringWrapper b = std::move(a);
    std::cout << b.mystr << std::endl;
}