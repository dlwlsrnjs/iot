# Network Traffic Classification Guide - Based on Raw Data Features

This guide uses **raw network traffic features** from the dataset:
- Protocol (proto), Service, Connection State (conn_state)
- IP addresses (id.orig_h, id.resp_h), Ports (id.orig_p, id.resp_p)
- Duration, Packets, Bytes (orig_bytes, resp_bytes, orig_pkts, resp_pkts)


================================================================================
# Normal
================================================================================

## Description:
Normal legitimate network traffic in AG-IoT environment. Regular and lawful communication between devices.

## Raw Data Feature Characteristics:

### Duration:
- **duration**: Values are stable or show predictable patterns according to application needs (e.g., sensor reporting intervals).
- **flow_duration**: Consistent with application requirements.

### Packets/Bytes:
- **orig_bytes, resp_bytes**: Show regular patterns according to specific application protocols (MQTT, CoAP, HTTP).
- **orig_pkts, resp_pkts**: Regular packet counts, no sudden large bursts.
- **fwd_pkts_per_sec, flow_pkts_per_sec**: Packet rate per second is not excessively high and maintains consistent values.

### Protocol:
- **proto**: Expected protocols like 'tcp', 'udp', 'icmp' appear.
- **service**: Expected services like 'mqtt', 'http', 'dns', 'icmp' appear.

### Connection State:
- **conn_state**: For TCP-based flows, mostly 'SF' (normal connection termination) or 'OTH' (other).
- **missed_bytes**: Low or close to 0.

### Port Usage:
- **id.resp_p**: Well-known ports (e.g., MQTT 1883, HTTP 80/443) or application-assigned ports.
- Random port usage is rare.

### Destination:
- **id.resp_h**: Limited to servers, brokers, or other device IPs within the AG-IoT system.

### AG-IoT Characteristics:
- Periodic sensor data reports (temperature, humidity, soil moisture)
- Control signals for irrigation systems, ventilation fans, etc.


## Real Sample Examples:

### Sample 1:
**Source IP**: 192.168.1.4
**Source Port**: 62876
**Destination IP**: 192.168.1.5
**Destination Port**: 1880
**Protocol**: tcp
**Service**: http
**Connection State**: S1
**Duration**: 0.013227
**Origin Packets**: 4
**Origin Bytes**: 182
**Response Packets**: 3
**Response Bytes**: 0
**Flow Packets Per Second**: 7.070379

### Sample 2:
**Source IP**: 192.168.1.11
**Source Port**: 50213
**Destination IP**: 192.168.1.5
**Destination Port**: 1883
**Protocol**: tcp
**Service**: mqtt
**Connection State**: OTH
**Duration**: 4.099793
**Origin Packets**: 14
**Origin Bytes**: 200
**Response Packets**: 12
**Response Bytes**: 120
**Flow Packets Per Second**: 6.683927

### Sample 3:
**Source IP**: 192.168.1.7
**Source Port**: 51319
**Destination IP**: 192.168.1.5
**Destination Port**: 1883
**Protocol**: tcp
**Service**: mqtt
**Connection State**: OTH
**Duration**: 4.261753
**Origin Packets**: 15
**Origin Bytes**: 250
**Response Packets**: 15
**Response Bytes**: 150
**Flow Packets Per Second**: 6.87443

## Typical Feature Value Ranges:

**Protocol Distribution:**
- tcp: 100.0% (9,978 samples)

**Service Distribution:**
- mqtt: 71.7% (7,152 samples)
- http: 13.9% (1,390 samples)

**Connection State Distribution:**
- OTH: 72.1% (7,195 samples)
- SF: 14.0% (1,392 samples)
- S1: 13.9% (1,390 samples)
- RSTRH: 0.0% (1 samples)

