# Cisco ZTP Underlay provision script

## Requirements
* Hosted Python Flask server with ZTP scripts  
-- main.py - main service for http  
-- ztp.py - python bootstrap config through GuestShell  
-- provision.py - function to wait for ZTP.  
-- ztpcli.py - post script config  

## Installation
* Python 3.6+
  * Download Source Code
```
git clone -b https://github.com/robertcsapo/cisco-pnp-ztp-guestshell.git
```
  * Install python modules and start application
```
cd cisco-pnp-ztp-guestshell
pip install -r requirements.txt
python main.py
```
  * Application running
```
Serving Flask app "main" (lazy loading)
Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
Debug mode: off
Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
```

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

Cisco IOS-XE 17.2  
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/zero_touch_provisioning.html  
Cisco IOS-XE 16.6  
https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/166/b_166_programmability_cg/zero_touch_provisioning.html  
