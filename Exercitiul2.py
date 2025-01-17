# ip 10.8.11.6/24.

import subprocess

def scan_vlan(vlan_subnet):
    active_ips = []
    for i in range(1, 255):  
        ip = f"{vlan_subnet}.{i}"
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            active_ips.append(ip)
    return active_ips

if __name__ == "__main__":
    vlan_subnet = "10.8.11"  
    print("Scanning VLAN for active machines...")
    active_ips = scan_vlan(vlan_subnet)
    print("Active IPs in the VLAN:")
    for ip in active_ips:
        print(ip)
