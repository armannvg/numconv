from ipaddress import *

#Wrapper function to converting to ipv6
def convert(num, args=None):
    try:
        return IPv6Address(num)
    except Exception:
        return "Error during conversion"
