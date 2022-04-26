#! /usr/bin/env python

import time
import threading
import Tkinter as tk
import tkMessageBox as messagebox 
import rospy # the ROS api for python. We need it to create a node, 
             # a subscriber and access other ROS-specific program control
from nav_msgs.msg import Odometry # Python message class for Odometry

#inisialisasi data x,y,z
listX = []
listY = []
listZ = []

ruangan = 1
titik = 0

def getpose():
    rospy.init_node("extra_message_node")
    msg = rospy.wait_for_message("/odom", Odometry)

    # sumbu x
    x = msg.pose.pose.position.x
    x = '%.3f' % x
    # sumbu y
    y = msg.pose.pose.position.y
    y = '%.3f' % y
    # sumbu z (arah)
    z = msg.pose.pose.orientation.z
    z = '%.3f' % z

    return x, y, z

sx, sy, sz = getpose()

status = "X=" + str(sx) + ", Y=" + str(sy) + ", Z=" + str(sz)

def com1():
    global listX
    global listY
    global listZ
    global ruangan
    global titik
    rospy.init_node("extra_message_node")
    msg = rospy.wait_for_message("/odom", Odometry)

    # sumbu x
    x = msg.pose.pose.position.x
    x = '%.3f' % x
    x = x.replace("'", "")
    # sumbu y
    y = msg.pose.pose.position.y
    y = '%.3f' % y
    y = y.replace("'", "")
    # sumbu z (arah)
    z = msg.pose.pose.orientation.z
    z = '%.3f' % z
    z = z.replace("'", "")

    listX.append(x)
    listY.append(y)
    listZ.append(z)
    titik = titik + 1
    print("Koordinat yang akan dilalui:")
    print(listX)
    print(listY)
    print(listZ)
    print("Jumlah titik yang akan dilalui: " + str(titik))
    messagebox.showinfo('Koordinat Ditambahkan', "Jumlah titik pada rute ini: " + str(titik))
    
    

def com2():
    global listX
    global listY
    global listZ
    global ruangan
    global titik
    fileloc = "/home/kai/catkin_ws/src/kairobot_project/kairobot/path/" #diubah "/"
    ruangan = text1.get()
    filex = fileloc + "Rx" + str(ruangan) + ".txt"
    filey = fileloc + "Ry" + str(ruangan) + ".txt"
    filez = fileloc + "Rz" + str(ruangan) + ".txt"
    fx = open(filex, "w+")
    fx.write(str(listX))
    fx.close()
    fy = open(filey, "w+")
    fy.write(str(listY))
    fy.close()
    fz = open(filez, "w+")
    fz.write(str(listZ))
    fz.close()
    print("Ruangan " + ruangan)
    print("Berhasil Tersimpan!")
    print("di " + filex)
    messagebox.showinfo('Berhasil Tersimpan', "Silahkan petakan rute lain")
    # set koordinat kosong
    listX = []
    listY = []
    listZ = []
    titik = 0

def com3():
    global ruangan
    global titik
    ruangan = 1
    titik = 0
    messagebox.showinfo('Berhasil Terhapus', "Silahkan petakan ulang!")

def keluar():
    MsgBox = messagebox.askquestion ('Keluar Aplikasi','Apakah anda yakin ingin keluar aplikasi?',icon = 'warning')
    if MsgBox == 'yes':
        window.destroy()
        quit()

window = tk.Tk()
window.title("Aplikasi Penambah Koordinat")

screen_width = (window.winfo_screenwidth()//2)
screen_height = window.winfo_screenheight()

window.geometry("400x170+{0}+{1}".format(screen_width-200, screen_height-250))
window.attributes("-topmost", 1)
window.protocol("WM_DELETE_WINDOW", keluar)
window.resizable(False,False)

lb1 = tk.Label(window, 
                    text ='Ketik rute 1-9 lalu tekan tambah', 
                    anchor="c") 
lb1.place(height=20, width=300, x = 50, y = 10) 

lb2 = tk.Label(window, 
                    text ='Nomor Rute :', 
                    anchor="w") 
lb2.place(height=20, width=100, x = 50, y = 40) 

text1 = tk.Entry(window) 
text1.place(height=20, width=200, x = 150, y = 40) 

tb1 = tk.Button(window,
                   text="Tambah Koordinat",
                   command=com1)
tb1.place(height=30, width=140, x = 30, y = 70)

tb2 = tk.Button(window,
                   text="Simpan",
                   command=com2)
tb2.place(height=30, width=140, x = 230, y = 70)

tb3 = tk.Button(window,
                   text="Reset Pemetaan",
                   command=com3)
tb3.place(height=30, width=140, x = 30, y = 110)
tb4 = tk.Button(window,
                   text="Keluar",
                   fg="red",
                   command=keluar)
tb4.place(height=30, width=140, x = 230, y = 110)

window.mainloop()

