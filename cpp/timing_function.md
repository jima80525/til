# Measuring the time a function call takes

Use the std::chrono library to measure the time between two points in code.

```cpp
#include <chrono>
using namespace std::chrono;

auto start = std::chrono::steady_clock::now();

//  test code here

auto stop = std::chrono::steady_clock::now();
auto duration = duration_cast<microseconds>(stop - start);
cerr << "Analytics frame time: " << duration.count() << endl;
```
