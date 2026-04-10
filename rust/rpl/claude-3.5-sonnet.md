Day 1: Advanced Ownership and Borrowing
Difficulty: Intermediate

Concepts:
- Lifetime annotations
- Shared and mutable references
- Move semantics
- Ownership in closures

Challenge:
Implement a function that takes two string slices and returns the longer one. Use lifetime annotations to make it work.

Day 2: Advanced Traits and Generics
Difficulty: Intermediate to Advanced

Concepts:
- Trait objects
- Associated types
- Generic type parameters
- Trait bounds

Challenge:
Create a generic `Container` trait with an associated type and implement it for `Vec` and `HashMap`.

Day 3: Concurrency and Parallelism
Difficulty: Advanced

Concepts:
- Threads
- Message passing
- Shared state concurrency
- Atomic types
- Mutexes and RwLocks

Challenge:
Implement a parallel merge sort algorithm using threads.

Day 4: Error Handling and Result Combinators
Difficulty: Intermediate

Concepts:
- Custom error types
- `?` operator
- `map`, `and_then`, `or_else` methods on Result
- Error propagation

Challenge:
Create a function that reads a file, parses it as JSON, and returns a specific field. Use proper error handling and combinators.

Day 5: Advanced Pattern Matching and Macros
Difficulty: Advanced

Concepts:
- Complex pattern matching
- Destructuring
- Macro rules and expansion
- Procedural macros (brief introduction)

Challenge:
Create a macro that generates a struct with getter and setter methods for each field.

Day 6: Unsafe Rust and FFI
Difficulty: Very Advanced

Concepts:
- Unsafe blocks
- Raw pointers
- Calling C functions from Rust
- Creating a safe abstraction over unsafe code

Challenge:
Write a safe wrapper for a C library function that manipulates a raw pointer.

Day 7: Advanced Asynchronous Programming
Difficulty: Very Advanced

Concepts:
- Futures
- Async/await syntax
- Tokio runtime
- Asynchronous streams

Challenge:
Implement an asynchronous web scraper that fetches and processes multiple pages concurrently using tokio.