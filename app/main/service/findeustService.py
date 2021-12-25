from app import db
from ..domain.fineDust import FineDust

def getAllFineDust():
    return FineDust.query.all()

def getFineDustByMinute():
    data = getAllFineDust()
    return data[-6:]

def getFineDustByHour():
    return

def getFineDustByDay():
    return

def getFineDustByMonth():
    return

def getFineDustByYear():
    return