# Script Name   : Lutron_Output
# Author        : William Berriel
# Created       : Oct 25 2016
# Last Modified :
# Version       : 0.01

# Modifications :

# Description   : This class will hold an Output and State


class Lutron_Output(object):
    """ Stores Output Metadata and state."""

    def __init__(self, Integration_ID=0, name=None, area=None):
        """ Constructor takes an optional Integration_ID, name, and area."""

        self.Integration_ID = Integration_ID
        # Pointer to the area object containing the device.
        self.area = area
        # Name should be  a string.
        self.name = name
        # level is from 0.0 to 100.0
        self.level = 0.0
        # tilt is from 0.0 to 100.0
        self.tilt = 0.0
        #fade is an integer in secods from 0 to 14400 (4 hours)
        self.fade = 0

