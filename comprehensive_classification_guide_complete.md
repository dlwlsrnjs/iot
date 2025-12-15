# Network Traffic Classification - Complete Guide

This is a comprehensive, fixed guide for classifying network traffic flows.
Always use this guide when classifying flows. Do not search for other documents.


================================================================================
# Normal
================================================================================
## What is Normal?

Normal network traffic represents legitimate, non-malicious communication between devices in an IoT network. This includes regular data exchanges, device status updates, and standard protocol communications.



## How does Normal behave?

Normal traffic exhibits balanced bidirectional communication, regular packet intervals, moderate packet sizes, and follows expected protocol patterns.



### Feature Value Criteria:
#### Bwd Header Size Tot (`bwd_header_size_tot`)
- **Classification Rule**: If this value is **> 0.523**, it strongly suggests Normal traffic




#### Fwd Header Size Tot (`fwd_header_size_tot`)
- **Classification Rule**: If this value is **> 0.227**, it strongly suggests Normal traffic




#### Resp Pkts (`resp_pkts`)
- **Classification Rule**: If this value is **> 0.882**, it suggests Normal traffic




#### Bwd Pkts Payload.Avg (`bwd_pkts_payload.avg`)
- **Classification Rule**: If this value is **> -0.053**, it suggests Normal traffic




#### Bwd Pkts Payload.Tot (`bwd_pkts_payload.tot`)
- **Classification Rule**: If this value is **> -0.024**, it suggests Normal traffic




#### Orig Pkts (`orig_pkts`)
- **Classification Rule**: If this value is **> 0.406**, it suggests Normal traffic





================================================================================
# Arp_Spoofing
================================================================================
## What is Arp_Spoofing?

ARP (Address Resolution Protocol) spoofing is an attack where an attacker sends falsified ARP messages over a local area network. This results in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network.



## How does Arp_Spoofing behave?

ARP spoofing attacks generate unusual ARP packet patterns with larger header sizes, frequent ARP request/response messages, and potential MAC address conflicts. The traffic shows high forward header sizes and burst patterns.



### Key Indicators:

- Fwd Header Size Max > 1.5 (very high compared to other classes)

- Fwd Header Size Min > 1.5 (very high)

- Bwd Header Size Max > 2.0 (very high)

- Flow Pkts Per Sec > 0.3 (high packet rate)

- Short inter-arrival times (burst pattern)




### Feature Value Criteria:
#### Bwd Header Size Max (`bwd_header_size_max`)
- **Classification Rule**: If this value is **> 1.374**, it strongly suggests Arp_Spoofing traffic




#### Bwd Header Size Min (`bwd_header_size_min`)
- **Classification Rule**: If this value is **> 1.529**, it strongly suggests Arp_Spoofing traffic




#### Fwd Header Size Min (`fwd_header_size_min`)
- **Classification Rule**: If this value is **> 1.566**, it strongly suggests Arp_Spoofing traffic




#### Fwd Header Size Max (`fwd_header_size_max`)
- **Classification Rule**: If this value is **> 1.478**, it strongly suggests Arp_Spoofing traffic




#### Flow Pkts Per Sec (`flow_pkts_per_sec`)
- **Classification Rule**: If this value is **> 0.000**, it suggests Arp_Spoofing traffic

- **Classification Rule**: If this value is **> 0.000**, it suggests Arp_Spoofing traffic




#### Bwd Pkts Per Sec (`bwd_pkts_per_sec`)
- **Classification Rule**: If this value is **> 0.000**, it suggests Arp_Spoofing traffic

- **Classification Rule**: If this value is **> 0.000**, it suggests Arp_Spoofing traffic




#### Fwd Pkts Per Sec (`fwd_pkts_per_sec`)
- **Classification Rule**: If this value is **> 0.000**, it suggests Arp_Spoofing traffic





================================================================================
# BotNet_DDOS
================================================================================
## What is BotNet_DDOS?

Botnet DDoS (Distributed Denial of Service) attacks involve multiple compromised devices (bots) coordinated to flood a target with traffic, overwhelming its resources and making it unavailable to legitimate users.



## How does BotNet_DDOS behave?

