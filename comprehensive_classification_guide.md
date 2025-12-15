# Network Traffic Classification - Comprehensive Guide

This document contains classification rules and key indicators for all traffic types.
Use this guide to classify network flows based on their characteristics.


================================================================================
# Normal
================================================================================
## What is Normal?

Normal network traffic represents legitimate, non-malicious communication between devices in an IoT network. This includes regular data exchanges, device status updates, and standard protocol communications.




================================================================================
# Arp_Spoofing
================================================================================
## What is Arp_Spoofing?

ARP (Address Resolution Protocol) spoofing is an attack where an attacker sends falsified ARP messages over a local area network. This results in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network.




### Key Indicators:

- Fwd Header Size Max > 1.5 (very high compared to other classes)

- Fwd Header Size Min > 1.5 (very high)

- Bwd Header Size Max > 2.0 (very high)

- Flow Pkts Per Sec > 0.3 (high packet rate)

- Short inter-arrival times (burst pattern)





================================================================================
# BotNet_DDOS
================================================================================
## What is BotNet_DDOS?

Botnet DDoS (Distributed Denial of Service) attacks involve multiple compromised devices (bots) coordinated to flood a target with traffic, overwhelming its resources and making it unavailable to legitimate users.




### Key Indicators:

- Very high packet rates

- Sustained high traffic volume

- Asymmetric traffic (high down/up ratio)

- Multiple source patterns





================================================================================
# HTTP_Flood
================================================================================
## What is HTTP_Flood?

HTTP flood attacks overwhelm a web server by sending a large number of HTTP requests, exhausting server resources and preventing legitimate users from accessing the service.




### Key Indicators:

- High HTTP request rates

- Many connection attempts

- Port 80/443 traffic

- High packet counts





================================================================================
# ICMP_Flood
================================================================================
## What is ICMP_Flood?

ICMP flood attacks (also known as ping floods) overwhelm a target by sending a large number of ICMP packets, typically ping requests, causing network saturation and denial of service.




### Key Indicators:

- Very high ICMP packet rates

- Ping flood patterns

- Very short inter-arrival times

- Network saturation patterns





================================================================================
# MQTT_Flood
================================================================================
## What is MQTT_Flood?

MQTT flood attacks target IoT devices using the MQTT protocol by sending excessive publish/subscribe messages, overwhelming the MQTT broker and disrupting IoT communications.




### Key Indicators:

- High MQTT message rates

- Port 1883/8883 traffic

- Excessive publish/subscribe messages

- Broker overload patterns





================================================================================
# Port_Scanning
================================================================================
## What is Port_Scanning?

Port scanning is a reconnaissance activity where an attacker probes a network to discover open ports and services, identifying potential vulnerabilities before launching an attack.




### Key Indicators:

- Multiple port connection attempts

- Sequential port patterns

- Low data transfer

- Many incomplete connections

- Reconnaissance patterns





================================================================================
# TCP_Flood
================================================================================
## What is TCP_Flood?

TCP flood attacks (including SYN floods) overwhelm a target by sending a large number of TCP connection requests, exhausting the connection table and preventing legitimate connections.




### Key Indicators:

- Very high TCP connection attempts

- SYN flood patterns

- Low connection completion

- Many incomplete connections

- Connection table exhaustion





================================================================================
# Classification Decision Tree
================================================================================

Follow these steps to classify a network flow:

1. **Check Header Sizes**
   - If Fwd Header Size Max > 1.5 AND Bwd Header Size Max > 2.0 → Arp_Spoofing
   - If Fwd Header Size Max < 0.2 AND Bwd Header Size Max < 0.0 → BotNet_DDOS

2. **Check Packet Rates**
   - If Flow Pkts Per Sec > 0.04 → ICMP_Flood (likely)
   - If Flow Pkts Per Sec ≈ 0.0 AND negative packet values → BotNet_DDOS

3. **Check Response Packets/Bytes**
   - If Resp Pkts > 2.0 AND Resp Ip Bytes > 2.5 → HTTP_Flood

4. **Check Traffic Patterns**
   - Balanced traffic with moderate values → Normal
   - High asymmetry with burst patterns → Check other indicators

5. **Compare with Feature Value Criteria**
   - Use the specific feature ranges provided for each class above
   - Match the flow's feature values with the classification rules


================================================================================
# Quick Reference Table
================================================================================

| Class | Key Indicator | Feature Value |
|-------|---------------|---------------|
| Arp_Spoofing | High header sizes | Fwd Header Size Max > 1.5, Bwd Header Size Max > 2.0 |
| BotNet_DDOS | Very low packet rate, negative values | Flow Pkts Per Sec ≈ 0.0, negative packets/bytes |
| HTTP_Flood | High response packets/bytes | Resp Pkts > 2.0, Resp Ip Bytes > 2.5 |
| ICMP_Flood | Higher packet rate | Flow Pkts Per Sec > 0.04 |
| Normal | Balanced, moderate values | Balanced traffic, moderate packet rates |
