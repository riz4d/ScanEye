
import socket

def check_http_https(ip):
    try:
        with socket.create_connection((ip, 80), timeout=2) as sock:
            sock.sendall(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode())
            response = sock.recv(1024).decode('utf-8', errors='ignore')
            if "HTTPS" in response or "https" in response:
                print(f"Port 80 on {ip} appears to be running HTTPS.")
            else:
                print(f"Port 80 on {ip} appears to be running HTTP.")
    except Exception as e:
        print(f"Error checking HTTP/HTTPS on {ip}: {e}")
