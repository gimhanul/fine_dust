import os
import fcntl
from app import db
from ..domain.fineDust import FineDust

#미세먼지 값 받기
I2C_SLAVE = 0x703
PM2008 = 0x28

fd = os.open('/dev/i2c-1',os.O_RDWR)
if fd < 0 :
    print("Failed to open the i2c bus\n")
io = fcntl.ioctl(fd,I2C_SLAVE,PM2008)
if io < 0 :
    print("Failed to acquire bus access/or talk to salve\n")

def getAndSaveNowFineDust():
    data = os.read(fd,32)
    now = FineDust(256*int(data[11])+int(data[12]))
    db.session.add(now)
    db.session.commit()

def getFineDustAll():
    return FineDust.query.all()

def getLatestFineDust():
    data = getFineDustAll()
    return data[-1]

def getFineDustByMinute():
    data = getFineDustAll()
    return data[-6:]

def getFineDustByHour():
    data = getFineDustAll()
    return

def getFineDustByDay():
    return

def getFineDustByMonth():
    return

def getFineDustByYear():
    return