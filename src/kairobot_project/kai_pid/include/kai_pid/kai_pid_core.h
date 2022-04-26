#ifndef SR_KAI_PID_CORE_H
#define SR_KAI_PID_CORE_H

#include "ros/ros.h"
#include "ros/time.h"

// Custom message includes. Auto-generated from msg/ directory.
#include "kai_msgs/PID.h"

// Dynamic reconfigure includes.
#include <dynamic_reconfigure/server.h>
// Auto-generated from cfg/ directory.
#include <kai_pid/kaiPIDConfig.h>

class KaiPID
{
public:
  KaiPID();
  ~KaiPID();
  void configCallback(kai_pid::kaiPIDConfig &config, double level);
  void publishMessage(ros::Publisher *pub_message);
  void messageCallback(const kai_msgs::PID::ConstPtr &msg);

  double p_;
  double d_;
  double i_;

};
#endif
