from scapy.all import sniff
from detectors import run_all_detectors
from utils import log_interface_info

if __name__ == "__main__":
    print("[*] Starting WiFi IDS... Logging interfaces:")
    log_interface_info()
    sniff(prn=run_all_detectors, store=0)
