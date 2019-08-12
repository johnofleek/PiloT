Disconnect
```
pi@raspberrypi:~ $ sudo tail -f /var/log/syslog
Aug 12 14:38:22 raspberrypi NetworkManager[394]: <info>  [1565617102.6322] manager: NetworkManager state is now CONNECTED_GLOBAL
Aug 12 14:38:22 raspberrypi systemd[1]: Starting Network Manager Script Dispatcher Service...
Aug 12 14:38:22 raspberrypi dbus-daemon[391]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Aug 12 14:38:22 raspberrypi systemd[1]: Started Network Manager Script Dispatcher Service.
Aug 12 14:38:22 raspberrypi nm-dispatcher: req:1 'up' [ppp0]: new request (1 scripts)
Aug 12 14:38:22 raspberrypi nm-dispatcher: req:1 'up' [ppp0]: start running ordered scripts...
Aug 12 14:38:22 raspberrypi nm-dispatcher: req:2 'connectivity-change': new request (1 scripts)
Aug 12 14:38:23 raspberrypi nm-dispatcher: req:2 'connectivity-change': start running ordered scripts...
Aug 12 14:38:33 raspberrypi systemd[1]: NetworkManager-dispatcher.service: Succeeded.
Aug 12 14:38:54 raspberrypi systemd-timesyncd[375]: Synchronized to time server for the first time 188.114.116.1:123 (0.debian.pool.ntp.org).
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.0795] device (ttyACM4): state change: activated -> deactivating (reason 'user-requested', sys-iface-state: 'managed')
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.0813] manager: NetworkManager state is now DISCONNECTING
Aug 12 14:43:39 raspberrypi dbus-daemon[391]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.8' (uid=0 pid=394 comm="/usr/sbin/NetworkManager --no-daemon ")
Aug 12 14:43:39 raspberrypi systemd[1]: Starting Network Manager Script Dispatcher Service...
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.1247] audit: op="device-disconnect" interface="ppp0" ifindex=11 pid=761 uid=1000 result="success"
Aug 12 14:43:39 raspberrypi NetworkManager[394]: Terminating on signal 15
Aug 12 14:43:39 raspberrypi pppd[2972]: Terminating on signal 15
Aug 12 14:43:39 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_phasechange): status 10 / phase 'terminate'
Aug 12 14:43:39 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_phasechange): status 8 / phase 'network'
Aug 12 14:43:39 raspberrypi ModemManager[403]: <info>  Modem /org/freedesktop/ModemManager1/Modem/3: state changed (connected -> disconnecting)
Aug 12 14:43:39 raspberrypi pppd[2972]: Connect time 5.3 minutes.
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.1361] modem["ttyACM4"]: modem state changed, 'connected' --> 'disconnecting' (reason: user-requested)
Aug 12 14:43:39 raspberrypi NetworkManager[394]: Connect time 5.3 minutes.
Aug 12 14:43:39 raspberrypi NetworkManager[394]: Sent 4953 bytes, received 2709 bytes.
Aug 12 14:43:39 raspberrypi pppd[2972]: Sent 4953 bytes, received 2709 bytes.
Aug 12 14:43:39 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_phasechange): status 5 / phase 'establish'
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.1424] device (ppp0): state change: disconnected -> unmanaged (reason 'connection-assumed', sys-iface-state: 'external')
Aug 12 14:43:39 raspberrypi NetworkManager[394]: <info>  [1565617419.1511] dns-mgr: Removing DNS information from /sbin/resolvconf
Aug 12 14:43:39 raspberrypi dbus-daemon[391]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Aug 12 14:43:39 raspberrypi systemd[1]: Started Network Manager Script Dispatcher Service.
Aug 12 14:43:39 raspberrypi nm-dispatcher: req:1 'connectivity-change': new request (1 scripts)
Aug 12 14:43:39 raspberrypi nm-dispatcher: req:1 'connectivity-change': start running ordered scripts...
Aug 12 14:43:39 raspberrypi pppd[2972]: Modem hangup
Aug 12 14:43:39 raspberrypi NetworkManager[394]: Modem hangup
Aug 12 14:43:39 raspberrypi NetworkManager[394]: Connection terminated.
Aug 12 14:43:39 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_phasechange): status 11 / phase 'disconnect'
Aug 12 14:43:39 raspberrypi pppd[2972]: Connection terminated.
Aug 12 14:43:40 raspberrypi ModemManager[403]: <info>  mobile equipment request to deactivate context (type IP, address 0.0.0.0, cid 2)
Aug 12 14:43:40 raspberrypi ModemManager[403]: <info>  Bearer /org/freedesktop/ModemManager1/Bearer/4: explicitly disconnected
Aug 12 14:43:40 raspberrypi ModemManager[403]: <warn>  (ttyACM4): could not re-acquire serial port lock: (5) Input/output error
Aug 12 14:43:40 raspberrypi ModemManager[403]: <info>  Modem /org/freedesktop/ModemManager1/Modem/3: state changed (disconnecting -> registered)
Aug 12 14:43:40 raspberrypi ModemManager[403]: <info>  mobile equipment request to deactivate context (type IP, address 0.0.0.0, cid 2)
Aug 12 14:43:40 raspberrypi NetworkManager[394]: Too few arguments.
Aug 12 14:43:40 raspberrypi NetworkManager[394]: Too few arguments.
Aug 12 14:43:40 raspberrypi NetworkManager[394]: <info>  [1565617420.2522] modem["ttyACM4"]: modem state changed, 'disconnecting' --> 'registered' (reason: user-requested)
Aug 12 14:43:40 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_phasechange): status 1 / phase 'dead'
Aug 12 14:43:40 raspberrypi pppd[2972]: nm-ppp-plugin: (nm_exit_notify): cleaning up
Aug 12 14:43:40 raspberrypi pppd[2972]: Exit.
Aug 12 14:43:41 raspberrypi ModemManager[403]: <info>  mobile equipment request to deactivate context (type IP, address 0.0.0.0, cid 2)
Aug 12 14:43:41 raspberrypi ModemManager[403]: <info>  mobile equipment request to deactivate context (type IP, address 0.0.0.0, cid 2)
Aug 12 14:43:42 raspberrypi NetworkManager[394]: <info>  [1565617422.1125] device (ttyACM4): state change: deactivating -> disconnected (reason 'user-requested', sys-iface-state: 'managed')
Aug 12 14:43:42 raspberrypi NetworkManager[394]: <info>  [1565617422.1230] manager: NetworkManager state is now DISCONNECTED
Aug 12 14:43:42 raspberrypi nm-dispatcher: req:2 'down' [ttyACM4]: new request (1 scripts)
Aug 12 14:43:42 raspberrypi nm-dispatcher: req:2 'down' [ttyACM4]: start running ordered scripts...
Aug 12 14:43:52 raspberrypi systemd[1]: NetworkManager-dispatcher.service: Succeeded.
Aug 12 14:44:09 raspberrypi dbus-daemon[663]: [session uid=1000 pid=663] Activating via systemd: service name='org.gtk.vfs.Metadata' unit='gvfs-metadata.service' requested by ':1.8' (uid=1000 pid=741 comm="pcmanfm --desktop --profile LXDE-pi ")
Aug 12 14:44:09 raspberrypi systemd[625]: Starting Virtual filesystem metadata service...
Aug 12 14:44:09 raspberrypi dbus-daemon[663]: [session uid=1000 pid=663] Successfully activated service 'org.gtk.vfs.Metadata'
Aug 12 14:44:09 raspberrypi systemd[625]: Started Virtual filesystem metadata service.
```

