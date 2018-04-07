"""
Cisco ZTP script through GuestShell
"""
import cli
import re

hostname = cli.execute('show version | i Processor board ID')
print(hostname)
filter = re.search("\w+$", hostname, flags=0)
print(filter.group(0))
hostname = "ztp-%s" % filter.group(0)
set_hostname = cli.configure('hostname %s' % hostname)
configuration = ['username user privilege 15 password 0 password',
                 'ip domain-name example.com',
                 'vtp mode transparent',
                 'line vty 0 4',
                 'login local',
                 ]
set_vty = cli.configure(configuration)
