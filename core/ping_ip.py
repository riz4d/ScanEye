import subprocess
import socket
from ping3 import ping, verbose_ping

def ping_ip(ip_address):
    response_time = ping(ip_address, timeout=1)
    if response_time is not None:
        print(f"{ip_address} is reachable. Response time: {response_time:.2f} ms")
        return True
    else:
        return f"{ip_address} is not reachable."