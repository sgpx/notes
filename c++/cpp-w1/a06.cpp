/*
Task: Simple Resource Manager (RAII)

Problem:
Simulate managing a file resource:
Write a class FileHandler that "opens" a file on construction (simulate with std::cout) and "closes" it on destruction.
No explicit close() calls — use RAII. */

#include <iostream>
#include <fstream>

class FileHandler
{
    public:
        std::ifstream myfile;

        FileHandler(const std::string& fpath) : myfile(fpath) {
            std::cout << "file opened" << std::endl;
        }

        ~FileHandler() {
            std::cout << "file closed" << std::endl;
        }

};

int main()
{
    FileHandler("a.html");
}
