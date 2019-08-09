root@raspberrypi:/etc/NetworkManager# cat system-connections/'3 Internet.nmconnection'
[connection]
id=3 Internet
uuid=c7a7a320-b996-4bfe-8ae9-8c776bb89126
type=gsm
autoconnect=false
permissions=user:pi:;

[gsm]
apn=3internet
number=*99#
password-flags=1

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto
