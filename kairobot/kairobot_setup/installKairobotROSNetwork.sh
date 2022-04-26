#!/bin/bash
echo "export ROS_IP=\`hostname -I | awk '{print \$1}'\`" >> ~/.bashrc
echo "export ROS_HOSTNAME=\`hostname -I | awk '{print \$1}'\`" >> ~/.bashrc
echo "export ROS_MASTER_URI=http://\`hostname -I | awk '{print \$1}'\`:11311" >> ~/.bashrc
echo "export KAIBASE=2wd" >> ~/.bashrc
echo "export KAILIDAR=rplidar" >> ~/.bashrc
echo "export KAILIDAR=rplidar" >> ~/.bashrc
echo "export KAI_SERIAL=AEEFGABES63K6M2JXWMTA4VUBU======" >> ~/.bashrc

echo "Network setup done"
