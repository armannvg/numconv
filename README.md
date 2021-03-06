numconv
=======

numconv is a small utility that converts numbers between different systems. The following systems are supported:

* Integer
* Binary
* Hex
* Roman
* IPv4
* IPv6

A number has a specific source system and it can be converted to any destination system.

Usage
=======

**convert from int to hex:** numconv.py --num 87 --source_system int --dest_system hex

0x57

**Same as above, but with short options:** numconv.py -n 87 -s int -d hex

0x57

**convert from hex to binary:** numconv.py --n 0xbc -s hex -d binary

10111100

**convert from hex to IPv4:** numconv.py -n 0xbc -s hex -d ipv4

0.0.0.188

**convert from int to roman:** numconv.py -n 24 -s int -d roman

XXIV

**convert from roman to hex:** numconv.py -n XI -s roman -d hex

0xb

There are also additional options to get further information about the converted number:

**convert hex to binary and print active bits:** numconv.py -n 0xbc -s hex -d binary --show_active_bits

10111100 [2, 3, 4, 5, 7]

If no destination system is specified then all conversions are printed out:

**convert from int:** numconv.py -n 119 -s int

binary: 1110111

hex: 0x77

int: 119

ipv4: 0.0.0.119

ipv6: ::77

roman: CXIX

**convert from hex:** numconv.py -n 0x3f -s hex

binary: 111111

hex: 0x3f

int: 63

ipv4: 0.0.0.63

ipv6: ::3f

roman: LXIII

Additional information
=======

This program requires Python 3.3 or above

Unit tests all can be executed with "python33 -m unittest discover" from the source code directory. This should find all the test files (i.e. test*) and execute them.

License: Creative Commons Attribution Share-Alike license (http://creativecommons.org/licenses/by-sa/3.0/)
