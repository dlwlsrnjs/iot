# Network Traffic Classification - Explicit Rules

This guide provides **explicit IF-THEN rules** for each class.
Follow these rules exactly when classifying flows.


================================================================================
# Arp_Spoofing
================================================================================
## What is Arp_Spoofing?

ARP spoofing is an attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address, causing network disruption.

## Real Sample Examples:

### Arp_Spoofing Sample 1:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000047
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### Arp_Spoofing Sample 2:
**Flow**: Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 2.350975
- Backward Header Size Max: 3.183240
- Flow Packets Per Second: 0.000036
- Response Packets: 0.882229
- Response IP Bytes: 1.503448

## Classification Rule:

**IF** the flow matches the following conditions, **THEN** classify it as **Arp_Spoofing**:

**IF** Forward Header Size Max > 1.4782 **AND** Backward Header Size Max > 1.3745
**THEN** classify as **Arp_Spoofing**

**OR**

**IF** the flow's feature values are similar to the Arp_Spoofing samples above
**THEN** classify as **Arp_Spoofing**

## Typical Value Ranges:

- **Forward Header Size Max**: Median=2.3510, Range=[1.4782, 2.3510]
- **Backward Header Size Max**: Median=2.4597, Range=[1.3745, 3.1832]
- **Flow Packets Per Second**: Median=0.1440, Range=[0.0002, 0.6649]
- **Response Packets**: Median=0.8822, Range=[0.8822, 0.8822]
- **Response IP Bytes**: Median=1.5034, Range=[1.0326, 1.5034]


================================================================================
# BotNet_DDOS
================================================================================
## What is BotNet_DDOS?

BotNet DDoS is a distributed denial-of-service attack launched by a botnet, showing coordinated attack patterns from multiple compromised devices.

## Real Sample Examples:

### BotNet_DDOS Sample 1:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

### BotNet_DDOS Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

## Classification Rule:

**IF** the flow matches the following conditions, **THEN** classify it as **BotNet_DDOS**:

**IF** Flow Packets Per Second ≈ 0.0 **AND** Response Packets < 0 (negative)
**THEN** classify as **BotNet_DDOS**

**OR**

**IF** the flow's feature values match the BotNet_DDOS samples above (Flow Pkts/Sec ≈ 0.0, negative packet values)
**THEN** classify as **BotNet_DDOS**

## Typical Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, -0.4342]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, -0.5003]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, -0.5368]


================================================================================
# HTTP_Flood
================================================================================
## What is HTTP_Flood?

HTTP flood is an attack that overwhelms a web server by sending excessive HTTP requests, exhausting server resources.

## Real Sample Examples:

### HTTP_Flood Sample 1:
**Flow**: Total packets: 3 (0 origin, 2 response). Total bytes: 3 (0 origin, 3 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: -0.434242
- Flow Packets Per Second: 0.000000
- Response Packets: 2.264751
- Response IP Bytes: 2.915949

### HTTP_Flood Sample 2:
**Flow**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: -2.013114
- Backward Header Size Max: 1.736247
- Flow Packets Per Second: 0.000000
- Response Packets: -0.500293
- Response IP Bytes: -0.536830

## Classification Rule:

**IF** the flow matches the following conditions, **THEN** classify it as **HTTP_Flood**:

**IF** the flow's feature values are similar to the HTTP_Flood samples above
**THEN** classify as **HTTP_Flood**

(Compare Response Packets and Response IP Bytes with samples)

## Typical Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Backward Header Size Max**: Median=-0.4342, Range=[-0.4342, 1.7362]
- **Flow Packets Per Second**: Median=0.0000, Range=[0.0000, 0.0000]
- **Response Packets**: Median=-0.5003, Range=[-0.5003, 0.8822]
- **Response IP Bytes**: Median=-0.5368, Range=[-0.5368, 1.1896]


================================================================================
# ICMP_Flood
================================================================================
## What is ICMP_Flood?

ICMP flood is an attack that floods the target with ICMP packets (ping flood), causing network saturation.

## Real Sample Examples:

### ICMP_Flood Sample 1:
**Flow**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.09 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166099s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.087822
- Response Packets: 0.882229
- Response IP Bytes: 1.032615

### ICMP_Flood Sample 2:
**Flow**: Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.
**Key Values:**
- Forward Header Size Max: 0.168930
- Backward Header Size Max: 1.374499
- Flow Packets Per Second: 0.000086
- Response Packets: 3.647273
- Response IP Bytes: 4.328450

## Classification Rule:

**IF** the flow matches the following conditions, **THEN** classify it as **ICMP_Flood**:

**IF** Flow Packets Per Second > 0.009119 **OR** values match ICMP_Flood samples above
**THEN** classify as **ICMP_Flood**

## Typical Value Ranges:

- **Forward Header Size Max**: Median=0.1689, Range=[0.1689, 0.6053]
- **Backward Header Size Max**: Median=1.3745, Range=[1.3745, 1.7362]
- **Flow Packets Per Second**: Median=0.0008, Range=[0.0001, 0.0091]
- **Response Packets**: Median=0.8822, Range=[0.8822, 3.6473]
- **Response IP Bytes**: Median=1.0326, Range=[1.0326, 4.3284]


================================================================================
# Complete Classification Process
================================================================================

## Step-by-Step Classification:

1. **Extract feature values** from the flow:
   - Forward Header Size Max
   - Backward Header Size Max
   - Flow Packets Per Second
   - Response Packets
   - Response IP Bytes

2. **Check each class's IF-THEN rule** above:
   - Start with Arp_Spoofing: IF Fwd Header Max > 1.4782 AND Bwd Header Max > 1.3745 → Arp_Spoofing
   - Check BotNet_DDOS: IF Flow Pkts/Sec ≈ 0.0 AND Resp Pkts < 0 → BotNet_DDOS
   - Check other classes: Compare with samples
   - If none match → Normal

3. **Compare with actual samples**:
   - Look at the sample values for each class
   - Find which class's samples match your flow's values best

4. **Classify**:
   - Use the class whose IF-THEN conditions are satisfied
   - Or the class whose samples match best
