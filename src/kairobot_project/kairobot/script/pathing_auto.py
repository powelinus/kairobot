#!/usr/bin/python

from lxml import etree as ET
from lxml.builder import E
import io
import os
import subprocess
import signal
import serial
import ast
import shlex
import time
import roslaunch
import rospy
import sys
import pexpect
from ast import literal_eval
from subprocess import Popen, PIPE, STDOUT

ser = serial.Serial('/dev/usbttl', 115200, timeout=1)
ser.flush()

def name(v):
    return {'name': v}
def default(v):
    return {'default': v}
def value(v):
    return {'value': v}
def pkg(v):
    return {'pkg': v}
def type(v):
    return {'type': v}
def respawn(v):
    return {'respawn': v}
def output(v):
    return {'output': v}

fileloc = "/home/kai/catkin_ws/src/kairobot_project/kairobot/path/"
launchloc = "/home/kai/catkin_ws/src/kairobot_project/kairobot/launch/"

fd = open("/home/kai/catkin_ws/src/kairobot_project/kairobot/path/log.txt", "w+")
fd.write(str(" "))
fd.close() 

ser.write("Raspi initialized\n".encode('utf-8'))

print("Menunggu input serial...")

while True:
    time.sleep(1)
    print("Menunggu input serial...")
    # input ruangan dari serial
    if ser.in_waiting > 0:
        input_ruang = ser.readline().decode('utf-8').rstrip()
        print(input_ruang)
        print("input anda: " + str(input_ruang))

        # opsi untuk keluar aplikasi
        if input_ruang == "q":
            sys.exit()
        list_ruang = input_ruang.split(',')

        # tampilkan input yang diberikan
        ser.write(str(input_ruang) + "\n".encode('utf-8'))
        print(list_ruang)
        for sample in list_ruang:
            try:
                literal_eval(sample)
            except ValueError:
                print("Input yang diberikan salah, silahkan masukkan nomor dengan benar!")
                ser.write("Input salah\n".encode('utf-8'))
            else:
                ser.write("Input diterima\n".encode('utf-8'))
                # susun koordinat dari file
                listX = []
                listY = []
                listZ = []
                for ruang in list_ruang:
                    filex = fileloc + "Rx" + str(ruang) + ".txt"
                    filey = fileloc + "Ry" + str(ruang) + ".txt"
                    filez = fileloc + "Rz" + str(ruang) + ".txt"
                    fx = open(filex, "r")
                    sx = fx.read()
                    fx.close()
                    fy = open(filey, "r")
                    sy = fy.read()
                    fy.close()
                    fz = open(filez, "r")
                    sz = fz.read()
                    fz.close()
                    sx = ast.literal_eval(sx)
                    sy = ast.literal_eval(sy)
                    sz = ast.literal_eval(sz)
                    listX.extend(sx)
                    listY.extend(sy)
                    listZ.extend(sz)
                
                # bersihkan list tanpa kutip
                listX.append(0)
                listY.append(0)
                listZ.append(0)
                liX = []
                liY = []
                liZ = []
                for i in listX:
                    liX.append(float(i))
                for j in listY:
                    liY.append(float(j))
                for k in listZ:
                    liZ.append(float(k))
                
                # tampilkan koordinat yang akan dilalui
                totalist = len(listX)
                print("Koordinat yang akan dilalui:")
                print(liX)
                print(liY)
                print(liZ)
                print("Jumlah titik : " + str(totalist))

                # ubah ke string
                string_X = [str(int) for int in liX]
                str_of_x = ", ".join(string_X)
                koorX = "[" + str_of_x + "]"

                string_Y = [str(int) for int in liY]
                str_of_y = ", ".join(string_Y)
                koorY = "[" + str_of_y + "]"

                string_Z = [str(int) for int in liZ]
                str_of_z = ", ".join(string_Z)
                koorZ = "[" + str_of_z + "]"

                # buat file way_point.launch
                way_point = (
                    E.launch(
                        E.arg(name("sim_mode"), default("false")),
                        E.param(name("/use_sim_time"), value("$(arg sim_mode)")),
                        E.arg(name("loopTimes"), default("0")),
                        E.node(
                            E.param(name("goalListX"), value(koorX)),
                            E.param(name("goalListY"), value(koorY)),
                            E.param(name("goalListZ"), value(koorZ)),
                            E.param(name("loopTimes"), value("1")),
                            E.param(name("map_frame"), value("map")),
                            pkg("robot_navigation"), type("way_point.py"), respawn("false"), name("way_point"), output("screen")
                        )
                    )
                )

                # simpan file way_point.launch
                tree = ET.ElementTree(way_point)
                tree.write(launchloc + 'way_point.launch', pretty_print=True, xml_declaration=False,   encoding="utf-8")

                # jalankan node utama
                process1 = subprocess.Popen(["gnome-terminal", "--disable-factory", "-e", "roslaunch robot_navigation robot_navigation2.launch"], preexec_fn=os.setpgrp)
                print("base dijalankan")
                time.sleep(10)

                # jalankan way_point
                proc = subprocess.Popen(shlex.split("roslaunch robot_navigation way_point.launch"), stdout=subprocess.PIPE, preexec_fn=os.setsid)
                print("Executing path...")
                # print(proc.poll()) # output = none
                log_prev =0
                cahce_log = " "
                goalon = "Current Goal ID is: 1"
                goaloff = "Current Goal ID is: " + str(totalist)
                while True:
                    fp = open("/home/kai/catkin_ws/src/kairobot_project/kairobot/path/log.txt", "r")
                    sp = fp.read()
                    fp.close()
                    if "Finished" in sp:
                        fd = open("/home/kai/catkin_ws/src/kairobot_project/kairobot/path/log.txt", "w+")
                        fd.write(str(" "))
                        fd.close() 
                        break
                    elif cahce_log != sp:
                        print(sp)
                        ser.write(str(sp) + "\n".encode('utf-8'))
                        cahce_log = sp
                        if goalon in sp:
                            print("Neon dinyalakan")
                            ser.write("Neon=on\n".encode('utf-8'))
                        if goaloff in sp:
                            print("Neon dimatikan")
                            ser.write("Neon=off\n".encode('utf-8'))
                    time.sleep(1)
                proc.kill()
                proc.terminate()
                print("proses akan dimatikan")
                os.killpg(process1.pid, signal.SIGINT)
                print("app sudah berhasil diterminate")
                ser.write("Looping selesai\n".encode('utf-8'))

                # kosongkan variable
                input_ruang = None
                list_ruang = None
                ser.flush()

                # selesai pathing, kembali ke awal untuk terima input selanjutnya
            print("Menunggu input serial selanjutnya...")
        print(" ")


