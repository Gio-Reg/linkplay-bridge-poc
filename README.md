# LinkPlay Bridge PoC
OmniStream Core: Universal Audio Discovery Engine

# Overview
This Proof of Concept demonstrates a protocol-agnostic discovery layer for professional audio environments. It utilizes mDNS (Multicast DNS) to map local network hardware, specifically targeting the LinkPlay/WiiMu ecosystem used by brands like JAM, Marshall, and Audio Pro.

# Business Value
By identifying legacy hardware and interrogating internal states via UPnP/HTTP, this bridge allows SaaS audio providers (like Soundtrack Your Brand) to onboard "Brownfield" locations without requiring proprietary hardware installations.

# Features
Multi-Service Scanning: Detects LinkPlay, Sonos, Google Cast, and Spotify Connect.

State Interrogation: Retrieves device metadata, firmware, and synchronization status.

Zero-Config: Automatic IP resolution via zeroconf.
