#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'willard.dennis@gmail.com'

import xmltodict


with open('junos-chassis.xml') as fd:
    mydict = xmltodict.parse(fd.read())

modnum = 0

print("Device model is: {}, serial number is: {}".format(
    mydict['rpc-reply']['chassis-inventory']['chassis']['description'],
    mydict['rpc-reply']['chassis-inventory']['chassis']['serial-number'])
)
print("\nModule list:")
for mod in mydict['rpc-reply']['chassis-inventory']['chassis']['chassis-module']:
    modnum += 1
    print("Module {}: {}, type {}".format(
        modnum,
        mod['name'],
        mod['description'])
    )
