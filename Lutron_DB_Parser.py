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
import Lutron_DB


class Lutron_DB_Parser(object):

    def __init__(self, DBTree):
        self.DBTree = DBTree

        self.Root = self.DBTree.getroot()

    @classmethod
    def fromFile(cls, filename):
        return cls(ET.ElementTree(file=filename))

    @classmethod
    def fromServer(cls, ipAddress):
        pass

    def createLutron_DB(self):
        root = self.DBTree.getroot()
        name = root.find("ProjectName").attrib.get("ProjectName")
        newDB = Lutron_DB(name)

        areas = root.find("Areas")
        # convert this to a recursive function
        for node in areas.iter("Area"):
            areaname = node.attrib.get("Name")
            area_Integration_ID = node.attrib.get("IntegrationID")
            tempArea = Lutron_Area(areaname, area_IntegrationID)
            newDB.areas[area_Integration_ID] = tempArea

            # only bottom level Areas can have devices
            # bottom level will have an empty "Areas" element
            if not len(list(node.find("Areas"))):

                for devicegroup in node.iter("DeviceGroup"):
                    devGroupName = devicegroup.attrib.get("Name")
                    print "\t%s group:" % devGroupName
                    for device in devicegroup.iter("Device"):

                        devName = device.attrib.get("Name")
                        devType = device.attrib.get("DeviceType")
                        integrationID = device.attrib.get("IntegrationID")

                        # if the device has a devname, it exists and it's a
                        # filler device.
                        if(devName):

                            tempDevice = Lutron_Device(integrationID,
                                                       devName,
                                                       tempArea)
                            newDB.devices = tempDevice
                            tempArea.devices = tempDevice

                            print "\t\t%s - %s: ID = %s" % (devName, devType,
                                                            integrationID)
        return newDB

    def printDevices(self):
        root = self.DBTree.getroot()
        areas = root.find("Areas")
        for node in areas.iter("Area"):
            areaname = node.attrib.get("Name")
            print "%s :" % areaname

            # only bottom level Areas can have devices
            # bottom level will have an empty "Areas" element
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
test = Lutron_DB_Parser.fromFile("eeny_demo.xml")
test.printDevices()