**duration**: Median=4.1009, Range=[0.0214, 4.1981]
**orig_pkts**: Median=14.0000, Range=[4.0000, 15.0000]
**orig_bytes**: Median=250.0000, Range=[151.0000, 250.0000]
**resp_pkts**: Median=14.0000, Range=[3.0000, 15.0000]
**resp_bytes**: Median=150.0000, Range=[0.0000, 150.0000]
**flow_pkts_per_sec**: Median=7.3658, Range=[6.9193, 443.2771]


================================================================================
# Arp_Spoofing
================================================================================

## Description:
ARP spoofing attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address.

## Raw Data Feature Characteristics:

### Protocol (Key Indicator):
- **proto**: Overwhelmingly 'arp' (this is the most distinguishing feature).

### Packets/Bytes:
- **orig_pkts, resp_pkts**: Abnormal ARP response packets from a single source MAC within a short time.
- **orig_bytes, resp_bytes**: Low values overall since ARP packets themselves are small.
- **duration**: Short duration but orig_pkts or resp_pkts may be high.

### Connection State:
- **conn_state**: May show 'OTH' (other) or specific ARP-related states.

### Key Indicators:
- **proto = 'arp'** (this is the primary indicator)
- Low bytes but high header sizes (if available)
- Short duration flows

### AG-IoT Impact:
- Threatens communication integrity between devices in farm local network (LAN)
- Can cause sensor data manipulation, control system malfunction


## Real Sample Examples:

### Sample 1:
**Source IP**: 192.168.1.4
**Source Port**: 55408
**Destination IP**: 192.168.1.5
**Destination Port**: 1883
**Protocol**: tcp
**Service**: -
**Connection State**: SHR
**Duration**: -
**Origin Packets**: 0
**Origin Bytes**: -
**Response Packets**: 1
**Response Bytes**: -
**Flow Packets Per Second**: 0.0

### Sample 2:
**Source IP**: 192.168.1.4
**Source Port**: 49367
**Destination IP**: 192.168.1.5
**Destination Port**: 1883
**Protocol**: tcp
**Service**: -
**Connection State**: SHR
**Duration**: -
**Origin Packets**: 0
**Origin Bytes**: -
**Response Packets**: 1
**Response Bytes**: -
**Flow Packets Per Second**: 4987.281807

### Sample 3:
**Source IP**: 192.168.1.4
**Source Port**: 62314
**Destination IP**: 192.168.1.5
**Destination Port**: 1883
**Protocol**: tcp
**Service**: -
**Connection State**: SHR
**Duration**: -
**Origin Packets**: 0
**Origin Bytes**: -
**Response Packets**: 1
**Response Bytes**: -
**Flow Packets Per Second**: 32.638297

## Typical Feature Value Ranges:

**Protocol Distribution:**
- tcp: 100.0% (26 samples)

**Service Distribution:**

**Connection State Distribution:**
- SHR: 80.8% (21 samples)
- RSTO: 11.5% (3 samples)
- OTH: 7.7% (2 samples)

**duration**: Median=1.6874, Range=[1.3574, 3.2442]
**orig_pkts**: Median=0.0000, Range=[0.0000, 0.0000]
**orig_bytes**: Median=0.0000, Range=[0.0000, 0.0000]
**resp_pkts**: Median=1.0000, Range=[1.0000, 2.0000]
**resp_bytes**: Median=0.0000, Range=[0.0000, 0.0000]
**flow_pkts_per_sec**: Median=0.0000, Range=[0.0000, 16.5018]


================================================================================
# HTTP_Flood
================================================================================

## Description:
Denial of Service attack that overwhelms a web server by sending excessive HTTP requests (GET/POST).

## Raw Data Feature Characteristics:

### Protocol:
- **proto**: 'tcp'
- **id.resp_p**: Destination port is 80 or 443
- **service**: May show 'http'

### Packets/Bytes:
- **orig_bytes, orig_pkts**: Abnormally surge within a short time directed at specific **id.resp_h** (web server IP).
- **fwd_pkts_per_sec, flow_pkts_per_sec**: High packet rate.

