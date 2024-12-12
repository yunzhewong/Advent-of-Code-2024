#include "3.h"

#include <iostream>
#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "filing.h"

const size_t START_LENGTH = std::string("mul(").length();
const size_t MAX_LENGTH = std::string("mul(123,123)").length();

bool section_length_valid(std::string_view section) {
  size_t length = section.length();
  return length <= 3 && length >= 1;
}

std::optional<int> get_value(std::string_view view) {
  if (std::string(view.substr(0, START_LENGTH)) != "mul(") {
    return std::nullopt;
  }

  std::string_view numerical_section =
      view.substr(START_LENGTH, MAX_LENGTH - START_LENGTH);
  std::vector<int> numbers;
  size_t start = 0;

  for (size_t i = 0; i < numerical_section.length(); ++i) {
    char current_char = numerical_section[i];

    if (current_char == ',') {
      std::string_view section = numerical_section.substr(start, i - start);
      if (!section_length_valid(section) || numbers.size() != 0) {
        return std::nullopt;
      }
      numbers.push_back(std::stoi(std::string(section)));
      start = i + 1;
    } else if (current_char == ')') {
      std::string_view section = numerical_section.substr(start, i - start);

      if (!section_length_valid(section) || numbers.size() != 1) {
        return std::nullopt;
      }
      numbers.push_back(std::stoi(std::string(section)));
      break;
    } else {
      if (!std::isdigit(current_char)) {
        return std::nullopt;
      }
    }
  }

  if (numbers.size() != 2) {
    return std::nullopt;
  }

  return numbers[0] * numbers[1];
}

void three_a() {
  std::ifstream file = getMainFile(3);

  int sum = 0;
  std::string line;
  while (std::getline(file, line)) {
    std::string_view view(line);

    for (size_t i = 0; i < view.length(); ++i) {
      if (line[i] == 'm') {
        auto result = get_value(view.substr(i, MAX_LENGTH));
        if (result.has_value()) {
          sum += result.value();
        }
      }
    }
  }

  std::cout << sum << "\n";
}

const std::string do_string = std::string("do()");
const std::string dont_string = std::string("don't()");

std::optional<bool> change_state(std::string_view view) {
  if (std::string(view.substr(0, do_string.length())) == do_string) {
    return true;
  }

  if (std::string(view.substr(0, dont_string.length())) == dont_string) {
    return false;
  }

  return std::nullopt;
}

void three_b() {
  std::ifstream file = getMainFile(3);

  int sum = 0;
  bool enabled = true;
  std::string line;
  while (std::getline(file, line)) {
    std::string_view view(line);

    for (size_t i = 0; i < view.length(); ++i) {
      if (line[i] == 'm') {
        if (!enabled) {
          continue;
        }

        auto result = get_value(view.substr(i, MAX_LENGTH));
        if (result.has_value()) {
          sum += result.value();
        }
      }

      if (line[i] == 'd') {
        auto result = change_state(view.substr(i, dont_string.length()));

        if (result.has_value()) {
          enabled = result.value();
        }
      }
    }
  }

  std::cout << sum << "\n";
}

void three() { three_b(); }