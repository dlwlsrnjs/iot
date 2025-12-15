# Network Traffic Classification Guide - Based on Actual Dataset Features

**IMPORTANT**: This dataset contains **normalized numerical features** extracted from raw network traffic.
The original raw features (proto, conn_state, IP addresses, ports) are not directly available.
Instead, statistical features derived from network flows are used.


================================================================================
# Arp_Spoofing
================================================================================

## Description:
ARP spoofing attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address.

## Actual Dataset Feature Characteristics:

### Header Sizes (Key Indicator):
- **fwd_header_size_max**: High values (typically > 1.4782, median ≈ 2.35)
- **bwd_header_size_max**: High values (typically > 1.3745, median ≈ 2.46)
- This is the **most distinguishing feature** for Arp_Spoofing.

### Packets/Bytes:
- **orig_pkts, resp_pkts**: May show abnormal patterns (short duration but high packet counts).
- **orig_ip_bytes, resp_ip_bytes**: Low values overall since ARP packets themselves are small.

### Packet Rate:
- **flow_pkts_per_sec**: Low packet rate (median ≈ 0.14, but can be very low ≈ 0.0).

### Key Indicators:
- **fwd_header_size_max > 1.4782** AND **bwd_header_size_max > 1.3745**
- Low packet rate but high header sizes
- This combination is unique to Arp_Spoofing

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
- Origin Packets: -0.067784
- Origin IP Bytes: -0.081724
- Forward Packets Per Second: 0.000039
- Missed Bytes: 0.000000
- Packets Difference: 0.007966

### Sample 2:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000036
- Response Packets: 0.882229
- Response IP Bytes: 1.503448
- Origin Packets: -0.067784
- Origin IP Bytes: 2.306590
- Forward Packets Per Second: 0.000030
- Missed Bytes: 0.000000
- Packets Difference: 0.007966

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=2.3510, Range=[1.4782, 2.3510]
- **Backward Header Size Max**: Median=2.4597, Range=[1.3745, 3.1832]
- **Flow Packets Per Second**: Median=0.1440, Range=[0.0002, 0.6649]
- **Response Packets**: Median=0.8822, Range=[0.8822, 0.8822]
- **Response IP Bytes**: Median=1.5034, Range=[1.0326, 1.5034]
- **Origin Packets**: Median=-0.0678, Range=[-0.0678, -0.0678]
- **Origin IP Bytes**: Median=-0.0622, Range=[-0.0817, 2.6770]
- **Forward Packets Per Second**: Median=0.1065, Range=[0.0002, 0.4894]
- **Missed Bytes**: Median=0.0000, Range=[0.0000, 0.0000]
- **Packets Difference**: Median=-0.0435, Range=[-0.0435, -0.0435]


================================================================================
# BotNet_DDOS
================================================================================

## Description:
Distributed Denial of Service attack using a botnet of multiple infected computers to flood a target server or device.

## Actual Dataset Feature Characteristics:

### Packet Rate (Key Indicator):
- **flow_pkts_per_sec**: Very low (≈ 0.0, median = 0.0000) - indicates incomplete or failed connections.
- **fwd_pkts_per_sec**: Very low (≈ 0.0).

### Response Packets (Key Indicator):
- **resp_pkts**: Negative values (median ≈ -0.50) - abnormal pattern indicating failed connections.
- **resp_ip_bytes**: Negative values (median ≈ -0.54).

### Header Sizes:
- **fwd_header_size_max**: Low values (typically ≈ 0.17, much lower than Arp_Spoofing).
- **bwd_header_size_max**: Negative values (typically ≈ -0.43).

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
- Origin Packets: -0.067784
- Origin IP Bytes: -0.276688
- Forward Packets Per Second: 0.000000
- Missed Bytes: 0.000000
- Packets Difference: 0.007966

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830
- Origin Packets: -0.067784
- Origin IP Bytes: -0.276688
- Forward Packets Per Second: 0.000000
- Missed Bytes: 0.000000
- Packets Difference: 0.007966

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, -0.4342]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, -0.5003]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, -0.5368]
- **Origin Packets**: Median=-0.0678, Range=[-0.0678, -0.0678]
- **Origin IP Bytes**: Median=-0.2767, Range=[-0.2767, -0.2767]
- **Forward Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Missed Bytes**: Median=0.0000, Range=[0.0000, 0.0000]
- **Packets Difference**: Median=0.0080, Range=[0.0080, 0.0080]


