"""
Configures devices through SSH from Python Service
"""

from netmiko import ConnectHandler


def postScript(device):
    """ Post Script after ZTP"""
    ztp_device = {
        "device_type": "cisco_ios",
        "ip": device,
        "username": "user",
        "password": "password",
        "port": 22,
        "verbose": False,
    }
    print("ssh device: %s" % device)
    net_connect = ConnectHandler(**ztp_device)
    config_commands = [
        "!",
        "int vlan1",
        "desc postScript",
        "!",
    ]
    output = net_connect.send_config_set(config_commands)
    # Remove if you don't want display output
    print(output)
    output = net_connect.disconnect()
