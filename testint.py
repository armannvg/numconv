import unittest
from numconv import *

class testint(unittest.TestCase):
    def testConvertToHex(self):
        val = convert("47", SysNames.int, SysNames.hex);
        self.assertEqual(str(val), "0x2f")

    def testConvertToBinary(self):
        val = convert("75", SysNames.int, SysNames.binary);
        self.assertEqual(str(val), "1001011")

    def testConvertToRoman(self):
        val = convert("26", SysNames.int, SysNames.roman);
        self.assertEqual(str(val), "XXVI")

    def testConvertToIpv4(self):
        val = convert("1902", SysNames.int, SysNames.ipv4);
        self.assertEqual(str(val), "0.0.7.110")

    def testConvertToIpv6(self):
        val = convert("650", SysNames.int, SysNames.ipv6);
        self.assertEqual(str(val), "::28a")

if __name__ == '__main__':
    unittest.main()
