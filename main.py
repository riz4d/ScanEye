import subprocess
import socket
from ping3 import ping, verbose_ping
from core.ping_ip import ping_ip
from libs.tcp_conf import ports
from core.tcp_scan import tcp_scan
from core.rtsp import rtsp_scan
from core.banner import scaneye_banner

def scan_ip_range(base_ip):
    with open('log.txt', 'a') as file:
        file.write(f"Scanned Report Of Gateway {base_ip}\n")
        file.close
    base_ip = ".".join(base_ip.split(".")[:3])
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        pinged_result = ping_ip(ip)
        if pinged_result:
            rtsp_bool=rtsp_scan(ip=ip)
            if rtsp_bool != False:
                tcp_port_status = tcp_scan(ip=ip,ports=ports)
                with open('log.txt', 'a') as file:
                    file.write(f"\nHost: {ip}\nState: up\nPort: 554\nState: open{rtsp_bool[1]}\n{tcp_port_status}\n")
                
        print(pinged_result)
def option_list():
    
    print("\nSelect an option:")
    print("1) Scan CCTV's")
    print("2) Documentation")
    print("3) Exit")
        
        
def option():
    while True:
        option_list()
        choice = input("Enter your choice [1-3]: ").strip()
        
        if choice == '1':
            ip_addr = input("Enter Network Gateway (192.168.25.1) : ")
            scan_ip_range(ip_addr)
        elif choice == '2':
            break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    scaneye_banner()
    option()
    