cmake_minimum_required(VERSION 3.5.1)
project(ai_cpp VERSION 1.0.0)


##################
## Dependencies ##
##################

set(PYTHON_REQUIRED_VERSION 3 CACHE STRING "Python version for bindings")

find_package(PythonInterp 3 REQUIRED)
string(REPLACE "." "" PYTHON_VERSION_STRING_COMPACT "${PYTHON_VERSION_STRING}")


# libboost-python1.65-dev
find_package(PythonLibs ${PYTHON_VERSION_STRING} EXACT REQUIRED)
find_library(BoostPython NAMES boost_python-py${PYTHON_VERSION_STRING_COMPACT} boost_python${PYTHON_VERSION_STRING_COMPACT})

if (BoostPython STREQUAL "BoostPython-NOTFOUND")
    message(SEND_ERROR "Could not find one of those libraries: boost_python-py${PYTHON_VERSION_STRING_COMPACT} boost_python${PYTHON_VERSION_STRING_COMPACT}")
endif()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall -Wextra")

###########
## Build ##
###########

include_directories(include)
include_directories(SYSTEM ${Boost_INCLUDE_DIRS})
include_directories(SYSTEM ${PYTHON_INCLUDE_DIRS})

file(GLOB_RECURSE HEADERS
    include/*.h
)

file(GLOB_RECURSE SOURCES
    src/*.cpp
)

add_library(${PROJECT_NAME} SHARED ${SOURCES} ${HEADERS})
set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".so")
target_link_libraries(${PROJECT_NAME}
    LINK_PUBLIC
    ${PYTHON_LIBRARIES}
    ${Boost_LIBRARIES}
    ${BoostPython}
    LINK_PRIVATE
)

