import socket
from datetime import datetime

#target input
target = input("Enter the target IP address or domain (e.g., 127.0.0.1 or example.com): ")

#resolve to IP address
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid host.")
    exit()

#file to log results
log_file = f"port_scan_results_{target_ip}.txt"
with open(log_file, "w") as f:
    f.write(f"Port scan results for {target} ({target_ip})\n")
    f.write(f"Scan started at: {datetime.now()}\n\n")
    f.write("Port\tStatus\n")
    f.write("-" * 30 + "\n")

    #common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306,3389, 8080, 8443, 9000, 9200, 27017]

    print(f"Scanning target: {target_ip}...")
    start_time = datetime.now()

    for port in range(1, 1024):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                try:
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner = sock.recv(1024).decode().strip()
                    output = f"Port {port} is open. Banner: {banner}"
                except:
                    output = f"Port {port} is open. Banner: Not available"

                print(output)
                f.write(output + "\n")

            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            break
        except Exception as e:
            error_message = f"Error scanning port {port}: {e}"
            print(error_message)
            f.write(error_message + "\n")   
    
    end_time = datetime.now()
    duration = f"\nScan completed in: {end_time - start_time}"
    print(duration)
    f.write(duration + "\n")