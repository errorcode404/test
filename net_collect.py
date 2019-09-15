#-*- coding:utf-8 -*-

import os, sys, platform, socket


os_data_0 = str(sys.getwindowsversion())
os_data_1 = "OS Version : " + str(platform.platform())
os_data_2 = "Bulid Version : "+ str(platform.version())
os_data_3 = "Host name : " + str(socket.gethostname())
if os.name == "nt":
    local_net_data = os.popen("ipconfig/all").read()
else:
    local_net_data = os.popen("ifconfig").read()
route_data = os.popen("netstat -r").read()
net_data = os.popen("netstat -abn").read()

f = open("C:"+str(os.getenv("homepath"))+"\\Desktop\\info.txt", mode="w", encoding="utf-8", buffering=50)

f.write("===========================   OS  INFO   ======================================\n")
f.write(os_data_0 + "\n"+ os_data_1 + "\n"+ os_data_2 + "\n"+ os_data_3)
f.write("\n===========================   IP  DATA   ======================================\n")
f.write(local_net_data)
f.write("\n===========================   NET DATA   ======================================\n")
f.write(net_data)
f.write("\n===========================   NET DATA   ======================================\n")
f.write(route_data)

f.close()


