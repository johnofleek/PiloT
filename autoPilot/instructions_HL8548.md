


# Config

Minicom terminal to HL USB serial port
```
$ sudo minicom -D /dev/ttyACM3
```
Change factory default from 0 to 2
```
AT+KUSBCOMP=2
```
This gives 5 CDC-ACM serial ports and 1x CDC-ECM Network adapter





# Debug
```
$ lsusb
...
Bus 001 Device 010: ID 1519:0303 Comneon 
...
```
