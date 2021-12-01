//#pragma comment (lib, "user32.lib")

#include <string>
#include <iostream>
#include <filesystem>
#include <cstdlib>
#include <vector>
#include <string>
namespace fs = std::filesystem;

int main()
{
    std::string path = ".";
    std::vector<std::string> flist;

    for (const auto & entry : fs::directory_iterator(path))
    {
        std::cout <<  entry.path().c_str() << std::endl;
        auto x = entry.path().c_str();
    }
    std::system("notepad.exe a.cpp");
    return 0;
}