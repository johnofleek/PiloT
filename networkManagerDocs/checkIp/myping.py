from subprocess import call
try:
    from subprocess import DEVNULL
except: # probably python <3.3
    import os
    DEVNULL = open(os.devnull,'w')
    
def ping(ip , count = 1 , interface = 'default' , timeout = 'default'):
    rc = -1
    countStr = str(count)
    pingList = ['ping','-c',countStr,ip]
    
    if (interface != 'default'):
        pingList = pingList + ['-I' , interface] 

    if (timeout != 'default'):
        '''
        Specify a timeout, in seconds, before ping exits regardless of how many packets
        have been sent or received.
        In this case, ping does not stop after count packet are sent,
        it waits either for deadline to expire or until count probes are answered or
        for some error notification from network.
        '''

        pingList = pingList + ['-w' , timeout]

    # print pingList
    rc = call(pingList, stdout=DEVNULL)
        
    return(rc)

def print_response(rc, ip):
    if rc == 0:
        print('ping %s active' % ip)
    elif rc == 2:
        print('ping %s no response' % ip)
    else:
        print('ping %s error %d' % (ip,rc))    

def printable_response(rc, ip):
    strRc = ""
    if rc == 0:
        strRc = 'ping %s active' % ip
    elif rc == 2:
        strRc = 'ping %s no response' % ip
    else:
        strRc = 'ping %s error %d' % (ip,rc)
    return strRc

def test(comment, interface ="eth0",ip = '8.8.8.8', count = 3 ):
    print (comment)
    print ("ip + defaults")
    print_response( ping(ip), ip)
    
    print ("ip + count test")
    print_response( ping(ip,count), ip)
    
    print ("non working ip + timeout")
    ip="1.8.1.8"
    print_response( ping(ip = ip, timeout='4'), ip)
    
    print ("URL + timeout + interface non default")
    ip="www.bbc.co.uk"
    print_response( ping(ip=ip, interface=interface, timeout='4') , ip)

# test("Test default interface ")
# test("Test alternative interface mixed with default", interface="wlan0")

    
