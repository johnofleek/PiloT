
This is a system which is connected to the network  

Command

```
$ nmcli c show 'O2 Pay and Go (Prepaid)' > file.txt
```

```
connection.id:                          O2 Pay and Go (Prepaid)
connection.uuid:                        e79ee73b-84c1-48b0-b81e-9e0b08a548b5
connection.stable-id:                   --
connection.type:                        gsm
connection.interface-name:              --
connection.autoconnect:                 no
connection.autoconnect-priority:        0
connection.autoconnect-retries:         -1 (default)
connection.multi-connect:               0 (default)
connection.auth-retries:                -1
connection.timestamp:                   1568211779
connection.read-only:                   no
connection.permissions:                 user:pi
connection.zone:                        --
connection.master:                      --
connection.slave-type:                  --
connection.autoconnect-slaves:          -1 (default)
connection.secondaries:                 --
connection.gateway-ping-timeout:        0
connection.metered:                     unknown
connection.lldp:                        default
connection.mdns:                        -1 (default)
connection.llmnr:                       -1 (default)
ipv4.method:                            auto
ipv4.dns:                               --
ipv4.dns-search:                        --
ipv4.dns-options:                       ""
ipv4.dns-priority:                      0
ipv4.addresses:                         --
ipv4.gateway:                           --
ipv4.routes:                            --
ipv4.route-metric:                      -1
ipv4.route-table:                       0 (unspec)
ipv4.ignore-auto-routes:                no
ipv4.ignore-auto-dns:                   no
ipv4.dhcp-client-id:                    --
ipv4.dhcp-timeout:                      0 (default)
ipv4.dhcp-send-hostname:                yes
ipv4.dhcp-hostname:                     --
ipv4.dhcp-fqdn:                         --
ipv4.never-default:                     no
ipv4.may-fail:                          yes
ipv4.dad-timeout:                       -1 (default)
ipv6.method:                            auto
ipv6.dns:                               --
ipv6.dns-search:                        --
ipv6.dns-options:                       ""
ipv6.dns-priority:                      0
ipv6.addresses:                         --
ipv6.gateway:                           --
ipv6.routes:                            --
ipv6.route-metric:                      -1
ipv6.route-table:                       0 (unspec)
ipv6.ignore-auto-routes:                no
ipv6.ignore-auto-dns:                   no
ipv6.never-default:                     no
ipv6.may-fail:                          yes
ipv6.ip6-privacy:                       0 (disabled)
ipv6.addr-gen-mode:                     stable-privacy
ipv6.dhcp-duid:                         --
ipv6.dhcp-send-hostname:                yes
ipv6.dhcp-hostname:                     --
ipv6.token:                             --
ppp.noauth:                             yes
ppp.refuse-eap:                         yes
ppp.refuse-pap:                         no
ppp.refuse-chap:                        yes
ppp.refuse-mschap:                      yes
ppp.refuse-mschapv2:                    yes
ppp.nobsdcomp:                          no
ppp.nodeflate:                          no
ppp.no-vj-comp:                         no
ppp.require-mppe:                       no
ppp.require-mppe-128:                   no
ppp.mppe-stateful:                      no
ppp.crtscts:                            no
ppp.baud:                               0
ppp.mru:                                0
ppp.mtu:                                auto
ppp.lcp-echo-failure:                   0
ppp.lcp-echo-interval:                  0
gsm.number:                             --
gsm.username:                           payandgo
gsm.password:                           <hidden>
gsm.password-flags:                     1 (agent-owned)
gsm.apn:                                --
gsm.network-id:                         --
gsm.pin:                                <hidden>
gsm.pin-flags:                          0 (none)
gsm.home-only:                          no
gsm.device-id:                          --
gsm.sim-id:                             --
gsm.sim-operator-id:                    --
gsm.mtu:                                auto
proxy.method:                           none
proxy.browser-only:                     no
proxy.pac-url:                          --
proxy.pac-script:                       --
GENERAL.NAME:                           O2 Pay and Go (Prepaid)
GENERAL.UUID:                           e79ee73b-84c1-48b0-b81e-9e0b08a548b5
GENERAL.DEVICES:                        cdc-wdm0
GENERAL.STATE:                          activated
GENERAL.DEFAULT:                        yes
GENERAL.DEFAULT6:                       no
GENERAL.SPEC-OBJECT:                    --
GENERAL.VPN:                            no
GENERAL.DBUS-PATH:                      /org/freedesktop/NetworkManager/ActiveConnection/8
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/Settings/3
GENERAL.ZONE:                           --
GENERAL.MASTER-PATH:                    --
IP4.ADDRESS[1]:                         10.161.89.159/24
IP4.GATEWAY:                            10.161.89.1
IP4.ROUTE[1]:                           dst = 10.161.89.0/24, nh = 0.0.0.0, mt = 700
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 10.161.89.1, mt = 700
IP4.DNS[1]:                             82.132.254.2
IP4.DNS[2]:                             82.132.254.3
IP6.ADDRESS[1]:                         fe80::e0d5:4635:f0d6:8985/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 700
IP6.ROUTE[2]:                           dst = ff00::/8, nh = ::, mt = 256, table=255
```

and tested HL7692 modem information
```
mmcli -m 5
  --------------------------
  General  |      dbus path: /org/freedesktop/ModemManager1/Modem/5
           |      device id: af0ec9dc872ff41c5a2941691c19ab814317106f
  --------------------------
  Hardware |   manufacturer: Generic
           |          model: MBIM [8087:0911]
           |       revision: M2M_7160_MBIM_CAT1_WW_01.1804.
           |   h/w revision: XMM7160_V1.2_MBIM_NAND_REV_4.5
           |      supported: gsm-umts, lte
           |        current: gsm-umts, lte
           |   equipment id: 355465070064353
  --------------------------
  System   |         device: /sys/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1
           |        drivers: cdc_acm, cdc_mbim
           |         plugin: Generic
           |   primary port: cdc-wdm0
           |          ports: cdc-wdm0 (mbim), wwan0 (net), ttyACM0 (at)
  --------------------------
  Status   | unlock retries: sim-pin2 (3)
           |          state: connected
           |    power state: on
           |    access tech: lte
           | signal quality: 58% (recent)
  --------------------------
  Modes    |      supported: allowed: 2g, 3g, 4g; preferred: none
           |        current: allowed: 2g, 3g, 4g; preferred: none
  --------------------------
  IP       |      supported: ipv4, ipv6, ipv4v6
  --------------------------
  3GPP     |           imei: 355465070064353
           |  enabled locks: fixed-dialing
           |    operator id: 23410
           |  operator name: O2 - UK
           |   registration: home
  --------------------------
  SIM      |      dbus path: /org/freedesktop/ModemManager1/SIM/4
  --------------------------
  Bearer   |      dbus path: /org/freedesktop/ModemManager1/Bearer/7
```
