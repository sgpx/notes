# 📅 Week 2: C++ Advanced Concepts (Medium - Hard)
In Week 2, we’ll tackle **inheritance**, **polymorphism**, **STL algorithms**, and **more advanced C++ features**.


## Task 2 — STL Algorithms: `std::sort` and `std::find`
**Problem:**  
Create a vector of integers.  
- **Sort** it using `std::sort`.
- **Find** a specific element using `std::find`.

- Bonus: **Reverse** the vector using `std::reverse`.

---

## Task 3 — Constructor Overloading & Initializer Lists  
**Problem:**  
Create a class `Person` that has two constructors:
1. A default constructor.
2. A constructor that takes a name and age, using an initializer list.

- Print the person's name and age after construction.

```cpp
class Person {
    std::string name;
    int age;

public:
    Person() : name("Unknown"), age(0) {}
    Person(std::string name, int age) : name(name), age(age) {}

    void printInfo() const {
        std::cout << name << ", " << age << " years old\n";
    }
};
```

---

## Task 4 — Lambda Functions & `std::for_each`  
**Problem:**  
Create a vector of integers and use **lambda functions** inside `std::for_each` to square all the elements.

Example:
```cpp
std::for_each(v.begin(), v.end(), [](int& n) { n *= n; });
```

---

## Task 5 — Move Semantics & `std::move`  
**Problem:**  
Create a class `StringWrapper` that wraps around `std::string`.  
Implement a **move constructor** and **move assignment operator**.

```cpp
StringWrapper(StringWrapper&& other) noexcept : str(std::move(other.str)) {}
StringWrapper& operator=(StringWrapper&& other) noexcept {
    str = std::move(other.str);
    return *this;
}
```

# 📅 Week 1 C++ Tasks

## Task 1 — Smart Pointer Warm-up
**Problem:**  
Write a simple `Point` class (with `x` and `y` coordinates) and manage a `Point` instance using `std::unique_ptr`.  
- Create the `Point` dynamically.
- Print its coordinates.
- No manual `delete`.

✅ Focus: Constructors, `unique_ptr`, `operator->`.

---

## Task 2 — Vector of Objects
**Problem:**  
Create a `std::vector` that stores multiple `Point` objects (from Task 1).  
- Fill it with 5 points (use a loop).
- Write a function that prints all points.

✅ Focus: `std::vector`, range-for loops, passing by reference.

---

## Task 3 — Copy vs Move
**Problem:**  
Create a `StringHolder` class that owns a `std::string`.  
- Implement a **copy constructor** and a **move constructor** manually.
- Print when copy/move happens.

```cpp
StringHolder(const StringHolder& other);
StringHolder(StringHolder&& other);
```

- Write a function that takes a `StringHolder` **by value** and observe copy/move calls.

✅ Focus: Copy/move semantics, `std::move`.

---

## Task 4 — Simple Resource Manager (RAII)
**Problem:**  
Simulate managing a file resource:  
- Write a class `FileHandler` that "opens" a file on construction (simulate with `std::cout`) and "closes" it on destruction.
- No explicit `close()` calls — use RAII.

Example output:
```
Opening file mydata.txt
File mydata.txt closed
```

✅ Focus: RAII (Resource Acquisition Is Initialization).

---

## Task 5 — Templates Basic
**Problem:**  
Write a **generic function** `add()` that adds two values of any type (int, float, double).

Example usage:
```cpp
auto sum1 = add(3, 4);      // int
auto sum2 = add(2.5, 3.7);  // double
```

✅ Focus: function templates.

---

## (Optional) Mini Bonus Challenge — Debug Printer
**Problem:**  
Create a variadic template function `debug()` that prints all its arguments, separated by commas.

Example:
```cpp
debug(1, "hello", 3.14);
// Output: 1, hello, 3.14
```

✅ Focus: Variadic templates (if you want extra challenge).

---

# 🎯 Goals for Week 1
- Understand constructors, destructors, and memory ownership.
- Use `unique_ptr`, `vector`, move semantics naturally.
- Write small classes and functions confidently.
- Get hands-on muscle memory.

---
