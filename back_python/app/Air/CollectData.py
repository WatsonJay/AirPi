# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 10:36
# @Author  : Jaywatson
# @File    : CollectDate.py
# @Soft    : back_python
import random
import time
from datetime import datetime
import logging
import serial

from models.EnvData import EnvData
from libs import db
from util.sql_factory import BaseSql

def collect():
    recv_bytes = __readSerial__()
    results = __dealData__(recv_bytes)
    with db.app.app_context():
        sql = BaseSql(EnvData)
        sql.insert([{
            'creatTime': datetime.now(),
            'hcho': results['hcho'],
            'tvoc': results['tvoc'],
            'co2': results['co2'],
            'pm25': results['pm25'],
            'pm10': results['pm10'],
            'temp': results['temp'],
            'hum': results['hum']
        }])
        print("----------------test------------------")

def __readSerial__():
    ser = serial.Serial("/dev/ttyUSB0", 9600)
    time.sleep(0.1)
    ser.flush()

    count = 0
    while count < 64:
        # 必要的软件延迟。否则刚打开串口设备数据还没进来，ser.inWaiting()为空。设备每0.2-0.8s传一次32字节结果数据，
        # 可以在ser = serial.Serial("/dev/ttyUSB0", 9600)后给time.sleep(2)然后再ser.read()，也可以while True循环read()部分，
        # sleep(1)能接受到1-2次数据集，再根据flag字节截取一次的32字节结果
        time.sleep(0.2)
        # 缓冲区已收到的数据字节个数
        count = ser.inWaiting()
        # print(count)

    # 读取数据
    try:
        recv_bytes = ser.read(count)  # 缓冲区的数据全部取出，可能包含多次数据
        return recv_bytes
    except serial.SerialException as e:
        logging.error(e)
    finally:
        ser.close()

def __dealData__(recv_bytes):
    recv_bytes_arr = bytearray(recv_bytes)  # 字节转字节数组才能操作

    BYTE_LENGTH = ''
    byte_flag_1 = False
    byte_flag_2 = False

    recv_decimal = []

    for i, byte in enumerate(recv_bytes_arr):
        """ 遍历从缓冲区取到的全部数据 根据起始字节flag取一次结果数据，丢弃其余字节数据。缩短time.sleep可以获得更频繁的数据
            转成16进制放入recv_hex
            2字节起始符+2字节帧长度+13组*2字节数据+2字节校验=32
        """
        if byte_flag_1 is False:
            # debug时字节显示是10进制数字，print（byte）时控制台输出显示是按照ascii和16进制编出来的字符（这里略歧义）。字节本质是二进制数字，所以先处理成16进制为了后面处理。
            # hex()返回类型字符串。二进制>16进制>编码字符。数字到字符为编码，字符到数字为解码，说白了是数字到信息的映射关系。
            if hex(byte) == '0x3c':  # 起始字节1  BYTE_FLAG_1为true时 continue到下一次循环，下一次的hex（byte）预计等于BYTE_FLAG_2
                byte_flag_1 = True
                recv_decimal.append(int(byte))
                continue
            else:
                continue

        if byte_flag_2 is False:  # 起始字节2
            if hex(byte) == '0x2':
                byte_flag_2 = True
                recv_decimal.append(int(byte))
                continue
            else:
                byte_flag_1 = False  # 如果不等于BYTE_FLAG_2，说明前一次的BYTE_FLAG_1是数据位恰好相等 并不是起始符1
                continue

        if byte_flag_2 is True:  # 起始2字节 帧长度2字节值应该为28 固定所以写死，有校验不怕出问题。所以除了起始2字节，向后取30字节
            recv_decimal.append(int(byte))
            if i == 16:
                break

        # print('recv_decimal', recv_decimal, len(recv_decimal))

    # 校验。校验码=起始符1+起始符2+……..+数据13低八位 前面30个字节的和
    check_code = recv_decimal[-1]  # <<8相当于*256 移位运算符优先级低注意括号 校验位高低各8位两字节
    bytes_sum = sum(recv for recv in recv_decimal[0:-1])  # 除校验位其它30字节累加

    if check_code == bytes_sum % 256:
        pass
    else:
        logging.error('校验失败,数据存在异常')

    results = dict()
    results["co2"] = recv_decimal[2] * 256 + recv_decimal[3]
    results["hcho"] = recv_decimal[4] * 256 + recv_decimal[5]
    results["tvoc"] = recv_decimal[6] * 256 + recv_decimal[7]
    results["pm25"] = recv_decimal[8] * 256 + recv_decimal[9]
    results["pm10"] = recv_decimal[10] * 256 + recv_decimal[11]
    results["temp"] = float(str(recv_decimal[12]) + '.' + str(recv_decimal[13]))
    results["hum"] = float(str(recv_decimal[14]) + '.' + str(recv_decimal[15]))

    return results


