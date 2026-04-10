/**
 * 
 * Task 5 — Templates Basic

Problem:
Write a generic function add() that adds two values of any type (int, float, double).
Example usage:
auto sum1 = add(3, 4);      // int
auto sum2 = add(2.5, 3.7);  // double
 * 
 */
#include <iostream>

template <typename T> T add(T a, T b) {
    return a + b;
}

int main() {
    auto a = add(5.0,6.1);
    std::cout << a << std::endl;
    return 0;
}