#include "5.h"

#include <algorithm>
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

int toInt(std::string val) { return std::stoi(val); }

Rule parse_rule(std::string line) {
  std::vector<std::string> strings = utils::split(line, '|');
  std::vector<int> numbers = utils::map<std::string, int>(strings, toInt);

  return Rule{numbers[0], numbers[1]};
}

std::vector<int> parse_updates(std::string line) {}

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
  });
  std::cout << total << "\n";
}
// state = State()

//     all_updates = []

//                   def
//                   fn(line
//                      : str)
//     : if line == "" : state.found_space = True return

//                                           if not state.found_space : x,
// y = parse_rule(line)

//     arr = state.rules.get(x, []) arr.append(y) state.rules[x] = arr return

//     updates = parse_updates(line) all_updates
//                   .append(updates)

//                       operate_on_lines(fn)

//                           return state.rules,
// all_updates
}

void five_a() {}

void five() { five_a(); };