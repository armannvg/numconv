import unittest
from numconv import *

class testint(unittest.TestCase):
    def testConvertToBinary(self):
        val = convert("::5c", SysNames.ipv6, SysNames.binary);
        self.assertEqual(str(val), "1011100")

    def testConvertToHex(self):
        val = convert("::efa", SysNames.ipv6, SysNames.hex);
        self.assertEqual(str(val), "0xefa")

    def testConvertToInt(self):
        val = convert("::bc", SysNames.ipv6, SysNames.int);
        self.assertEqual(str(val), "188")

    def testConvertToRoman(self):
        val = convert("::c", SysNames.ipv6, SysNames.roman);
        self.assertEqual(str(val), "XII")

    def testConvertToIpv4(self):
        val = convert("::7", SysNames.ipv6, SysNames.ipv4);
        self.assertEqual(str(val), "0.0.0.7")

if __name__ == '__main__':
    unittest.main()
