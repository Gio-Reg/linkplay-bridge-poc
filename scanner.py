import requests
from zeroconf import ServiceBrowser, Zeroconf
import time
import socket

class SpeakerDiscovery:
    def __init__(self):
        self.found_devices = []

    def add_service(self, zc, type, name):
        info = zc.get_service_info(type, name)
        if info:
            # Convert IP from bytes to string
            addresses = [socket.inet_ntoa(addr) for addr in info.addresses]
            device_data = {
                "name": name,
                "ip": addresses[0] if addresses else "Unknown",
                "port": info.port,
                "type": type
            }
            self.found_devices.append(device_data)
            print(f"✅ Found Speaker: {name} at {device_data['ip']}")

# Initialize the 'Radar'
zeroconf = Zeroconf()
listener = SpeakerDiscovery()

# The "Discovery Radar" for B2B Audio environments
services = [
    "_linkplay._tcp.local.",       # For JAM, Marshall, Audio Pro, etc.
    "_sonos._tcp.local.",          # For Sonos ecosystem
    "_googlecast._tcp.local.",     # For Nest/Chromecast devices
    "_spotify-connect._tcp.local.", # General Spotify-enabled hardware
    "_http._tcp.local."            # Catch-all for basic web-controlled speakers
]
browser = ServiceBrowser(zeroconf, services, listener)

print("📡 Scanning for speakers... (Waiting 10 seconds)")
try:
    time.sleep(10)
    if not listener.found_devices:
        print("❌ No speakers found. Check if they are on the same Wi-Fi!")
except KeyboardInterrupt:
    pass
finally:
    zeroconf.close()


# Use the IP address we just found
IP = "192.168.3.13"

def get_info():
    # Common LinkPlay status endpoints
    endpoints = ["/getStatus", "/getDeviceInfo"]
    
    for ep in endpoints:
        try:
            url = f"http://{IP}{ep}"
            print(f"Trying {url}...")
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                print("💎 SUCCESS! Data received:")
                print(r.text)
                return
        except Exception as e:
            print(f"Could not reach {ep}")

get_info()
