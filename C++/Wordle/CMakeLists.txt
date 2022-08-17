cmake_minimum_required(VERSION 3.21)
project(hw3)

set(CMAKE_CXX_STANDARD 11)

configure_file(files/wordList.txt files/wordList.txt COPYONLY)

add_executable(hw3 main.cpp)
