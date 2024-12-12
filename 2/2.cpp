#include "2.h"

#include <iostream>
#include <memory>
#include <vector>

#include "filing.h"

std::vector<int> get_numbers(std::string line) {
  std::vector<int> numbers;
  std::string_view view(line);

  size_t start = 0;
  for (size_t i = 0; i < view.length(); ++i) {
    char current_char = view[i];

    if (current_char == ' ') {
      numbers.push_back(std::stoi(std::string(view.substr(start, i))));
      start = i + 1;
    }
  }

  numbers.push_back(std::stoi(std::string(view.substr(start, view.length()))));

  return std::move(numbers);
}

bool same_sign(int n1, int n2) { return n1 * n2 >= 0; }

bool valid_range(int diff) { return abs(diff) <= 3 && abs(diff) >= 1; }

bool is_safe(std::vector<int> numbers) {
  int first_diff = numbers[1] - numbers[0];

  for (size_t i = 0; i < numbers.size() - 1; ++i) {
    int diff = numbers[i + 1] - numbers[i];

    if (!same_sign(first_diff, diff)) {
      return false;
    }

    if (!valid_range(diff)) {
      return false;
    }
  }

  return true;
}

void two_a() {
  std::ifstream file = getMainFile(2);

  int safe_lines = 0;
  std::string line;
  while (std::getline(file, line)) {
    std::vector<int> numbers = get_numbers(line);

    if (is_safe(numbers)) {
      safe_lines += 1;
    }
  }

  std::cout << safe_lines << "\n";
}

void two_b() {
  std::ifstream file = getMainFile(2);

  int safe_lines = 0;
  std::string line;
  while (std::getline(file, line)) {
    std::vector<int> numbers = get_numbers(line);

    if (is_safe(numbers)) {
      safe_lines += 1;
      continue;
    }

    for (size_t i = 0; i < numbers.size(); i++) {
      std::vector<int> sectioned_numbers;

      for (size_t j = 0; j < i; ++j) {
        sectioned_numbers.push_back(numbers[j]);
      }

      for (size_t j = i + 1; j < numbers.size(); ++j) {
        sectioned_numbers.push_back(numbers[j]);
      }

      if (is_safe(sectioned_numbers)) {
        safe_lines += 1;
        break;
      }
    }
  }

  std::cout << safe_lines << "\n";
}

void two() { two_b(); }