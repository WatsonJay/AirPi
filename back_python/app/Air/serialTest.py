# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:07
# @Author  : Jaywatson
# @File    : serialTest.py
# @Soft    : back_python
import binascii

import serial
import struct
import time

ser = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(0.1)
ser.flush()

time.sleep(5)
count = ser.inWaiting()    # 获取还有多少字符未读
if count != 0:
    data = ser.read_all()    # 读取数据存到data中
    print(data)    # 打印接受到的数据
    print(binascii.b2a_hex(data))