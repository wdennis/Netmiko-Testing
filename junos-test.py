#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'willard.dennis@gmail.com'

import netmiko


juniper_ex2200 = {
    'device_type': 'juniper',
    'ip': '192.168.1.2',
    'username': 'netadmin',
    'password': 'B1g53cr37',
    'secret': '',
    'verbose': False,
}


SSHClass = netmiko.ssh_dispatcher(device_type=juniper_ex2200['device_type'])
device_conn = SSHClass(**juniper_ex2200)
output = device_conn.send_command('show chassis hardware | display xml')

fd = open('junos-chassis.xml', 'w')
fd.write(output.strip())
fd.close()
