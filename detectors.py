from scapy.all import ARP, Ether, Dot11Deauth
from alerts import alert

arp_table = {}
mac_counter = {}

def detect_arp_spoof(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 2:
        real_mac = arp_table.get(pkt[ARP].psrc)
        current_mac = pkt[ARP].hwsrc
        if real_mac and real_mac != current_mac:
            alert(f"ARP Spoofing Detected! IP: {pkt[ARP].psrc} is now at {current_mac}, was {real_mac}")
        else:
            arp_table[pkt[ARP].psrc] = current_mac

def detect_mac_spoof(pkt):
    if pkt.haslayer(Ether):
        mac = pkt[Ether].src
        if mac:
            mac_counter[mac] = mac_counter.get(mac, 0) + 1
            if mac_counter[mac] == 100:
                alert(f"Possible MAC Spoofing/Flooding detected from: {mac}")

def detect_deauth(pkt):
    if pkt.haslayer(Dot11Deauth):
        source = pkt.addr2
        target = pkt.addr1
        alert(f"Deauthentication Attack Detected! Source: {source}, Target: {target}")


def run_all_detectors(pkt):
    detect_arp_spoof(pkt)
    detect_mac_spoof(pkt)
    detect_deauth(pkt)
