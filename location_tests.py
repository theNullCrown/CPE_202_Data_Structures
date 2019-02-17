# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):


    def test_init(self):
        loc = Location("SLO", 35.3, -120.7) 
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

    def test_init(self):
        loc = Location("Paris", 38, 4) 
        self.assertEqual(loc.name, "Paris")
        self.assertEqual(loc.lat, 38)
        self.assertEqual(loc.lon, 4)


    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    
    def test_repr(self): 
        loc = Location("LA", 50, -132.7) 
        self.assertEqual(repr(loc), "Location('LA', 50, -132.7)")

    def test_repr(self): 
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc), "Location('Paris', 48.9, 2.4)")

    def test_equal(self): 
        loc = Location("Paris", 48.9, 2.4)
        loc2 = Location("Paris", 48.9, 2.4) 
        self.assertEqual(loc, loc2)

    def test_equal(self): 
        loc = Location('LA', 50, -132.7)
        loc2 = Location('LA', 50, -132.7) 
        self.assertEqual(loc, loc2)    


if __name__ == "__main__":
        unittest.main()
