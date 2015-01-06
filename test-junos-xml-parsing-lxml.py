#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'willard.dennis@gmail.com'

from lxml import etree


modnum = 0

xmldoc = etree.parse('junos-chassis.xml')
docroot = xmldoc.getroot()

for ele in docroot.iter('{*}chassis'):
    print("Device model is: {}, serial number is: {}".format(
        ele.find('{*}description').text,
        ele.find('{*}serial-number').text)
    )
print("\nModule list:")
for mod in docroot.iter('{*}chassis-module'):
    modnum += 1
    print("Module {}: {}, type {}".format(
        modnum,
        mod.find('{*}name').text,
        mod.find('{*}description').text)
    )
