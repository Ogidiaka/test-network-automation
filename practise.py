#Here’s an example of a simple script to log in to a router (an example IP is 192.168.255.249 with a username and password of cisco)
from netmiko import ConnectHandler
device = ConnectHandler(device_type=’cisco_ios’, ip=’192.168.255.249′, username=’cisco’, password=’cisco’)
output = device.send_command(“show version”)
print (output)
device.disconnect()
