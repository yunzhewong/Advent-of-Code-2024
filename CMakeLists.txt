cmake_minimum_required(VERSION 3.5.0)
project(main VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_BUILD_TYPE Release)

add_executable(main ./7/7.cpp filing.cpp utils.cpp main.cpp)
include_directories(include)

include(CTest)
enable_testing()

