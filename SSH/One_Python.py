from netmiko import ConnectHandler

iosv_l2_CORE_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.243',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_CORE_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.244',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_ACCESS_SW01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.245',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_ACCESS_SW02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.246',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_ACCESS_SW03 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.86.247',
    'username': 'cisco',
    'password': 'cisco',
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_ACCESS_SW03, iosv_l2_ACCESS_SW02, iosv_l2_ACCESS_SW01]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
