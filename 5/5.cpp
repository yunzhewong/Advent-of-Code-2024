#include "5.h"

#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

#include "filing.h"
#include "utils.h"

struct Rule {
  int x;
  int y;
};

Rule parse_rule(std::string line) {
  std::vector<std::string> strings = utils::split(line, ' ');
  std::vector<int> numbers;

  for (std::string s : strings) {
    numbers.push_back(std::stoi(s));
  }

  return Rule{numbers[0], numbers[1]};
}

void five_a() {
  int total = 0;
  std::unordered_map<int, std::vector<int>> rules;

  operate_on_lines(5, [&](std::string line) {
    std::cout << line << "\n";
    total += 1;
  });
  std::cout << total << "\n";
}

void five() { five_a(); };