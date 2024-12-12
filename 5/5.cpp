#include "5.h"

#include <algorithm>
#include <iostream>
#include <optional>
#include <sstream>
#include <unordered_map>
#include <vector>

#include "filing.h"
#include "utils.h"

struct Rule {
  int x;
  int y;
};

int toInt(std::string val) { return std::stoi(val); }

Rule parse_rule(std::string line) {
  std::vector<std::string> strings = utils::split(line, '|');
  std::vector<int> numbers = utils::map<std::string, int>(strings, toInt);
  return Rule{numbers[0], numbers[1]};
}

std::vector<int> parse_updates(std::string line) {
  std::vector<std::string> strings = utils::split(line, ',');
  std::vector<int> numbers = utils::map<std::string, int>(strings, toInt);
  return numbers;
}

struct FileInfo {
  std::unordered_map<int, std::vector<int>> rules;
  std::vector<std::vector<int>> all_updates;
};

FileInfo parse_file() {
  bool found_space = false;
  FileInfo info;

  operate_on_lines(5, [&](std::string line) {
    if (line == "") {
      found_space = true;
      return;
    }

    if (!found_space) {
      Rule rule = parse_rule(line);
      info.rules[rule.x].push_back(rule.y);
      return;
    }

    std::vector<int> updates = parse_updates(line);
    info.all_updates.push_back(updates);
  });

  return info;
}

std::optional<std::tuple<int, int>> get_invalidating_update(
    std::unordered_map<int, std::vector<int>> rules, std::vector<int> updates) {
  for (size_t i = 0; i < updates.size(); ++i) {
    int current_update = updates[i];

    std::vector<int> matching_rules = rules[current_update];

    for (size_t j = i + 1; j < updates.size(); ++j) {
      int later_update = updates[j];

      bool update_found = false;

      for (int rule : matching_rules) {
        if (rule == later_update) {
          update_found = true;
          break;
        }
      }

      if (!update_found) {
        return std::make_tuple(current_update, later_update);
      }
    }
  }
  return std::nullopt;
}

bool updates_valid(std::unordered_map<int, std::vector<int>> rules,
                   std::vector<int> updates) {
  auto invalidating_update = get_invalidating_update(rules, updates);
  return !invalidating_update.has_value();
}

int get_middle_value(std::vector<int> updates) {
  int middle_index = (int)((updates.size() - 1) / 2);
  return updates[middle_index];
}

void five_a() {
  FileInfo info = parse_file();
  int total = 0;

  for (std::vector<int> updates : info.all_updates) {
    if (!updates_valid(info.rules, updates)) {
      continue;
    }

    total += get_middle_value(updates);
  }

  std::cout << total << "\n";
}

int get_update_index(std::vector<int> updates, int update_value) {
  int update_index = -1;

  for (size_t i = 0; i < updates.size(); ++i) {
    if (updates[i] == update_value) {
      update_index = i;
      break;
    }
  }

  if (update_index == -1) {
    throw std::runtime_error("Expected to find later update");
  }

  return update_index;
}

std::vector<int> fix_incorrect_updates(
    std::unordered_map<int, std::vector<int>> rules, std::vector<int> updates) {
  while (true) {
    auto invalidating_update = get_invalidating_update(rules, updates);

    if (!invalidating_update.has_value()) {
      break;
    }

    auto [current_update, later_update] = invalidating_update.value();

    int later_update_index = get_update_index(updates, later_update);
    updates.erase(updates.begin() + later_update_index);
    int update_index = get_update_index(updates, current_update);
    updates.insert(updates.begin() + update_index, later_update);
  }

  return updates;
}

void five_b() {
  FileInfo info = parse_file();

  int total = 0;

  for (std::vector<int> updates : info.all_updates) {
    if (updates_valid(info.rules, updates)) {
      continue;
    }

    std::vector<int> correct_updates =
        fix_incorrect_updates(info.rules, updates);

    total += get_middle_value(correct_updates);
  }

  std::cout << total << "\n";
}

void five() { five_b(); };