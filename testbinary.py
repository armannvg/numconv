import unittest
from numconv import *

class testbinary(unittest.TestCase):
    def testConvertToHex(self):
        val = convert("11001010", SysNames.binary, SysNames.hex);
        self.assertEqual(str(val), "0xca")

        val = convert("100011100", SysNames.binary, SysNames.hex);
        self.assertEqual(str(val), "0x11c")

    def testConvertToInt(self):
        val = convert("11001010", SysNames.binary, SysNames.int);
        self.assertEqual(str(val), "202")

        val = convert("10100011", SysNames.binary, SysNames.int);
        self.assertEqual(str(val), "163")

    def testConvertToRoman(self):
        val = convert("11101110", SysNames.binary, SysNames.roman);
        self.assertEqual(str(val), "CCXXXVIII")

    def testConvertToIpv4(self):
        val = convert("110011", SysNames.binary, SysNames.ipv4);
        self.assertEqual(str(val), "0.0.0.51")

    def testConvertToIpv6(self):
        val = convert("111111", SysNames.binary, SysNames.ipv6);
        self.assertEqual(str(val), "::3f")

if __name__ == '__main__':
    unittest.main()
