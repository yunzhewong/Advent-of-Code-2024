#include <filing.h>

#include <fstream>
#include <functional>
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

void operate_on_file(std::ifstream& file, callbackOnFileLine fn) {
  std::string line;

  while (getline(file, line)) {
    fn(line);
  }
}

void operate_on_lines(int number, callbackOnFileLine fn) {
  std::ifstream file = getMainFile(number);
  operate_on_file(file, fn);
}

void operate_on_test(int number, callbackOnFileLine fn) {
  std::ifstream file = getTestFile(number);
  operate_on_file(file, fn);
}