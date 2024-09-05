import socket
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
def rtsp_scan(ip):
    port = 554
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{GREEN}Port {port} is open on {ip}. Checking for RTSP...{RESET}")
                rtsp_log = check_rtsp(ip)
                return True,rtsp_log
            else:
                f"Port {port} is crtsp_scan closed on {ip}."
                return False
    except Exception as e:
        print(f"Error scanning {ip} on port {port}: {e}")

def check_rtsp(ip):
    try:
        with socket.create_connection((ip, 554), timeout=2) as sock:
            request = f"OPTIONS rtsp://{ip}/ RTSP/1.0\r\nCSeq: 1\r\n\r\n".encode()
            sock.sendall(request)
            response = sock.recv(1024).decode('utf-8', errors='ignore')
            if "RTSP" in response:
                print(f"{GREEN}Port 554 on {ip} is running RTSP.{RESET}")
                return f"Port 554 on {ip} is running RTSP."
            else:
                print(f"Port 554 on {ip} did not respond with RTSP headers.")
                return False
    except Exception as e:
        print(f"{RED}Error checking RTSP on {ip}: {e}{RESET}")

