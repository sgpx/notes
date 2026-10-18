/*
## Task 3 — Constructor Overloading & Initializer Lists  
**Problem:**  
Create a class `Person` that has two constructors:
1. A default constructor.
2. A constructor that takes a name and age, using an initializer list.

- Print the person's name and age after construction.
*/
#include <iostream>

class Person
{
public:
    std::string name;
    int age;
    Person() {
    };
    Person(std::string _name, int _age) : name(_name), age(_age)
    {
        std::cout << "name : " << name << std::endl;
        std::cout << "age : " << age << std::endl;
    };
};

int main() {
    Person *p = new Person("1", 5);
    delete p;
    return 0;
}