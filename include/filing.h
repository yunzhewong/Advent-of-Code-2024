#pragma once

#include <fstream>
#include <functional>
#include <string>

typedef std::function<void(std::string)> callbackOnFileLine;

std::ifstream getFile(std::string name);
std::ifstream getMainFile(int number);
std::ifstream getTestFile(int number);

void operate_on_lines(int number, callbackOnFileLine fn);
void operate_on_lines(int number, callbackOnFileLine fn);