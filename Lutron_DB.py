# Script Name   : Lutron_DB
# Author        : William Berriel
# Created       : Oct 26 2016
# Last Modified :
# Version       : 0.01

# Modifications :

# Description   : Contrary to the name, this is not a database. It's a simple
# object representing the XML database for a Lutron Processor.


class Lutron_DB(object):
    """Stores a representation of a Lutron XML Database."""

    def __init__(self, name=None):
        self.name = name
        self.areas = {}
        self.devices = {}
        self.outputs = {}

    def __repr__(self):
        return "<Lutron_DB Name: %s" % (self.name)

    def __str__(self):
        return_string = "Lutron_DB: %s" % (self.name)
        if(self.areas.keys()):
            return_string += "\nAreas:"

        for key in self.areas.keys():
            return_string += "\n%s" % self.areas[key]

        return return_string


class Lutron_Area(object):
    """ Stores the Metadata, sub areas, devices, and outputs for an area."""

    def __init__(self, IntegrationID=0, name=0):
        """Init will have an optional Integration_ID and name."""

        self.IntegrationID = IntegrationID
        self.name = name
        self.parent = None

        self.areas = {}
        self.devices = {}
        self.outputs = {}

    def __repr__(self):
        return "<Lutron_Area Name: %s IntegrationID: %s>" % \
            (self.name, self.IntegrationID)

    def __str__(self):
        return_string = "Area: %s-%s" % (self.name, self.IntegrationID)
        if(self.devices.keys()):
            return_string += "\nDevices:"
            for key in self.devices.keys():
                return_string += "\n%s" % self.devices[key]

        if(self.outputs.keys()):
            return_string += "\nOutputs:"
            for key in self.outputs.keys():
                return_string += "\n%s" % self.outputs[key]

        return return_string


class Lutron_Device(object):
    """ Stores the Device Metadata and State"""

    def __init__(self, IntegrationID=0, name=None, area=None):
        """ Constructor takes an optional Integration_ID, name, and area."""
        # Integration_ID is an unsigned integer
        self.IntegrationID = IntegrationID
        # Pointer to the containing area object.
        self.area = area
        # Name should be a string.
        self.name = name
        # LED_status stores the status of up to 10 LEDS
        # (current keypads use 7).
        self.LED_status = [0] * 10
        # button_status stores the status of up to 20 buttons. (current keypads
        # use 10).
        self.button_status = [0] * 20

    def __repr__(self):
        return "<Lutron_Device Name: %s IntegrationID: %s>" % \
            (self.name, self.IntegrationID)

    def __str__(self):
        return "%s-%s" % (self.name, self.IntegrationID)


class Lutron_Output(object):
    """ Stores Output Metadata and state."""

    def __init__(self, IntegrationID=0, name=None, area=None):
        """ Constructor takes an optional Integration_ID, name, and area."""

        self.IntegrationID = IntegrationID
        # Pointer to the area object containing the device.
        self.area = area
        # Name should be  a string.
        self.name = name
        # level is from 0.0 to 100.0
        self.level = 0.0
        # tilt is from 0.0 to 100.0
        self.tilt = 0.0
        # fade is an integer in secods from 0 to 14400 (4 hours)
        self.fade = 0

    def __repr__(self):
        return "<Lutron_Output Name: %s IntegrationID: %s Level: %s>" % \
            (self.name, self.IntegrationID, self.level)

    def __str__(self):
        return "%s-%s: %s" % (self.name, self.IntegrationID, self.level)
