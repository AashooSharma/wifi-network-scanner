import os
import re

def get_local_ip():
    # Run ifconfig command and capture the output
    ifconfig_result = os.popen('ifconfig').read()

    # Extract the IP address using regex
    ip_search = re.search(r'wlan0:.*?inet (\d+\.\d+\.\d+\.\d+)', ifconfig_result, re.DOTALL)
    if ip_search:
        return ip_search.group(1)
    else:
        return None

def calculate_network_range(ip):
    # Assuming a default subnet mask of 255.255.255.0
    ip_parts = ip.split('.')
    network_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
    return network_range

def scan_network(network_range):
    # Run nmap command to scan the network
    nmap_result = os.popen(f'nmap -sP {network_range}').read()
    return nmap_result

def get_connected_devices(nmap_result):
    # Extract IPs from nmap output
    devices = re.findall(r'Nmap scan report for (\d+\.\d+\.\d+\.\d+)', nmap_result)
    return devices

def scan_device_ports(ip):
    # Scan the device for open ports and services
    nmap_port_result = os.popen(f'nmap -sV {ip}').read()
    return nmap_port_result

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print(f"Local IP: {local_ip}")

        network_range = calculate_network_range(local_ip)
        print(f"Network Range: {network_range}")

        nmap_result = scan_network(network_range)
        print(f"Connected Devices:\n{nmap_result}")

        devices = get_connected_devices(nmap_result)
        for device in devices:
            print(f"\nScanning {device} for open ports and services...")
            device_scan_result = scan_device_ports(device)
            print(device_scan_result)
    else:
        print("Could not determine the local IP address.")
      
