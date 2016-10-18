# Script Name	: LutronDB-Parser.py
# Author		: William Berriel
# Created		: March 08  2016
# Last Modified	: 
# Version		: 0.01

# Modifications	: 

# Description	: This module will handle parsing a lutron XML database which is available from a Lutron processor. It should work for RadioRA or HOmeworks QS.


import xml.etree.ElementTree as ET

class LutronDBParser(object):
    
    def __init__(self, DBTree):
        self.DBTree = DBTree
        
        self.Root = self.DBTree.getroot()
        
        
    @classmethod
    def fromFile(cls, filename):
        return cls(ET.ElementTree(file=filename))
    
    @classmethod
    def fromServer(cls, ipAddress):
        pass
    
    def printDevices():
        for node in DBTree.iter('Area'):
            areaname = node.attribute.get("Name")
            for devicegroup in node.iter("DeviceGroups"):
                devGroupName = devicegroup.attribute.get("Name")
                for device in devicegroup.iter("Device"):
                    devName = device.attribute.get("Name")

                    if(devName):
                         print ('Area %s - DeviceGroup %s - Device Name %s' % areaname, devGroupName, devName)
    
    
test = LutronDBParser.fromFile("eeny demo.xml")