================================================================================
# HTTP_Flood
================================================================================

## Description:
Denial of Service attack that overwhelms a web server by sending excessive HTTP requests (GET/POST).

## Actual Dataset Feature Characteristics:

### Header Sizes:
- **fwd_header_size_max**: Low values (typically ≈ 0.17, much lower than Arp_Spoofing).
- **bwd_header_size_max**: May vary (range: -0.43 to 1.74).

### Response Packets/Bytes:
- **resp_pkts**: May vary significantly (range: -0.50 to 0.88, some samples show high values like 2.26).
- **resp_ip_bytes**: May vary (range: -0.54 to 1.19, some samples show high values like 2.92).

### Packet Rate:
- **flow_pkts_per_sec**: Very low (≈ 0.0, median = 0.0000).

### Key Indicators:
- **fwd_header_size_max < 1.4782** (low, typically ≈ 0.17)
- **resp_pkts** may vary: some samples show high values (2.26), others show negative (-0.50)
- **resp_ip_bytes** may vary: some samples show high values (2.92), others show negative (-0.54)
- Compare with actual samples to identify patterns

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
- Origin Packets: 0.405725
- Origin IP Bytes: 0.113241
- Forward Packets Per Second: 0.000000
- Missed Bytes: 0.266985
- Packets Difference: 0.007966

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: -2.013114
- Backward Header Size Max: 1.736247
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830
- Origin Packets: -0.067784
- Origin IP Bytes: -0.276688
- Forward Packets Per Second: 0.000000
- Missed Bytes: 0.000000
- Packets Difference: -0.094890

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, 1.7362]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, 0.8822]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, 1.1896]
- **Origin Packets**: Median=-0.0678, Range=[-0.0678, -0.0678]
- **Origin IP Bytes**: Median=-0.2767, Range=[-0.2767, -0.2767]
- **Forward Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Missed Bytes**: Median=0.0000, Range=[0.0000, 0.0000]
- **Packets Difference**: Median=0.0080, Range=[-0.0435, 0.0080]


================================================================================
# ICMP_Flood
================================================================================

## Description:
Denial of Service attack that floods the target with ICMP packets (mainly Echo Request, "ping").

## Actual Dataset Feature Characteristics:

### Packet Rate (Key Indicator):
- **flow_pkts_per_sec**: May be higher than other classes (median ≈ 0.0008, q75 ≈ 0.0091).
- Some samples show higher packet rates (up to 0.14).

### Header Sizes:
- **fwd_header_size_max**: Low values (typically ≈ 0.17, range: 0.17 to 0.61).
- **bwd_header_size_max**: Moderate values (typically 1.37 to 1.74).

### Response Packets/Bytes:
- **resp_pkts**: May vary (median ≈ 0.88, range: 0.88 to 3.65).
- **resp_ip_bytes**: May vary (median ≈ 1.03, range: 1.03 to 4.33).

### Key Indicators:
- **flow_pkts_per_sec > 0.0091** (higher than other classes in some samples)
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
- Origin Packets: 0.405725
- Origin IP Bytes: 0.113241
- Forward Packets Per Second: 0.086183
- Missed Bytes: 0.000000
- Packets Difference: 0.007966

### Sample 2:
**Flow**: Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.
**Key Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.000086
- Response Packets: 3.647273
- Response IP Bytes: 4.328450
- Origin Packets: 1.352744
- Origin IP Bytes: 2.696519
- Forward Packets Per Second: 0.000068
- Missed Bytes: 0.000000
- Packets Difference: 0.059394

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.6053]
- **Backward Header Size Max**: Median=1.3745, Range=[1.3745, 1.7362]
- **Flow Packets Per Second**: Median=0.0008, Range=[0.0001, 0.0091]
- **Response Packets**: Median=0.8822, Range=[0.8822, 3.6473]
- **Response IP Bytes**: Median=1.0326, Range=[1.0326, 4.3284]
- **Origin Packets**: Median=0.4057, Range=[0.4057, 1.3527]
- **Origin IP Bytes**: Median=0.1132, Range=[0.1132, 2.6965]
- **Forward Packets Per Second**: Median=0.0006, Range=[0.0001, 0.0071]
- **Missed Bytes**: Median=0.0000, Range=[0.0000, 0.0000]
- **Packets Difference**: Median=-0.0435, Range=[-0.0435, 0.0080]
