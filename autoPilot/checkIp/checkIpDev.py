#!/bin/env python2
'''
Todo:

Fix the absolute paths log and pilot scripts
'''


from subprocess import call
try:
    from subprocess import DEVNULL
except: # probably python <3.3
    import os
    DEVNULL = open(os.devnull,'w')


import logging

#LOG_LEVEL = logging.INFO
LOG_LEVEL = logging.DEBUG
LOG_FILE = "/home/pi/Pilot/autoPilot/checkIp/mylogD"
#LOG_FILE = "/dev/stdout"
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)

import myping
import pilotData

# fixed settings - could be driven from a JSON file or such
PING_TARGET_ADDRESS = "www.google.com"
PING_FAIL_RESTART_LIMIT = 5
PILOT_ON_SCRIPT  = "/home/pi/Pilot/autoPilot/pilotOn.sh"
PILOT_OFF_SCRIPT = "/home/pi/Pilot/autoPilot/pilotOff.sh"



def run_stateMachine() :
    state = pilotData.volatile_getValueBasedOnKey('state', 'system_power_up')

    logging.debug("run state : " + str(state))
    
    # main state machine
    if   (state == 'system_power_up'):
        pilotData.volatile_setValueBasedOnKey('state' , 'pilot_power_on')
        ## pilotOff
        rc = call(PILOT_OFF_SCRIPT, stdout=DEVNULL)
        logging.info("Pilot power off : " + str(rc))
        
    elif (state == 'pilot_power_on'):
        pilotData.volatile_setValueBasedOnKey('state' , 'pilot_ping_test')
        rc = call(PILOT_ON_SCRIPT, stdout=DEVNULL)
        logging.info("Pilot power on : " + str(rc))
        
    elif (state == 'pilot_ping_test'):    
        rc = myping.ping(ip = PING_TARGET_ADDRESS, timeout = '5' , interface = 'wwan0')
        logging.info(myping.printable_response(rc, PING_TARGET_ADDRESS))

        pingFailCount = 0
        
        if(rc != 0): # 0 means ping worked
            pingFailCountStr = pilotData.volatile_getValueBasedOnKey('pingFailCount','0')
            pingFailCount = int(pingFailCountStr) + 1
            logging.debug("ping fail")
        
        pingFailCountStr = str(pingFailCount)
        logging.info("ping fail count : " + pingFailCountStr)
            
        pilotData.volatile_setValueBasedOnKey('pingFailCount',pingFailCountStr)
        
        if ( pingFailCount > PING_FAIL_RESTART_LIMIT):
            pilotData.volatile_setValueBasedOnKey('state' , 'system_power_up')
                         
    else:
        pilotData.volatile_setValueBasedOnKey('state' , 'system_power_up')
        logging.error("something is wrong with state machine changing to system_power_up" )
        
        


    

run_stateMachine()

              