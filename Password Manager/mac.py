import uuid
import platform
import os

# Class to get the mac address
class GetMac:
    @staticmethod
    def get_mac_address():
        if platform.system().lower() == "linux":
            # For Linux
            try:
                mac = open('/sys/class/net/eth0/address').read()
            except IOError:
                return "Unable to read MAC address"
        elif platform.system().lower() == "darwin":
            # For macOS
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2,6)][::-1])
        elif platform.system().lower() == "windows":
            # For Windows
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2,6)][::-1])
        else:
            return "Unsupported platform"

        return mac

