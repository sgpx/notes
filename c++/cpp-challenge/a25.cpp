#include <iostream>
#include <vector>
#include <map>
#include <thread>
#include <mutex>
#include <cmath>
#include <algorithm>

std::mutex mtx;
std::map<int, int> input_tasks;
std::map<int, int> results;

// Helper: Check if a number is prime
bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

// Helper: Find largest prime <= N
int findLargestPrime(int n) {
    for (int i = n; i >= 2; --i) {
        if (isPrime(i)) return i;
    }
    return 0; // No prime found
}

void processTasks() {
    while (true) {
        int currentN = -1;

        // CRITICAL SECTION: Accessing the input map
        mtx.lock();
        if (!input_tasks.empty()) {
            auto it = input_tasks.begin();
            currentN = it->first;
            input_tasks.erase(it); // Take the task out of the "to-do" pile
        }
        mtx.unlock();

        if (currentN == -1) break; // No more tasks left!

        // HEAVY LIFTING: Done outside the lock so other threads can work
        int largestPrime = findLargestPrime(currentN);

        // CRITICAL SECTION: Saving the result
        mtx.lock();
        results[currentN] = largestPrime;
        mtx.unlock();
    }
}

int main() {
    // 1. Fill input map with 50 random numbers (e.g., between 100 and 1000)
    for (int i = 0; i < 50; ++i) {
        input_tasks[rand() % 900 + 100] = 0; 
    }

    // 2. Launch 2 threads
    std::thread t1(processTasks);
    std::thread t2(processTasks);

    // 3. Wait for them to finish
    t1.join();
    t2.join();

    // 4. Print results
    std::cout << "Results { N : Largest Prime <= N }\n";
    for (auto const& [n, p] : results) {
        std::cout << n << " : " << p << "\n";
    }

    return 0;
}