Botnet DDoS attacks show high packet rates from multiple sources, sustained high traffic volume, coordinated attack patterns, and network saturation. The traffic is typically unidirectional (mostly toward the target).



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



## How does HTTP_Flood behave?

HTTP flood attacks generate excessive HTTP requests, high request rates, connection exhaustion patterns, and typically target port 80/443. The traffic shows high packet counts and request rates.



### Key Indicators:

- High HTTP request rates

- Many connection attempts

- Port 80/443 traffic

- High packet counts




### Feature Value Criteria:
#### Pkts Difference (`pkts_difference`)
- **Classification Rule**: If this value is **< 0.008**, it suggests HTTP_Flood traffic





================================================================================
# ICMP_Flood
================================================================================
## What is ICMP_Flood?

ICMP flood attacks (also known as ping floods) overwhelm a target by sending a large number of ICMP packets, typically ping requests, causing network saturation and denial of service.



## How does ICMP_Flood behave?

ICMP flood attacks feature high ICMP packet rates, ping flood patterns, network saturation attempts, and unidirectional traffic. The traffic shows very high packet rates with ICMP protocol.



### Key Indicators:

- Very high ICMP packet rates

- Ping flood patterns

- Very short inter-arrival times

- Network saturation patterns




### Feature Value Criteria:
#### Bwd Header Size Tot (`bwd_header_size_tot`)
- **Classification Rule**: If this value is **> 0.523**, it strongly suggests ICMP_Flood traffic




#### Fwd Header Size Tot (`fwd_header_size_tot`)
- **Classification Rule**: If this value is **> 0.227**, it strongly suggests ICMP_Flood traffic




#### Resp Pkts (`resp_pkts`)
- **Classification Rule**: If this value is **> 0.882**, it suggests ICMP_Flood traffic




#### Bwd Pkts Payload.Avg (`bwd_pkts_payload.avg`)
- **Classification Rule**: If this value is **> -0.053**, it suggests ICMP_Flood traffic




#### Bwd Pkts Payload.Tot (`bwd_pkts_payload.tot`)
- **Classification Rule**: If this value is **> -0.024**, it suggests ICMP_Flood traffic




#### Orig Pkts (`orig_pkts`)
- **Classification Rule**: If this value is **> 0.406**, it suggests ICMP_Flood traffic





================================================================================
# MQTT_Flood
================================================================================
## What is MQTT_Flood?

MQTT flood attacks target IoT devices using the MQTT protocol by sending excessive publish/subscribe messages, overwhelming the MQTT broker and disrupting IoT communications.



## How does MQTT_Flood behave?

MQTT flood attacks generate excessive MQTT publish/subscribe messages, high message rates, potential broker overload, and target port 1883. The traffic shows high MQTT message rates.



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



## How does Port_Scanning behave?

Port scanning shows connection attempts to multiple ports, sequential port access patterns, reconnaissance behavior, and typically low data transfer. The traffic shows many connection attempts with low success rates.



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



## How does TCP_Flood behave?

TCP flood attacks feature high TCP connection attempts, SYN flood patterns, connection table exhaustion, and incomplete connections. The traffic shows many TCP connection attempts with low completion rates.



### Key Indicators:

- Very high TCP connection attempts

- SYN flood patterns

- Low connection completion

- Many incomplete connections

- Connection table exhaustion





================================================================================
# How to Classify a Flow
================================================================================

## Step-by-Step Classification Process:

1. **Extract Feature Values**
   - Get the following key features from the flow:
     * fwd_header_size_max
     * bwd_header_size_max
     * flow_pkts_per_sec
     * resp_pkts
     * resp_ip_bytes
     * orig_pkts
     * orig_ip_bytes

2. **Apply Classification Rules**
   - Check each class's Key Indicators and Feature Value Criteria above
   - Match the flow's feature values with the rules
   - Find the class that matches best

3. **Decision Priority**
   - First check header sizes (Arp_Spoofing has high header sizes)
   - Then check packet rates (ICMP_Flood has higher rates)
   - Check response packets/bytes (HTTP_Flood has high values)
   - Check for negative values (BotNet_DDOS often has negative packets/bytes)
   - If none match, check Normal patterns

4. **Final Classification**
   - Use the class whose rules match the most features
   - If multiple classes match, use the one with the strongest indicators
