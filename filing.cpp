#include <fstream>
#include <iostream>
#include <string>

std::ifstream getFile(std::string name) {
  std::ifstream file(name);
  if (!file) {
    throw std::runtime_error("Failed to get file");
  }
  return file;
}

std::ifstream getMainFile(int number) {
  return getFile("../" + std::to_string(number) + "/input.txt");
}

std::ifstream getTestFile(int number) {
  return getFile("../" + std::to_string(number) + "/testinput.txt");
}