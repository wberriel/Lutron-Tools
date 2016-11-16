# Script Name   : Lutron_Area
# Author        : William Berriel
# Created       : Oct 25 2016
# Last Modified :
# Version       : 0.01

# Modifications :

# Description   : This class will hold areas. Areas can contain either Areas or
# Devices & Outputs, but not both.


import Lutron_Device
import Lutron_Output


class Lutron_Area(object):
    """ Stores the Metadata, sub areas, devices, and outputs for an area."""

    def __init__(self, Integration_ID=0, name=0):
        """Init will have an optional Integration_ID and name."""

        self.Integration_ID = Integration_ID
        self.name = name
        self.parent = None

        self.areas = {}
        self.devices = {}
        self.outputs = {}
