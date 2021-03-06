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
from Lutron_DB import Lutron_DB, Lutron_Area, Lutron_Device, Lutron_Output


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
            area_IntegrationID = node.attrib.get("IntegrationID")
            tempArea = Lutron_Area(areaname, area_IntegrationID)
            newDB.areas[area_IntegrationID] = tempArea

            # only bottom level Areas can have devices
            # bottom level will have an empty "Areas" element
            if not len(list(node.find("Areas"))):

                for devicegroup in node.iter("DeviceGroup"):
                    for device in devicegroup.iter("Device"):

                        device_Name = device.attrib.get("Name")
                        device_IntegrationID = \
                            device.attrib.get("IntegrationID")

                        # if the device has a devname, it exists and it's a
                        # filler device.
                        if(device_Name):

                            tempDevice = Lutron_Device(device_IntegrationID,
                                                       device_Name,
                                                       tempArea)
                            newDB.devices[device_IntegrationID] = tempDevice
                            tempArea.devices[device_IntegrationID] = tempDevice

                # The outputs will be found in Output objects which are part of
                # an Outputs object.
                for output in node.find("Outputs").iter("Output"):
                    output_Name = output.attrib.get("Name")
                    output_IntegrationID = output.attrib.get("IntegrationID")
                    tempOutput = Lutron_Output(output_IntegrationID,
                                               output_Name,
                                               tempArea)
                    tempArea.outputs[output_IntegrationID] = tempOutput
                    newDB.outputs[output_IntegrationID] = tempOutput

        return newDB

test = Lutron_DB_Parser.fromFile("eeny_demo.xml")
newDB = test.createLutron_DB()

print newDB
