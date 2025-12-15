# Network Traffic Classification Guide - Dataset Feature Based

This guide explains how each attack type manifests in the dataset features.


================================================================================
# Arp_Spoofing
================================================================================

## Description:
ARP spoofing attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address, causing Man-in-the-Middle (MITM) attacks.

## Dataset Feature Characteristics:

### Protocol:
- **proto**: Overwhelmingly 'arp'.

### Packet Characteristics (Abnormal ARP Response/MAC-IP Mismatch):
- **total_fwd_packets, total_backward_packets**: Abnormal ARP response packets from a single source MAC within a short time.
- **flow_duration**: Short duration but orig_pkts or resp_pkts may be high.
- **fwd_header_size_max, bwd_header_size_max**: High header sizes (typically > 1.4 for forward, > 1.3 for backward).

### Bytes:
- **total_length_of_fwd_packets, total_length_of_bwd_packets**: Low values overall since ARP packets themselves are small.

### Key Indicators:
- **fwd_header_size_max > 1.4782** AND **bwd_header_size_max > 1.3745**
- Low packet rate but high header sizes
- Short duration flows

### AG-IoT Impact:
- Threatens communication integrity between devices in farm local network (LAN)
- Can cause sensor data manipulation, control system malfunction


## Real Sample Examples:

### Sample 1:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000047
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### Sample 2:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000036
- Response Packets: 0.882229
- Response IP Bytes: 1.503448

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=2.3510, Range=[1.4782, 2.3510]
- **Backward Header Size Max**: Median=2.4597, Range=[1.3745, 3.1832]
- **Flow Packets Per Second**: Median=0.1440, Range=[0.0002, 0.6649]
- **Response Packets**: Median=0.8822, Range=[0.8822, 0.8822]
- **Response IP Bytes**: Median=1.5034, Range=[1.0326, 1.5034]


================================================================================
# BotNet_DDOS
================================================================================

## Description:
Distributed Denial of Service attack using a botnet of multiple infected computers to flood a target server or device with massive traffic.

## Dataset Feature Characteristics:

### Source IP:
- **id.orig_h**: Multiple unique source IPs targeting the same **id.resp_h** (distributed attack pattern).
- This characteristic is visible when examining multiple samples together, not a single sample.

### Packets/Bytes:
- **total_length_of_fwd_packets, total_fwd_packets**: Abnormally high values directed at target IP (**id.resp_h**).
- **flow_pkts_per_sec**: Very low (≈ 0.0) - indicates incomplete or failed connections.
- **fwd_pkts_per_sec**: Abnormally high packet rate.

### Protocol:
- **proto**: Various protocols ('tcp', 'udp', 'icmp') appear with high frequency simultaneously.

### Connection State:
- **conn_state**: For TCP-based flows, many 'S0', 'S1' states (connection failures or incomplete connection attempts).
- **missed_bytes, pkts_difference**: May have high values.

### Duration:
- **flow_duration**: High traffic volume maintained as many flows occur simultaneously during the attack.

### Key Indicators:
- **flow_pkts_per_sec ≈ 0.0** AND **resp_pkts < 0** (negative)
- **fwd_header_size_max < 1.4782** (low, typically ≈ 0.17)
- **bwd_header_size_max < 0** (negative)

### AG-IoT Impact:
- Causes severe disruption to real-time monitoring and automatic control systems
- Paralyzes agricultural data servers, irrigation system control servers


## Real Sample Examples:

### Sample 1:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, -0.4342]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, -0.5003]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, -0.5368]


================================================================================
# HTTP_Flood
================================================================================

## Description:
Denial of Service attack that overwhelms a web server by sending excessive HTTP requests (GET/POST), exhausting server resources.

## Dataset Feature Characteristics:

### Protocol:
- **proto**: 'tcp'
- **id.resp_p**: Destination port is 80 or 443
- **service**: May show 'http'

### Packets/Bytes:
- **total_length_of_fwd_packets, total_fwd_packets**: Abnormally surge within a short time directed at specific **id.resp_h** (web server IP).
- **flow_pkts_per_sec**: High packet rate.
- **fwd_pkts_per_sec**: Abnormally high.

### Request Pattern:
- **total_fwd_packets** vs **total_backward_packets**: Low ratio of resp_pkts to orig_pkts.
- **flow_duration**: Very short duration flows repeatedly from same **id.orig_h** to same **id.resp_h** on specific port.

### Key Indicators:
- **fwd_header_size_max < 1.4782** (low, typically ≈ 0.17)
- **resp_pkts** may vary: some samples show high values (2.26), others show negative (-0.50)
- **resp_ip_bytes** may vary: some samples show high values (2.92), others show negative (-0.54)

### AG-IoT Impact:
- Causes access failure to smart farm web interfaces, data visualization dashboards, remote control web applications


## Real Sample Examples:

### Sample 1:
**Flow**: Total packets: 3 (0 origin, 2 response). Total bytes: 3 (0 origin, 3 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: 2.264751
- Response IP Bytes: 2.915949

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: -2.013114
- Backward Header Size Max: 1.736247
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, 1.7362]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, 0.8822]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, 1.1896]


================================================================================
# ICMP_Flood
================================================================================

## Description:
Denial of Service attack that floods the target with ICMP packets (mainly Echo Request, "ping"), consuming bandwidth and exhausting resources.

## Dataset Feature Characteristics:

### Protocol:
- **proto**: 'icmp'

### Packets/Bytes:
- **total_fwd_packets, total_length_of_fwd_packets**: Abnormally high values directed at target **id.resp_h** within a short time.
- **flow_pkts_per_sec**: May be higher than other classes (median ≈ 0.0008, q75 ≈ 0.0091).
- **fwd_pkts_per_sec**: Abnormally high packet rate.

### Response Characteristics:
- **total_backward_packets, total_length_of_bwd_packets**: Significantly lower than orig_pkts/orig_bytes, or close to 0.
- Target system fails to send ICMP Echo Reply properly due to overload.

### Duration:
- **flow_duration**: Very high frequency ICMP packets occur continuously during the attack.

### Packet Size:
- Large ICMP packets may be used to maximize bandwidth consumption.

### Key Indicators:
- **flow_pkts_per_sec > 0.0091** (higher than other classes)
- **fwd_header_size_max < 1.4782** (low, typically ≈ 0.17)
- **bwd_header_size_max**: Typically 1.37-1.74 range

### AG-IoT Impact:
- Paralyzes network devices (routers, switches) or servers in the farm
- Disrupts communication of entire AG-IoT system


## Real Sample Examples:

### Sample 1:
**Flow**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.09 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166099s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.087822
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### Sample 2:
**Flow**: Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.000086
- Response Packets: 3.647273
- Response IP Bytes: 4.328450

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.6053]
- **Backward Header Size Max**: Median=1.3745, Range=[1.3745, 1.7362]
- **Flow Packets Per Second**: Median=0.0008, Range=[0.0001, 0.0091]
- **Response Packets**: Median=0.8822, Range=[0.8822, 3.6473]
- **Response IP Bytes**: Median=1.0326, Range=[1.0326, 4.3284]
