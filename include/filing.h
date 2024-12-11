#pragma once

#include <fstream>
#include <string>

std::ifstream getFile(std::string name);
std::ifstream getMainFile(int number);
std::ifstream getTestFile(int number);