cmake_minimum_required(VERSION 3.5.0)
project(AdventOfCode2024 VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(AdventOfCode2024 ./2/2.cpp filing.cpp main.cpp)
include_directories(include)

include(CTest)
enable_testing()

