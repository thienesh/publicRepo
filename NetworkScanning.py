from scapy.all import srp, Ether, ARP


# import scapy

def scan_network(interface):
    # Create ARP request
    arp_request = ARP(pdst="192.168.1.1/24")
    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine ARP request and Ethernet frame
    packet = ether / arp_request

    # Send and receive packets using srp() function
    result = srp(packet, timeout=3, iface=interface, verbose=False)[0]

    # List to store IP and MAC addresses of active devices
    active_devices = []

    # Process response packets
    for sent_packet, received_packet in result:
        active_devices.append({
            "ip": received_packet[ARP].psrc,
            "mac": received_packet[Ether].src
        })

    return active_devices


if __name__ == "__main__":
    # Replace 'eth0' with the name of your network interface
    active_devices = scan_network("Wi-Fi")
    print("Active Devices:")
    for device in active_devices:
        print(f"IP: {device['ip']} MAC: {device['mac']}")
