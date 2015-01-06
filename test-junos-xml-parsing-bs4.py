#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'willard.dennis@gmail.com'

from bs4 import BeautifulSoup as Soup
# also need the 'lxml' module installed on system to use the 'xml' kw in BeautifulSoup


with open('junos-chassis.xml') as fd:
    cmdout = fd.read()

modnum = 0

soup = Soup(cmdout, 'xml')
#print(soup.prettify())

for chassis_info in soup.find_all('chassis'):
    print("Device model is: {}, serial number is: {}".format(
        chassis_info.find('description').text,
        chassis_info.find('serial-number').text)
    )
print("\nModule list:")
for mod in soup.find_all('chassis-module'):
    modnum += 1
    print("Module {}: {}, type {}".format(
        modnum,
        mod.find('name').text,
        mod.find('description').text)
    )
