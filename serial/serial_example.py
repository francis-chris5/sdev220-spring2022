# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:40:39 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

## usb plug and play devices or bluetooth or anything on a serial port
import serial
import time


## SERIAL( com-port, baud-rate, ... )
ser = serial.Serial("COM3", "115200", timeout=1)
time.sleep(3)



def getRotary():
    ser.write(b"SPIN")
    res = int(ser.readline())
    return res


def getClick():
    ser.write(b"TAP")
    res = int(ser.readline())
    return res


def getBoth():
    ser.write(b"CHECK")
    res = ser.readline()
    return res






def close():
    ##remember to disconnect when finished
    ser.close()
    




