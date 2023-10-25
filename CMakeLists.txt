# Version requirement
cmake_minimum_required(VERSION 3.0)
set (CMAKE_CXX_STANDARD 20)

project(<proj_name>)

# dependencies
add_subdirectory("lib")

# code
add_subdirectory("src")