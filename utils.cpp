#include "utils.h"

std::vector<std::string> utils::split(std::string& string, char character) {
  std::vector<std::string> output;

  size_t start = 0;

  for (int i = 0; i < string.length(); ++i) {
    char current_char = string[0];

    if (current_char == character) {
      output.push_back(string.substr(start, i - start));
      start = i + 1;
    }
  }

  output.push_back(string.substr(start, string.length() - start));

  return output;