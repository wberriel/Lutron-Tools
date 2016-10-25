# Script Name   : Lutron_Device
# Author        : William Berriel
# Created       : Oct 25 2016
# Last Modified :
# Version       : 0.01

# Modifications :

# Description   : This class will hold a Lutron Device and State


class Lutron_Device(object):
    """ Stores the Device Metadata and State"""

    def __init__(self, Integration_ID=0, name=None, room=None):
        """ Constructor takes an optional Integration_ID, name, and area."""
        # Integration_ID is an unsigned integer
        self.Integration_ID = Integration_ID
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
