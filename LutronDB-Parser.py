# Script Name	: LutronDB-Parser.py
# Author		: William Berriel
# Created		: March 08  2016
# Last Modified	:
# Version		: 0.01

# Modifications	:

# Description	: This module will handle parsing a lutron XML database which is
# available from a Lutron processor. It should work for RadioRA or HOmeworks
# QS.


# If possible, import the c implemenation, if not, import normal.
try:
        import xmletree.cElementTree as ET
except ImportError:
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

    def printDevices(self):
        root = self.DBTree.getroot()
        areas = root.find("Areas")
        for node in areas.iter("Area"):
            areaname = node.attrib.get("Name")
            print "%s :" % areaname

            # only bottom level Areas can have devices
            if not len(list(node.find("Areas"))):

                for devicegroup in node.iter("DeviceGroup"):
                    devGroupName = devicegroup.attrib.get("Name")
                    print "\t%s group:" % devGroupName
                    for device in devicegroup.iter("Device"):
                        devName = device.attrib.get("Name")
                        devType = device.attrib.get("DeviceType")
                        integrationID = device.attrib.get("IntegrationID")
                        if(devName):
                            print "\t\t%s - %s: ID = %s" % (devName, devType,
                                                            integrationID)
test = LutronDBParser.fromFile("eeny_demo.xml")
test.printDevices()
