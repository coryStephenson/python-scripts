import time
import pywifi

def get_encryption_type(network):
    encryptions = {
        0: "None",
        1: "WEP",
        2: "WPA",
        3: "WPA2",
        4: "WPA/WPA2",
    }
    akm_values = network.akm
    if akm_values:
        return encryptions.get(akm_values[0], "Unknown")
    return "Unknown"

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(5)  # Wait for the scan to complete

    scan_results = iface.scan_results()
    return scan_results

def print_wifi_info(networks):
    print("\nSite Survey Results:\n")
    print("{:<30} {:<15} {:<10} {:<20}".format("SSID", "BSSID", "Signal", "Encryption"))
    print("-" * 70)

    for network in networks:
        ssid = network.ssid
        bssid = network.bssid
        signal_strength = network.signal
        encryption_type = get_encryption_type(network)

        print("{:<30} {:<15} {:<10} {:<20}".format(ssid, bssid, signal_strength, encryption_type))

if __name__ == "__main__":
    wifi_networks = scan_wifi()
    print_wifi_info(wifi_networks)
