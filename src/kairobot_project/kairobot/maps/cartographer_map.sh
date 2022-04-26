rm -rf /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/house.pgm 
rm -rf /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/house.yaml

rosservice call /write_state /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/map.bag.pbstream

rosrun cartographer_ros cartographer_pbstream_to_ros_map -pbstream_filename=/home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/map.bag.pbstream


cp  /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/map.pgm /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/house.pgm

cp  /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/map.yaml /home/kairobot/catkin_ws/src/kairobot_project/kairobot/maps/house.yaml

