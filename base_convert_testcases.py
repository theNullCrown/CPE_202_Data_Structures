import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(255,2),"11111111")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base_EdgeCases(self):
        self.assertEqual(convert(0,2),"0")
        self.assertEqual(convert(0,20),"0")

if __name__ == "__main__":
        unittest.main()