import unittest
from numconv import *

class testhex(unittest.TestCase):
    def testConvertToBinary(self):
        val = convert("0x4c", SysNames.hex, SysNames.binary);
        self.assertEqual(str(val), "1001100")

    def testConvertToInt(self):
        val = convert("0x73", SysNames.hex, SysNames.int);
        self.assertEqual(str(val), "115")

    def testConvertToRoman(self):
        val = convert("0x2e", SysNames.hex, SysNames.roman);
        self.assertEqual(str(val), "XLVI")

    def testConvertToIpv4(self):
        val = convert("0x9a", SysNames.hex, SysNames.ipv4);
        self.assertEqual(str(val), "0.0.0.154")

        val = convert("0x00000000000000000000ffff0c0c0000", SysNames.hex, SysNames.ipv4);
        self.assertEqual(str(val), "12.12.0.0")

        val = convert("0x00000000000000000000ffff0c0c00ff", SysNames.hex, SysNames.ipv4);
        self.assertEqual(str(val), "12.12.0.255")

        val = convert("0x00000000000000000000ffffc0a82d26", SysNames.hex, SysNames.ipv4);
        self.assertEqual(str(val), "192.168.45.38")

    def testConvertToIpv6(self):
        val = convert("0xcb", SysNames.hex, SysNames.ipv6);
        self.assertEqual(str(val), "::cb")

if __name__ == '__main__':
    unittest.main()
