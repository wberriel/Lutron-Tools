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
        self.areas = []


