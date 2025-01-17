import subprocess

def scan_services(ip):
    print(f"Scanning services on {ip}...")
    try:
        result = subprocess.run(['nmap', '-sV', '-p-', ip], capture_output=True, text=True)
        if "open" in result.stdout:  
            print(f"Services found on {ip}:")
            print(result.stdout)
        else:
            print(f"No services found on {ip}.")
    except Exception as e:
        print(f"Error scanning {ip}: {e}")

def scan_vlan(vlan_subnet):
    
    for i in range(1, 255):  
        ip = f"{vlan_subnet}.{i}"
        print(f"Checking {ip}...")
        ping_result = subprocess.run(['ping', '-c', '1', '-W', '1', ip],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ping_result.returncode == 0:
            print(f"{ip} is active. Scanning for services...")
            scan_services(ip)
        else:
            print(f"{ip} is not active. Skipping.")

if __name__ == "__main__":
    vlan_subnet = "10.8.11"  
    print("Scanning VLAN for active machines and their services...")
    scan_vlan(vlan_subnet)

