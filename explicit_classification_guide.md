# Network Traffic Classification Guide

This guide explains **what each class is** and **when to classify a flow as that class**.


================================================================================
# Arp_Spoofing
================================================================================
## What is Arp_Spoofing?

ARP spoofing is an attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address.

## Actual Sample Examples:

Here are **real samples** from the dataset:

### Sample 1:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000047
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### Sample 2:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000036
- Response Packets: 0.882229
- Response IP Bytes: 1.503448

### Sample 3:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.08 packets/second. Balanced bidirectional traffic: ratio 0.17. Very short inter-arrival time: -0.167218s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.082291
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

## When to Classify as Arp_Spoofing:

**Classify a flow as Arp_Spoofing if it matches the following conditions:**

1. **Forward Header Size Max > 1.4782** (typical: 2.3510)
2. **Backward Header Size Max > 1.3745** (typical: 2.4597)
3. Compare with the actual samples above - if your flow's values are similar to Arp_Spoofing samples, classify as Arp_Spoofing

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=2.3510, 25-75% Range=[1.4782, 2.3510]
- **Backward Header Size Max**: Median=2.4597, 25-75% Range=[1.3745, 3.1832]
- **Flow Packets Per Second**: Median=0.1440, 25-75% Range=[0.0002, 0.6649]
- **Response Packets**: Median=0.8822, 25-75% Range=[0.8822, 0.8822]
- **Response IP Bytes**: Median=1.5034, 25-75% Range=[1.0326, 1.5034]


================================================================================
# BotNet_DDOS
================================================================================
## What is BotNet_DDOS?

BotNet DDoS is a distributed denial-of-service attack launched by a botnet, showing coordinated attack patterns from multiple sources.

## Actual Sample Examples:

Here are **real samples** from the dataset:

### Sample 1:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

### Sample 3:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

## When to Classify as BotNet_DDOS:

**Classify a flow as BotNet_DDOS if it matches the following conditions:**

1. **Flow Packets Per Second ≈ 0.0** (typical: 0.000000)
2. **Response Packets is negative** (typical: -0.5003)
3. Compare with the actual samples above - if your flow's values match BotNet_DDOS samples, classify as BotNet_DDOS

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, 25-75% Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, 25-75% Range=[-0.4342, -0.4342]
- **Flow Packets Per Second**: Median=0.0000, 25-75% Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, 25-75% Range=[-0.5003, -0.5003]
- **Response IP Bytes**: Median=-0.5368, 25-75% Range=[-0.5368, -0.5368]


================================================================================
# HTTP_Flood
================================================================================
## What is HTTP_Flood?

HTTP flood is an attack that overwhelms a web server by sending excessive HTTP requests.

## Actual Sample Examples:

Here are **real samples** from the dataset:

### Sample 1:
**Flow**: Total packets: 3 (0 origin, 2 response). Total bytes: 3 (0 origin, 3 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: 2.264751
- Response IP Bytes: 2.915949

### Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: -2.013114
- Backward Header Size Max: 1.736247
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

### Sample 3:
**Flow**: Total packets: 0 (-1 origin, 1 response). Total bytes: 1 (-1 origin, 1 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: -2.013114
- Backward Header Size Max: 1.736247
- Flow Packets Per Second: 0.000000
- Response Packets: 0.882229
- Response IP Bytes: 1.189559

## When to Classify as HTTP_Flood:

**Classify a flow as HTTP_Flood if it matches the following conditions:**

1. Check Response Packets value (typical: -0.5003)
2. Check Response IP Bytes value (typical: -0.5368)
3. Compare with the actual samples above - if your flow's values match HTTP_Flood samples, classify as HTTP_Flood

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, 25-75% Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, 25-75% Range=[-0.4342, 1.7362]
- **Flow Packets Per Second**: Median=0.0000, 25-75% Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, 25-75% Range=[-0.5003, 0.8822]
- **Response IP Bytes**: Median=-0.5368, 25-75% Range=[-0.5368, 1.1896]


================================================================================
# ICMP_Flood
================================================================================
## What is ICMP_Flood?

ICMP flood is an attack that floods the target with ICMP packets (ping flood).

## Actual Sample Examples:

Here are **real samples** from the dataset:

### Sample 1:
**Flow**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.09 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166099s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.087822
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### Sample 2:
**Flow**: Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.000086
- Response Packets: 3.647273
- Response IP Bytes: 4.328450

### Sample 3:
**Flow**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.14 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166259s (burst traffic pattern). Small payload: -0 bytes.
**Feature Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.135477
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

## When to Classify as ICMP_Flood:

**Classify a flow as ICMP_Flood if it matches the following conditions:**

1. **Flow Packets Per Second** may be higher than other classes (typical: 0.000807, range up to 0.009119)
2. Compare with the actual samples above - if your flow's values match ICMP_Flood samples, classify as ICMP_Flood

## Typical Feature Value Ranges:

- **Forward Header Size Max**: Median=0.1689, 25-75% Range=[0.1689, 0.6053]
- **Backward Header Size Max**: Median=1.3745, 25-75% Range=[1.3745, 1.7362]
- **Flow Packets Per Second**: Median=0.0008, 25-75% Range=[0.0001, 0.0091]
- **Response Packets**: Median=0.8822, 25-75% Range=[0.8822, 3.6473]
- **Response IP Bytes**: Median=1.0326, 25-75% Range=[1.0326, 4.3284]


================================================================================
# Complete Classification Instructions
================================================================================

## For Each Class:

1. **Normal**: Balanced traffic, moderate values → Classify as Normal
2. **Arp_Spoofing**: High header sizes (Fwd > 1.4, Bwd > 1.3) → Classify as Arp_Spoofing
3. **BotNet_DDOS**: Very low packet rate (≈ 0.0) and negative packet values → Classify as BotNet_DDOS
4. **HTTP_Flood**: Check samples above, compare values → Classify as HTTP_Flood if similar
5. **ICMP_Flood**: Check samples above, compare values → Classify as ICMP_Flood if similar
6. **MQTT_Flood**: Check samples above, compare values → Classify as MQTT_Flood if similar
7. **Port_Scanning**: Check samples above, compare values → Classify as Port_Scanning if similar
8. **TCP_Flood**: Check samples above, compare values → Classify as TCP_Flood if similar
9. **UDP_Flood**: Check samples above, compare values → Classify as UDP_Flood if similar

## Classification Process:

1. Extract feature values from the flow
2. For each class, check the "When to Classify" conditions above
3. Compare with actual samples
4. Select the class that matches best
