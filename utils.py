from scapy.all import get_if_list

def list_interfaces():
    return get_if_list()


def log_interface_info():
    interfaces = list_interfaces()
    print("[*] Available Interfaces:")
    for iface in interfaces:
        print(f"  - {iface}")