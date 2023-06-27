# Version reequirement
# cmake_minimum_required(VERSION 3.10)

set (CMAKE_CXX_STANDARD 17)


project(<proj_name>)

# include 3rd party libs
# add_subdirectory("lib/<dependency_name>")

# target_link_libraries(<proj_name> PRIVATE <dependency_name>)

# own source files
set( SRC_BACKEND
	# src/main.cpp
)

add_executable(<proj_name> ${SRC_BACKEND})

