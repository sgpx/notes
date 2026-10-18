/*

Task 1 — Smart Pointer Warm-up

Problem:
Write a simple Point class (with x and y coordinates) and manage a Point instance using std::unique_ptr.

    Create the Point dynamically.
    Print its coordinates.
    No manual delete.

✅ Focus: Constructors, unique_ptr, operator->.

*/

#include <iostream>
#include <memory>

class Point {
	public:
		int x;
		int y;

		Point(int x1, int y1) {
			x = x1;
			y = y1;			
			std::cout << "Created" << std::endl ; 
		}

		~Point() {
			std::cout << "Destroyed" << std::endl ;
		}
};

int main() {
        std::unique_ptr<int> ptr = std::make_unique<int>(10);
        std::cout << "Value: " << *ptr << std::endl ;

        std::unique_ptr<Point> mypoint = std::make_unique<Point>(3,4);
        std::cout << mypoint->x << ", " << mypoint->y << std::endl ;
}
