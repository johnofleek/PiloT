#!/bin/env python2

# https://realpython.com/python-json/

import logging

#LOG_LEVEL = logging.INFO
LOG_LEVEL = logging.DEBUG
LOG_FILE = "/home/pi/Pilot/autoPilot/checkIp/mylogD"
#LOG_FILE = "/dev/stdout"
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)

import json

jsonFile = "/tmp/pilotManageDataConnection.json"

def readFromTmpJsonFile():
    dataR = {}
    try:
        with open(jsonFile, "r") as file_handle:
            dataR = json.load(file_handle)
    except:
        logging.error ("read temp json error")
        None

    return dataR



def writeToTmpJsonFile(dataToWrite):
    rc = -1
    try:
        with open(jsonFile, "w") as write_file:
            json.dump(dataToWrite, write_file)
            rc = 0
    except:
        logging.error("write temp json error")
        None
        
    return rc

def volatile_getValueBasedOnKey(key, defaultValue):
    volPilotDict = readFromTmpJsonFile()

    if key in volPilotDict.keys():
        logging.debug("volatile KVS found key: " + str(key) + "value: " + str(volPilotDict[key]))
    else:
        volPilotDict[key] = defaultValue
        logging.debug("volatile KVS no found key using default: " + str(key) + "value: " + str(volPilotDict[key]))
      
        writeToTmpJsonFile(volPilotDict) # save 
        
    return volPilotDict[key]

def volatile_setValueBasedOnKey(key, value):
    volPilotDict = readFromTmpJsonFile()

    volPilotDict[key] = value
    logging.debug("volatile write: " + str(key) + "value: " + str(volPilotDict[key]))
      
    writeToTmpJsonFile(volPilotDict) # save 
        



### test stuff
def test_TmpJsonReadWrite():
    dataR = readFromTmpJsonFile()  
    print ("temp json read data :" + str(dataR))

    dataW = {
                'state' : "power_up",
            }
    
    rc = writeToTmpJsonFile(dataW)
    logging.debug ("temp json write data response:" + str(rc))

    volatile_getValueBasedOnKey('testKey', 'testValue')
    volatile_getValueBasedOnKey('testKey', 'testValue1')
    volatile_setValueBasedOnKey('testKey', 'testValue2')
    volatile_getValueBasedOnKey('testKey', 'testValue3')

#test_TmpJsonReadWrite()




                