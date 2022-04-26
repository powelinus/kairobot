cmake_minimum_required(VERSION 2.8.3)
project(kairobot)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  rosserial_python
  sensor_msgs
  kai_msgs
  std_msgs
  tf
  serial
)
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES kairobot
  CATKIN_DEPENDS roscpp rospy tf nav_msgs kai_msgs geometry_msgs sensor_msgs std_msgs 
  DEPENDS system_lib serial
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

###############################
INCLUDE_DIRECTORIES(/usr/local/lib)
LINK_DIRECTORIES(/usr/local/lib)
 
add_executable(send_goals src/send_goals.cpp)
target_link_libraries(send_goals ${catkin_LIBRARIES})
################################


add_library(kai_base src/kai_base.cpp)
add_executable(kai_base_node src/kai_base_node.cpp)
target_link_libraries(kai_base_node kai_base ${catkin_LIBRARIES})


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(serial_example_node src/serial_example_node.cpp)

target_link_libraries(serial_example_node
  ${catkin_LIBRARIES}
)

