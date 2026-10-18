/*

Problem:
Create a vector of integers and use lambda functions inside std::for_each to square all the elements.

*/

#include <vector>
#include <algorithm>
#include <iostream>

int main()
{
    std::vector<int> v = {1, 3, 5, 6};
    auto foo = [](int &a)
    {
        a *= a;
    };
    std::for_each(v.begin(), v.end(), foo);

    std::for_each(v.begin(), v.end(), [](int &a)
                  { std::cout << a << std::endl; });
}