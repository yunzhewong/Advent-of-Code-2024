#include "4.h"

#include <functional>
#include <iostream>
#include <string>
#include <vector>

#include "filing.h"

class StringGrid {
 private:
  std::vector<std::string> m_storage;

 public:
  StringGrid() {
    std::ifstream file = getMainFile(4);

    std::string line;
    while (std::getline(file, line)) {
      m_storage.push_back(std::move(line));
    }
  }

  size_t get_height() { return m_storage.size(); }
  size_t get_width() { return m_storage[0].length(); }

  char get(int i, int j) {
    int height = static_cast<int>(get_height());
    int width = static_cast<int>(get_width());

    if (i >= height || i < 0) {
      return ' ';
    }

    if (j >= width || j < 0) {
      return ' ';
    }

    return m_storage[i][j];
  }

  bool check_for_xmas(int i, int j, std::function<std::tuple<int, int>()> fn) {
    auto [v, h] = fn();

    if (get(i, j) != 'X') {
      return false;
    }

    if (get(i + v, j + h) != 'M') {
      return false;
    }

    if (get(i + 2 * v, j + 2 * h) != 'A') {
      return false;
    }

    if (get(i + 3 * v, j + 3 * h) != 'S') {
      return false;
    }

    return true;
  }

  void print() {
    for (std::string s : m_storage) {
      std::cout << s << "\n";
    }
  }
};

std::tuple<int, int> move_vertical(int direction) {
  return std::make_tuple(direction, 0);
}

std::tuple<int, int> move_horizontal(int direction) {
  return std::make_tuple(0, direction);
}

std::tuple<int, int> move_diagonal_1(int direction) {
  return std::make_tuple(direction, direction);
}

std::tuple<int, int> move_diagonal_2(int direction) {
  return std::make_tuple(direction, -direction);
}

void four_a() {
  StringGrid grid;
  size_t height = grid.get_height();
  size_t width = grid.get_width();

  int xmases = 0;
  for (size_t i = 0; i < height; ++i) {
    for (size_t j = 0; j < width; ++j) {
      int v = static_cast<int>(i);
      int h = static_cast<int>(j);

      if (grid.get(v, h) != 'X') {
        continue;
      }

      if (grid.check_for_xmas(v, h, []() { return move_vertical(1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_vertical(-1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_horizontal(1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_horizontal(-1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_diagonal_1(1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_diagonal_1(-1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_diagonal_2(1); })) {
        xmases += 1;
      }
      if (grid.check_for_xmas(v, h, []() { return move_diagonal_2(-1); })) {
        xmases += 1;
      }
    }
  }

  std::cout << xmases << "\n";
}

void four() { four_a(); }
