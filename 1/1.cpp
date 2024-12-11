#include "1.h"

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

const int SPACE_WIDTH = 3;

void one() {
  std::ifstream file("../1/testinput.txt");

  if (!file) {
    throw std::runtime_error("Failed to get file");
  }

  std::vector<int> list1 = {};
  std::vector<int> list2 = {};

  std::string line;
  while (std::getline(file, line)) {
    size_t total_length = line.length();
    size_t number_size = (total_length - SPACE_WIDTH) / 2;

    int first_num = std::stoi(line.substr(0, number_size));
    int second_num =
        std::stoi(line.substr(number_size + SPACE_WIDTH, line.length()));

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

  file.close();
}