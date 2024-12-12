#include "utils.h"

std::vector<std::string> utils::split(std::string& string, char character) {
  std::vector<std::string> output;

  size_t start = 0;

  for (size_t i = 0; i < string.length(); ++i) {
    char current_char = string[i];

    if (current_char == character) {
      output.push_back(string.substr(start, i - start));
      start = i + 1;
    }
  }

  output.push_back(string.substr(start, string.length() - start));

  return output;
}