### Request Pattern:
- **orig_pkts** vs **resp_pkts**: Low ratio of resp_pkts to orig_pkts.
- **duration**: Very short duration flows repeatedly from same **id.orig_h** to same **id.resp_h** on specific port.

### Connection State:
- **conn_state**: May show 'S1', 'S0' (incomplete connections) or 'SF' (if connections complete).

### Key Indicators:
- **proto = 'tcp'** AND **id.resp_p = 80 or 443** AND **service = 'http'**
- High **orig_pkts, orig_bytes** directed at web server
- Short **duration** with high packet rate

### AG-IoT Impact:
- Causes access failure to smart farm web interfaces, data visualization dashboards, remote control web applications


## Real Sample Examples:

### Sample 1:
**Source IP**: 192.168.1.4
**Source Port**: 43016
**Destination IP**: 192.168.1.5
**Destination Port**: 1880
**Protocol**: tcp
**Service**: -
**Connection State**: OTH
**Duration**: 0.000041
**Origin Packets**: 1
**Origin Bytes**: 10351
**Response Packets**: 1
**Response Bytes**: 0
**Flow Packets Per Second**: 54.868565

### Sample 2:
**Source IP**: 192.168.1.4
**Source Port**: 34226
**Destination IP**: 192.168.1.5
**Destination Port**: 1880
**Protocol**: tcp
**Service**: -
**Connection State**: OTH
**Duration**: 0.000131
**Origin Packets**: 1
**Origin Bytes**: 185
**Response Packets**: 1
**Response Bytes**: 0
**Flow Packets Per Second**: 90200.086022

### Sample 3:
**Source IP**: 192.168.1.4
**Source Port**: 44234
**Destination IP**: 192.168.1.5
**Destination Port**: 1880
**Protocol**: tcp
**Service**: -
**Connection State**: OTH
**Duration**: 0.000022
**Origin Packets**: 1
**Origin Bytes**: 15
**Response Packets**: 1
**Response Bytes**: 0
**Flow Packets Per Second**: 9.312046

## Typical Feature Value Ranges:

**Protocol Distribution:**
- tcp: 100.0% (81,551 samples)

**Service Distribution:**
- http: 21.4% (17,416 samples)

**Connection State Distribution:**
- OTH: 62.1% (50,627 samples)
- S1: 23.0% (18,780 samples)
- SF: 9.5% (7,759 samples)
- RSTO: 3.6% (2,943 samples)
- SH: 0.9% (773 samples)

**duration**: Median=0.0145, Range=[0.0000, 0.5398]
**orig_pkts**: Median=2.0000, Range=[1.0000, 3.0000]
**orig_bytes**: Median=169.0000, Range=[9.0000, 406.0000]
**resp_pkts**: Median=1.0000, Range=[1.0000, 2.0000]
**resp_bytes**: Median=0.0000, Range=[0.0000, 0.0000]
**flow_pkts_per_sec**: Median=6579.3004, Range=[12.3462, 76959.7064]


================================================================================
# Port_Scanning
================================================================================

## Description:
Activity to find open ports on hosts by attempting sequential or random port connections.

## Raw Data Feature Characteristics:

### Destination Port:
- **id.resp_p**: Multiple different destination ports from single **id.orig_h** (source IP) to same **id.resp_h** (target IP) within a short time.
- Sequential or random port connection attempts.

### Packet Characteristics (SYN Scan, etc.):
- **proto**: 'tcp' for TCP-based scans
- **conn_state**: Many 'S0' (SYN_SENT), 'S1' (SYN_RECV) states - incomplete connection states.
- **orig_pkts**: High, but **resp_pkts** is low.
- **duration**: Very short duration flows are predominant.

### Bytes:
- **orig_bytes, resp_bytes**: Low values overall since port scanning itself does not transmit much data.

### Key Indicators:
- Multiple flows from same **id.orig_h** to same **id.resp_h** with different **id.resp_p** values
- **conn_state** showing 'S0', 'S1' (incomplete connections)
- Short **duration**, low bytes

