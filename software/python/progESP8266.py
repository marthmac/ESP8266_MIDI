import sys; sys.dont_write_bytecode = True
import time
import serial
import argparse

from os import listdir

import pyConfig
from ESP8266_utils import *


parser = argparse.ArgumentParser(description='Programs ESP8266 over USB->Serial')
parser.add_argument('type', metavar='T', type=str, nargs='+', help='m = Master, s = Slave')
args = parser.parse_args()

if args.type[0] == 'm':
    luaPath = pyConfig.luaPath_master
elif args.type[0] == 's':
    luaPath = pyConfig.luaPath_slave

ser = serial.Serial(
    port = pyConfig.serialPort,
    baudrate = pyConfig.serialBaudRate,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout = pyConfig.serialTimeout
    )

ser.close()
time.sleep(10/1000)
ser.open()

luaFiles = listdir(luaPath)

clearESP8266( ser, 1 )

for luaFile in luaFiles:
    if luaFile != "init.lua":
        writeFileToESP8266( ser, luaPath, luaFile, 1)

if "init.lua" in luaFiles:
    writeFileToESP8266( ser, luaPath, "init.lua", 1)

[files, numFiles] = listAllFilesOnESP8266( ser, 1 )

resetESP8266( ser, 1 )

ser.close()
