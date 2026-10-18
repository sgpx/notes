/*

Task 2 — Vector of Objects

Problem:
Create a std::vector that stores multiple Point objects (from Task 1).

    Fill it with 5 points (use a loop).
    Write a function that prints all points.


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
#include <vector>

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
	std::vector<Point> myvec;

	for(int i = 0; i < 5 ; i++) {
	myvec.push_back(Point(3*i,4*i));	
	}

}