### AG-IoT Impact:
- Used to identify vulnerabilities in AG-IoT devices (sensors, controllers), servers, network devices
- Serves as a stepping stone for future attacks


## Real Sample Examples:

### Sample 1:
**Source IP**: 192.168.1.20
**Source Port**: 42933
**Destination IP**: 192.168.1.5
**Destination Port**: 902
**Protocol**: tcp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 17367.718427

### Sample 2:
**Source IP**: 192.168.1.20
**Source Port**: 42933
**Destination IP**: 192.168.1.5
**Destination Port**: 2111
**Protocol**: tcp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 14388.692967

### Sample 3:
**Source IP**: 192.168.1.20
**Source Port**: 42933
**Destination IP**: 192.168.1.5
**Destination Port**: 13782
**Protocol**: tcp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 5.38998

## Typical Feature Value Ranges:

**Protocol Distribution:**
- tcp: 100.0% (222 samples)

**Service Distribution:**

**Connection State Distribution:**
- S0: 100.0% (222 samples)

**orig_pkts**: Median=1.0000, Range=[1.0000, 1.0000]
**resp_pkts**: Median=0.0000, Range=[0.0000, 0.0000]
**flow_pkts_per_sec**: Median=14652.6910, Range=[4108.6202, 20648.9047]


================================================================================
# UDP_Flood
================================================================================

## Description:
Denial of Service attack that sends massive UDP packets to exhaust server resources.

## Raw Data Feature Characteristics:

### Protocol:
- **proto**: 'udp'

### Packets/Bytes:
- **orig_pkts, orig_bytes**: Abnormally explosive increase within a short time directed at target **id.resp_h**.
- **flow_pkts_per_sec**: Very high packet rate.

### Port Usage:
- **id.resp_p**: May concentrate on single port, or appear on random wide range of ports.

### Response Characteristics:
- **resp_pkts, resp_bytes**: Significantly lower than orig_pkts/orig_bytes, or close to 0.

### Duration:
- **duration, flow_duration**: Very high frequency UDP packets occur continuously during the attack.

### Key Indicators:
- **proto = 'udp'**
- High **orig_pkts** but low **resp_pkts**
- High packet rate

### AG-IoT Impact:
- Paralyzes DNS servers, NTP servers, or specific UDP-based IoT services in agricultural infrastructure
- Causes failures in sensor data transmission, time synchronization, etc.


## Real Sample Examples:

### Sample 1:
**Source IP**: 192.168.1.9
**Source Port**: 57359
**Destination IP**: 192.168.1.5
**Destination Port**: 5683
**Protocol**: udp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 0.0

### Sample 2:
**Source IP**: 192.168.1.9
**Source Port**: 65020
**Destination IP**: 192.168.1.5
**Destination Port**: 5683
**Protocol**: udp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 0.0

### Sample 3:
**Source IP**: 192.168.1.9
**Source Port**: 7240
**Destination IP**: 192.168.1.5
**Destination Port**: 5683
**Protocol**: udp
**Service**: -
**Connection State**: S0
**Duration**: -
**Origin Packets**: 1
**Origin Bytes**: -
**Response Packets**: 0
**Response Bytes**: -
**Flow Packets Per Second**: 0.0

## Typical Feature Value Ranges:

**Protocol Distribution:**
- udp: 100.0% (8,223 samples)

**Service Distribution:**

**Connection State Distribution:**
- S0: 100.0% (8,223 samples)

**duration**: Median=1.2620, Range=[0.9553, 1.9710]
**orig_pkts**: Median=1.0000, Range=[1.0000, 1.0000]
**orig_bytes**: Median=0.0000, Range=[0.0000, 0.0000]
**resp_pkts**: Median=0.0000, Range=[0.0000, 0.0000]
**resp_bytes**: Median=0.0000, Range=[0.0000, 0.0000]
**flow_pkts_per_sec**: Median=0.0000, Range=[0.0000, 0.0000]
