import unittest
from numconv import *

class testint(unittest.TestCase):
    def testConvertToBinary(self):
        val = convert("0.0.1.33", SysNames.ipv4, SysNames.binary);
        self.assertEqual(str(val), "100100001")

    def testConvertToHex(self):
        val = convert("0.0.0.69", SysNames.ipv4, SysNames.hex);
        self.assertEqual(str(val), "0x45")

    def testConvertToInt(self):
        val = convert("0.0.11.109", SysNames.ipv4, SysNames.int);
        self.assertEqual(str(val), "2925")

    def testConvertToRoman(self):
        val = convert("0.0.0.212", SysNames.ipv4, SysNames.roman);
        self.assertEqual(str(val), "CCXII")

    def testConvertToIpv6(self):
        val = convert("0.0.0.72", SysNames.ipv4, SysNames.ipv6);
        self.assertEqual(str(val), "::48")

if __name__ == '__main__':
    unittest.main()
