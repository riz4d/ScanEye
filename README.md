ScanEye is designed to scan a range of IP addresses to detect security surveillance cameras that are streaming video over HTTP or RTSP. The tool sends HTTP requests to each IP address in the specified range and checks for active HTTP services and potential video stream

### Features
- IP Range Scanning: Automatically checks each IP in the given range.
- Port Scanning: Detects open HTTP and RTSP ports.
- Stream Detection: Detects whether an IP address is hosting a video stream.
- Logs: Generates a log file with details about detected devices.

### Security Considerations
- Ensure you have permission to scan the IP addresses to avoid violating legal regulations.
- Some cameras may require authentication, which can be handled by sending appropriate HTTP headers with credentials.
