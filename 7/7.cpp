#include "7.h"

#include <iostream>

#include "filing.h"
#include "utils.h"

enum Operator {
  Add = 0,
  Multiply,
  Concatenate,
};

using number = long long;

std::tuple<number, std::vector<number>> split_line(std::string line) {
  std::vector<std::string> sections = utils::split(line, ':');

  number total = std::stoll(sections[0]);

  std::vector<std::string> remaining = utils::split(sections[1], ' ');

  std::vector<number> numbers;
  numbers.reserve(remaining.size() - 1);

  for (size_t i = 1; i < remaining.size(); i++) {
    numbers.push_back(std::stoi(remaining[i]));
  }

  return std::make_tuple(total, numbers);
}

class Signs {
 private:
  std::vector<int> m_data;
  size_t m_count;

 public:
  Signs(size_t count) {
    m_data.reserve(count);
    for (size_t i = 0; i < count; ++i) {
      m_data.push_back(Operator::Add);
    }
    m_count = count;
  }

  const int& operator[](size_t index) const { return m_data[index]; }

  size_t size() const { return m_data.size(); }

  void increment(int operator_options) {
    m_data[m_count - 1] += 1;

    for (size_t i = m_count - 1; i > 0; i--) {
      if (m_data[i] == operator_options) {
        m_data[i] = 0;
        m_data[i - 1] += 1;
      }
    }
  }
};

number evaluate_option(const std::vector<number>& numbers, const Signs& signs,
                       number target) {
  number total = numbers[0];

  for (size_t i = 0; i < signs.size(); ++i) {
    if (total > target) {
      return 0;
    }

    const int& sign = signs[i];

    const number& next = numbers[i + 1];

    if (sign == Operator::Multiply) {
      total *= next;
    } else if (sign == Operator::Add) {
      total += next;
    } else if (sign == Operator::Concatenate) {
      total = std::stoll(std::to_string(total) + std::to_string(next));
    }
  }

  return total;
}

bool numbers_meet_total(std::vector<number> numbers, number total,
                        int operator_options) {
  size_t number_of_signs = numbers.size() - 1;
  Signs signs(number_of_signs);

  size_t methods =
      static_cast<size_t>(std::pow(operator_options, number_of_signs));

  for (size_t i = 0; i < methods; ++i) {
    if (evaluate_option(numbers, signs, total) == total) {
      return true;
    }

    signs.increment(operator_options);
  }

  return false;
}

void seven_a() {
  number sum = 0;

  operate_on_lines(7, [&](std::string line) {
    auto [total, numbers] = split_line(line);
    if (numbers_meet_total(numbers, total, 2)) {
      sum += total;
    }
  });

  std::cout << sum << "\n";
}

void seven_b() {
  number sum = 0;
  number line_number = 0;

  operate_on_lines(7, [&](std::string line) {
    auto [total, numbers] = split_line(line);
    if (numbers_meet_total(numbers, total, 3)) {
      sum += total;
    }
    line_number++;
    std::cout << line_number << "\n";
  });

  std::cout << sum << "\n";
}
void seven() { seven_b(); }