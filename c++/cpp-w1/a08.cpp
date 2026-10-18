/*
Task — Debug Printer

Problem:
Create a variadic template function debug() that prints all its arguments, separated by commas.
Example:
debug(1, "hello", 3.14);
// Output: 1, hello, 3.14
✅ Focus: Variadic templates (if you want extra challenge).
*/

#include <iostream>


template <typename T, typename ... Args> void debug(T a) {
    std::cout << a << std::endl;
}

template <typename T, typename ... Args> void debug(T a, Args... args) {
    std::cout << a << ", ";
    debug(args...);
}

int main() {
    debug(1, "hello", 3.14);
    return 0;
}