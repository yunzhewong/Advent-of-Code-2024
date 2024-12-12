#include "5.h"

#include <iostream>

#include "filing.h"

void five_a() {
  operate_on_lines(5, [](std::string line) { std::cout << line << "\n"; });
}

void five() { five_a(); };