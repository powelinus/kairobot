#!/usr/bin/python

from lxml import etree as ET
from lxml.builder import E
import io
import os
import signal
import serial
import ast
import shlex
import subprocess
import time
import roslaunch
import rospy
import sys


while True:
    # input ruangan dengan keyboard
    # if ser.in_waiting > 0:
    #    line = ser.readline().decode('utf-8').rstrip()
    input_name=None
    input_name=raw_input("Input nama Map: ")
    #ok = line
    #input_ruang=ser.readline().decode('utf-8').rstrip() #("Input ruangan yang akan dilalui (pisahkan dengan koma): ")
    print("input anda: " + str(input_name))

    # jalankan node utama
    #pros1 = subprocess.Popen(["gnome-terminal", "--disable-factory", "-e", "roscd kairobot/maps&& rosrun map_server map_saver -f okokkk"], preexec_fn=os.setpgrp)
    print("buka folder map")
    pros1 = os.system ("cd ~/catkin_ws/src/kairobot_project/kairobot/maps&& rosrun map_server map_saver -f " + str(input_name))
    time.sleep(1)
    # jalankan way_point
    #proc = subprocess.Popen(shlex.split("rosrun map_server map_saver -f" + str(input_name)), stdout=subprocess.PIPE, preexec_fn=os.setsid)
    #time.sleep(5)
    print("map Disimpan")
    #proc.kill()
    #proc.terminate()
    print("proses akan dimatikan")
    os.killpg(pros1.pid, signal.SIGINT)
    break
