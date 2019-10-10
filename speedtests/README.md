## Test methods

Originally I used speedtest.net in the RPi4 browser but will be switching
 to command line like this.

```
~/Pilot $ speedtest-cli
Retrieving speedtest.net configuration...
Testing from Three (94.196.182.81)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Redraw Internet (London) [2.56 km]: 64.756 ms
Testing download speed................................................................................
Download: 5.17 Mbit/s
Testing upload speed......................................................................................................
Upload: 2.09 Mbit/s
```

Install speedtest-cli
```
sudo apt install speedtest-cli
```

Note the speedtest-cli is written in Python so probably can be modified
 or repurposed for automated testing


## 02 PAYG SIM testing
With a new PAYG SIM the modem could not IP connect.  
After a £10 top up - still no connection  
After £20 the 5GB contracted started and it worked  
Disconnecting / reconnecting the antenna caused a massive 
 delay before the modem could reconnect
 
Using RPi4

Using Network manager / MBIM


### Windows - M.2 adapter - EM7455 - 02 PAYG
```
Desk main antenna only 
UP 20 Mbps
DOWN 20 MBPS
```

With a diversity (FLAT type) antenna and FLAT antenna
```
DOWN 	28.2 Mbps
UP 	20.0 Mbps
```

### Windows - Pilot - HL7692 - 02 PAYG
```
Flat antenna 
With modem forced to LTE only
DOWN 	11.0 Mbps
UP 	 4.6 Mbps
```

### RPi4 - Pilot - HL7692 - 02 PAYG
```
Flat antenna 
With modem forced to LTE only
DOWN 	9.02 Mbps
UP 	 4.7 Mbps
```

## Vodafone
```
Using RPi4
Using Network manager / MBIM
```

### RPi4 - Pilot - HL7692 - Vodafone PAYG
```
Flat antenna 
With modem LTE / 2G 
DOWN 	8.42 Mbps
UP 	4.65 Mbps
Ping 33ms
```

## Three
Using RPi4

### RPi4 -Pilot - HL8548 - Three PAYG - PPP via networkManager
```
Flat antenna
Connection via Network manager and PPP
3G
DOWN 	5.49 Mbps
UP 	3.74 Mbps
```
With cli
```
Testing from Three (94.196.182.81)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Redraw Internet (London) [2.56 km]: 64.719 ms
Testing download speed................................................................................
Download: 5.85 Mbit/s
Testing upload speed......................................................................................................
Upload: 2.02 Mbit/s
```

### RPi4 -Pilot - HL8548 - Three PAYG - manual connection
```
Flat antenna
Connection via AT+XCEDATA=1,0
3G
DOWN 	2.55 Mbps
UP 	1.61 Mbps
```

With cli
```
Testing from Three (92.40.45.114)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Redraw Internet (London) [2.56 km]: 68.998 ms
Testing download speed................................................................................
Download: 5.53 Mbit/s
Testing upload speed......................................................................................................
Upload: 2.05 Mbit/s
```

