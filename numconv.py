import sys
import argparse
import roman
from ipaddress import *

import conv2roman
import conv2binary
import conv2ipv4
import conv2ipv6

__version__ = "0.1"

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

#Supported numbering systems
SysNames = Enum(["int", "hex", "binary", "roman", "ipv4", "ipv6"])

def convertFromInt(num, dest_system, args=None):
    if dest_system == SysNames.binary: return conv2binary.convert(num, args)
    elif dest_system == SysNames.hex: return hex(num)
    elif dest_system == SysNames.roman: return conv2roman.convert(num)
    elif dest_system == SysNames.int: return num
    elif dest_system == SysNames.ipv4: return conv2ipv4.convert(num)
    elif dest_system == SysNames.ipv6: return conv2ipv6.convert(num)

def convert(num, source_system, dest_system, args=None):
    if source_system == SysNames.int:
        return convertFromInt(int(num), dest_system, args)

    if source_system == SysNames.hex:
        return convertFromInt(int(num, 16), dest_system, args)

    if source_system == SysNames.binary:
        return convertFromInt(int(num, 2), dest_system, args)

    if source_system == SysNames.roman:
        return convertFromInt(roman.from_roman(num), dest_system, args)

    if (source_system == SysNames.ipv4) or (source_system == SysNames.ipv6):
        ipaddress = ip_address(num)
        return convertFromInt(int(ipaddress), dest_system, args)

    return "No conversion applicable"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', help='Number to convert')
    parser.add_argument('-s', '--source_system', help='Number system to convert from')
    parser.add_argument('-d', '--dest_system', default=None, help='Number system to convert to')
    parser.add_argument('--show_active_bits', dest='show_active_bits', action='store_true', help='Display location of active bits for binary numbers')
    args = parser.parse_args()

    try:
        if args.source_system not in SysNames:
            print("Invalid source system")
        elif args.dest_system is None:
            for system in sorted(SysNames):
                output = convert(args.num, args.source_system, system, args)
                print(str(system) + ": " + str(output))
        elif args.dest_system not in SysNames:
            print("Invalid destination system")
        else:
            output = convert(args.num, args.source_system, args.dest_system, args)
            print(str(output))
    except Exception as e:
        print("Error during number conversion: " + str(e))
