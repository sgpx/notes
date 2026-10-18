
/*

Problem:
Create a base class Shape with a virtual method area().
Then, create two derived classes: Circle and Rectangle, each implementing area() differently.
Use virtual functions for polymorphism.
Use a pointer to base class (Shape*) to store derived objects and call area().

*/

#include <cmath>
#include <iostream>

class Shape
{
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape
{
public:
    double r;
    Circle(double r1) : r(r1) {};
    virtual double area() const
    {

        return M_PI * r * r;
    }
};

class Rectangle : public Shape
{
public:
    double l, w;
    Rectangle(double l1, double w1) : l(l1), w(w1)
    {
    }
    virtual double area() const
    {
        return l * w;
    }
};

int main()
{
    Shape *r = new Rectangle(5, 6);
    Shape *c = new Circle(3);
    std::cout << r->area() << std::endl;
    std::cout << c->area() << std::endl;

    delete r;
    delete c;
}