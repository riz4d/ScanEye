
import socket

def tcp_scan(ip,ports):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"{GREEN}Port {port} is open on {ip}.{RESET}")
                    return f"Port {port} is open on {ip}."
                else:
                    return f"Port {port} is closed on {ip}."
        except Exception as e:
            print(f"Error scanning {ip} on port {port}: {e}")

