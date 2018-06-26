# Cisco ZTP Underlay provision script

## Requirements
* Hosted Python Flask server with ZTP scripts  
-- http.py - main service for http  
-- ztp.py - python bootstrap config through GuestShell  
-- provision.py - function to wait for ZTP.  
-- ztpcli.py - post script config  

## Supported on Cisco IOS-XE 16.6+
## How to Configure the DHCP pool (on IOS-XE)
```
Device> enable
Device# configure terminal
Device(config)# ip dhcp pool pnp_device_pool
Device(config-dhcp)# network 10.1.1.0 255.255.255.0
Device(config-dhcp)# default-router 10.1.1.1 
Device(config-dhcp)# option 67 ascii http://198.51.100.1/http.py
Device(config-dhcp)# end
```
### For more examples
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/166/b_166_programmability_cg/zero_touch_provisioning.html