# connect
pi@raspberrypi:~ $ sudo tail -f /var/log/syslog

Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.1554] device (ttyACM4): Activation: starting connection '3 Internet' (f23612eb-7b35-4524-9e3d-67bc86003e04)
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.1576] audit: op="connection-activate" uuid="f23612eb-7b35-4524-9e3d-67bc86003e04" name="3 Internet" pid=761 uid=1000 result="success"
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.1594] device (ttyACM4): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.1658] manager: NetworkManager state is now CONNECTING
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect started...
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect state (4/8): Wait to get fully enabled
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect state (5/8): Register
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect state (6/8): Bearer
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect state (7/8): Connect
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Modem /org/freedesktop/ModemManager1/Modem/3: state changed (registered -> connecting)
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.1800] modem["ttyACM4"]: modem state changed, 'registered' --> 'connecting' (reason: user-requested)
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Modem /org/freedesktop/ModemManager1/Modem/3: state changed (connecting -> connected)
Aug 12 14:55:58 raspberrypi ModemManager[403]: <info>  Simple connect state (8/8): All done
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2225] modem["ttyACM4"]: modem state changed, 'connecting' --> 'connected' (reason: user-requested)
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2267] device (ttyACM4): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2301] device (ttyACM4): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <warn>  [1565618158.2350] device (ttyACM4): interface ttyACM4 not up for IP configuration
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2359] modem["ttyACM4"]: using modem-specified IP timeout: 20 seconds
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2376] ppp-manager: starting PPP connection
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2428] ppp-manager: pppd started with pid 3307
Aug 12 14:55:58 raspberrypi pppd[3307]: Plugin /usr/lib/pppd/2.4.7/nm-pppd-plugin.so loaded.
Aug 12 14:55:58 raspberrypi NetworkManager[394]: Plugin /usr/lib/pppd/2.4.7/nm-pppd-plugin.so loaded.
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (plugin_init): initializing
Aug 12 14:55:58 raspberrypi pppd[3307]: pppd 2.4.7 started by root, uid 0
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_phasechange): status 3 / phase 'serial connection'
Aug 12 14:55:58 raspberrypi pppd[3307]: Using interface ppp0
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_phasechange): status 5 / phase 'establish'
Aug 12 14:55:58 raspberrypi NetworkManager[394]: Using interface ppp0
Aug 12 14:55:58 raspberrypi NetworkManager[394]: Connect: ppp0 <--> /dev/ttyACM4
Aug 12 14:55:58 raspberrypi pppd[3307]: Connect: ppp0 <--> /dev/ttyACM4
Aug 12 14:55:58 raspberrypi NetworkManager[394]: <info>  [1565618158.2740] manager: (ppp0): new Ppp device (/org/freedesktop/NetworkManager/Devices/16)
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_phasechange): status 6 / phase 'authenticate'
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (get_credentials): passwd-hook, requesting credentials...
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (get_credentials): got credentials from NetworkManager
Aug 12 14:55:58 raspberrypi pppd[3307]: CHAP authentication succeeded: Welcome!
Aug 12 14:55:58 raspberrypi NetworkManager[394]: CHAP authentication succeeded: Welcome!
Aug 12 14:55:58 raspberrypi NetworkManager[394]: CHAP authentication succeeded
Aug 12 14:55:58 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_phasechange): status 8 / phase 'network'
Aug 12 14:55:58 raspberrypi pppd[3307]: CHAP authentication succeeded
Aug 12 14:56:01 raspberrypi pppd[3307]: local  IP address 94.197.91.52
Aug 12 14:56:01 raspberrypi NetworkManager[394]: local  IP address 94.197.91.52
Aug 12 14:56:01 raspberrypi NetworkManager[394]: remote IP address 192.200.1.21
Aug 12 14:56:01 raspberrypi NetworkManager[394]: primary   DNS address 217.171.132.0
Aug 12 14:56:01 raspberrypi NetworkManager[394]: secondary DNS address 217.171.135.0
Aug 12 14:56:01 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_phasechange): status 9 / phase 'running'
Aug 12 14:56:01 raspberrypi pppd[3307]: remote IP address 192.200.1.21
Aug 12 14:56:01 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_ip_up): ip-up event
Aug 12 14:56:01 raspberrypi pppd[3307]: primary   DNS address 217.171.132.0
Aug 12 14:56:01 raspberrypi pppd[3307]: nm-ppp-plugin: (nm_ip_up): sending IPv4 config to NetworkManager...
Aug 12 14:56:01 raspberrypi pppd[3307]: secondary DNS address 217.171.135.0
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3567] device (ppp0): state change: unmanaged -> unavailable (reason 'connection-assumed', sys-iface-state: 'external')
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3625] ppp-manager: (IPv4 Config Get) reply received.
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3741] device (ttyACM4): state change: ip-config -> ip-check (reason 'none', sys-iface-state: 'managed')
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3828] device (ppp0): state change: unavailable -> disconnected (reason 'none', sys-iface-state: 'external')
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3889] device (ttyACM4): state change: ip-check -> secondaries (reason 'none', sys-iface-state: 'managed')
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3921] device (ttyACM4): state change: secondaries -> activated (reason 'none', sys-iface-state: 'managed')
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.3967] manager: NetworkManager state is now CONNECTED_LOCAL
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.4147] manager: NetworkManager state is now CONNECTED_SITE
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.4151] policy: set '3 Internet' (ppp0) as default for IPv4 routing and DNS
Aug 12 14:56:01 raspberrypi NetworkManager[394]: <info>  [1565618161.4156] dns-mgr: Writing DNS information to /sbin/resolvconf
Aug 12 14:56:02 raspberrypi NetworkManager[394]: <info>  [1565618162.4982] device (ttyACM4): Activation: successful, device activated.
Aug 12 14:56:02 raspberrypi NetworkManager[394]: <info>  [1565618162.5006] manager: NetworkManager state is now CONNECTED_GLOBAL
Aug 12 14:56:02 raspberrypi dbus-daemon[391]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.8' (uid=0 pid=394 comm="/usr/sbin/NetworkManager --no-daemon ")
Aug 12 14:56:02 raspberrypi systemd[1]: Starting Network Manager Script Dispatcher Service...
Aug 12 14:56:02 raspberrypi dbus-daemon[391]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Aug 12 14:56:02 raspberrypi systemd[1]: Started Network Manager Script Dispatcher Service.
Aug 12 14:56:02 raspberrypi nm-dispatcher: req:1 'up' [ppp0]: new request (1 scripts)
Aug 12 14:56:02 raspberrypi nm-dispatcher: req:1 'up' [ppp0]: start running ordered scripts...
Aug 12 14:56:02 raspberrypi nm-dispatcher: req:2 'connectivity-change': new request (1 scripts)
Aug 12 14:56:03 raspberrypi nm-dispatcher: req:2 'connectivity-change': start running ordered scripts...
