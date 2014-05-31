import unittest
from numconv import *

class testint(unittest.TestCase):
    def testConvertToBinary(self):
        val = convert("LXXI", SysNames.roman, SysNames.binary);
        self.assertEqual(str(val), "1000111")

    def testConvertToHex(self):
        val = convert("LXXXIII", SysNames.roman, SysNames.hex);
        self.assertEqual(str(val), "0x53")

    def testConvertToInt(self):
        val = convert("XCIX", SysNames.roman, SysNames.int);
        self.assertEqual(str(val), "99")

    def testConvertToIpv4(self):
        val = convert("MDCCC", SysNames.roman, SysNames.ipv4);
        self.assertEqual(str(val), "0.0.7.8")

    def testConvertToIpv6(self):
        val = convert("DI", SysNames.roman, SysNames.ipv6);
        self.assertEqual(str(val), "::1f5")

if __name__ == '__main__':
    unittest.main()
