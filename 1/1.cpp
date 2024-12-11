#include "1.h"

#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "filing.h"

const int FILE_NUMBER = 1;
const int SPACE_WIDTH = 3;

std::tuple<int, int> destructureLine(std::string line) {
  size_t total_length = line.length();
  size_t number_size = (total_length - SPACE_WIDTH) / 2;

  int first_num = std::stoi(line.substr(0, number_size));
  int second_num =
      std::stoi(line.substr(number_size + SPACE_WIDTH, line.length()));

  return std::make_tuple(first_num, second_num);
}

void one_b() {
  std::ifstream file = getMainFile(FILE_NUMBER);
  std::unordered_map<int, int> counts;

  std::vector<int> similarityItems;

  std::string line;
  while (std::getline(file, line)) {
    auto [first_num, second_num] = destructureLine(line);
    similarityItems.push_back(first_num);
    counts[second_num] += 1;
  }

  int total = 0;
  for (size_t i = 0; i < similarityItems.size(); ++i) {
    int item = similarityItems[i];
    total += item * counts[item];
  }

  std::cout << total << "\n";
}

void one_a() {
  std::ifstream file = getMainFile(FILE_NUMBER);
  std::vector<int> list1 = {};
  std::vector<int> list2 = {};

  std::string line;
  while (std::getline(file, line)) {
    auto [first_num, second_num] = destructureLine(line);

    list1.push_back(first_num);
    list2.push_back(second_num);
  }

  std::sort(list1.begin(), list1.end());
  std::sort(list2.begin(), list2.end());

  int sum = 0;

  for (size_t i = 0; i < list1.size(); ++i) {
    if (list1[i] < list2[i]) {
      sum += list2[i] - list1[i];
    } else {
      sum += list1[i] - list2[i];
    }
  }

  std::cout << sum << "\n";
}

void one() { one_b(); }
