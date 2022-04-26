#include <ros/ros.h>
#include "kai_base.h"

int main(int argc, char** argv )
{
    ros::init(argc, argv, "kai_base_node");
    KaiBase kai;
    ros::spin();
    return 0;
}
