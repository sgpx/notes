/*
Problem:

Create a std::vector<StringWrapper>.
Add multiple StringWrapper objects to it.
Move the whole vector into another vector.
Print out the strings from the new vector.
Confirm that moving did not copy strings unnecessarily.
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

    StringWrapper &operator=(StringWrapper &&other) noexcept
    {
        if (this != &other)
        {
            mystr = std::move(other.mystr);
        }
        return *this;
    }
};

int main()
{
    std::vector<StringWrapper> v;
    v.push_back(StringWrapper("hello1"));
    v.push_back(StringWrapper("hello2"));
    v.push_back(StringWrapper("hello3"));

    std::vector<StringWrapper> v2 = std::move(v);
    for(auto iter = v.begin(); iter != v.end(); ++iter) {
        std::cout << "v : " << iter->mystr << std::endl;
    }

    for(auto iter = v2.begin(); iter != v2.end(); ++iter) {
        std::cout << "v2 : " << iter->mystr << std::endl;
    }

    return 0;
}