from ipaddress import *

#Wrapper function to converting to ipv4
def convert(num, args=None):
    try:
        ipaddress = ip_address(num)
        if isinstance(ipaddress, IPv4Address): return ipaddress
        elif isinstance(ipaddress, IPv6Address):
            if ipaddress.ipv4_mapped is not None: return ipaddress.ipv4_mapped
            elif ipaddress.sixtofour is not None: return ipaddress.sixtofour
    except Exception:
        return "Error during conversion"
