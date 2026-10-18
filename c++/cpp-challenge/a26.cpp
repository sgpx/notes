#include <iostream>
#include <vector>
#include <map>
#include <thread>
#include <mutex>
#include <cmath>
#include <chrono> // For timing
#include <random>

std::mutex mtx;
std::map<int, int> input_tasks;
std::map<int, int> results;

// Track how many tasks each thread handled
std::map<int, int> thread_load; 

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i <= std::sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int findLargestPrime(int n) {
    for (int i = n; i >= 2; --i) {
        if (isPrime(i)) return i;
    }
    return 0;
}

void processTasks(int threadID) {
    int tasksHandled = 0;

    while (true) {
        int currentN = -1;

        {
            // std::lock_guard automatically locks here...
            std::lock_guard<std::mutex> lock(mtx);
            if (input_tasks.empty()) break;

             auto it = input_tasks.begin();
            currentN = it->first;
            input_tasks.erase(it);
        } // ...and automatically unlocks here!

        int largestPrime = findLargestPrime(currentN);

        {
            std::lock_guard<std::mutex> lock(mtx);
            results[currentN] = largestPrime;
            tasksHandled++;
        }
    }

    // Record how much work this specific thread did
    std::lock_guard<std::mutex> lock(mtx);
    thread_load[threadID] = tasksHandled;
}

int main() {
    int N_threads = 4; // CONFIGURABLE: Change this to 1, 2, 8, etc.
    
    // Fill with 50 random numbers
    for (int i = 0; i < 50; ++i) {
        input_tasks[rand() % 10000 + 100] = 0; 
    }

    std::cout << "Starting " << N_threads << " threads...\n";
    
    // Start Timer
    auto start = std::chrono::high_resolution_clock::now();

    // Create a vector to hold our thread objects
    std::vector<std::thread> workers;
    for (int i = 0; i < N_threads; ++i) {
        workers.push_back(std::thread(processTasks, i));
    }

    // Join all threads
    for (auto& t : workers) {
        t.join();
    }

    // End Timer
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    // --- REPORT ---
    std::cout << "\n--- Load Distribution ---\n";
    for (auto const& [id, count] : thread_load) {
        std::cout << "Thread #" << id << " handled " << count << " numbers.\n";
    }

    std::cout << "\nTotal Time Taken: " << elapsed.count() << " seconds.\n";

    return 0;
}
