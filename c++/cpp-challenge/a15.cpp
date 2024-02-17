#include <memory>
#include <iostream>

void fxn(std::unique_ptr<int> &ptr) {
    std::cout << *ptr << std::endl;	
}

int main() {
    std::unique_ptr<int> ptr(new int(42));
    fxn(ptr);
    std::cout << *ptr << std::endl;
    return 0;
}
