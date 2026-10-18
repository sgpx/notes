/**
 * 
 * 
 * Problem:
Create a vector of integers.
Sort it using std::sort.
Find a specific element using std::find.
Bonus: Reverse the vector using std::reverse
 */
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v = {1, 4, 1, 0, -1, -9, 6};
    auto x = std::find(v.begin(), v.end(), -1);
    std::cout << distance(v.begin(), x) << std::endl;
    std::reverse(v.begin(), v.end());
    std::sort(v.begin(), v.end(), std::greater<int>());
    return 0;
}