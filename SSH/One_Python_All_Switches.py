from netmiko import ConnectHandler

CORE_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.243',
    'username': 'cisco',
    'password': 'cisco',
}

CORE_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.244',
    'username': 'cisco',
    'password': 'cisco',
}

ACCESS_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.245',
    'username': 'cisco',
    'password': 'cisco',
}

ACCESS_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.246',
    'username': 'cisco',
    'password': 'cisco',
}

ACCESS_SW03 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.247',
    'username': 'cisco',
    'password': 'cisco',
}

with open('vlan_names') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01, CORE_SW02, ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('vtp_config') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01, CORE_SW02, ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('spanning_tree_Core01') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('spanning_tree_Core02') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('spanning_tree_Access') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('users_access_ports') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('core_trunk') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01, CORE_SW02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('access_trunk') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('core_port_channel') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01, CORE_SW02]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('dhcp_snooping') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [CORE_SW01, CORE_SW02, ACCESS_SW01, ACCESS_SW02, ACCESS_SW03]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


