# Network Traffic Classification - Compare with Actual Samples

**IMPORTANT**: This guide contains **real samples from the dataset**.
When classifying a flow, **directly compare** its feature values with the sample values below.


================================================================================
# Arp_Spoofing
================================================================================

**Dataset Count**: 57,611 samples

## Real Samples from Dataset:

Compare your flow with these **actual Arp_Spoofing samples**:

### Arp_Spoofing Sample 1:

**Description**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 2.350975
- Bwd Header Max: 3.183240
- Flow Pkts/Sec: 0.000047
- Resp Pkts: 0.882229
- Resp Bytes: 1.032615

### Arp_Spoofing Sample 2:

**Description**: Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 2.350975
- Bwd Header Max: 3.183240
- Flow Pkts/Sec: 0.000036
- Resp Pkts: 0.882229
- Resp Bytes: 1.503448

### Arp_Spoofing Sample 3:

**Description**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.08 packets/second. Balanced bidirectional traffic: ratio 0.17. Very short inter-arrival time: -0.167218s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 2.350975
- Bwd Header Max: 1.374499
- Flow Pkts/Sec: 0.082291
- Resp Pkts: 0.882229
- Resp Bytes: 1.032615

## Typical Value Ranges:

- **Fwd Header Size Max**: Median=2.3510, Range=[1.4782, 2.3510]
- **Bwd Header Size Max**: Median=2.4597, Range=[1.3745, 3.1832]
- **Flow Pkts Per Sec**: Median=0.1440, Range=[0.0002, 0.6649]
- **Resp Pkts**: Median=0.8822, Range=[0.8822, 0.8822]
- **Resp Ip Bytes**: Median=1.5034, Range=[1.0326, 1.5034]

## How to Classify:

1. Get your flow's feature values
2. **Compare directly** with the sample values above
3. Check if values are **similar** to the Arp_Spoofing samples
4. If similar → Classify as **Arp_Spoofing**


================================================================================
# BotNet_DDOS
================================================================================

**Dataset Count**: 57,611 samples

## Real Samples from Dataset:

Compare your flow with these **actual BotNet_DDOS samples**:

### BotNet_DDOS Sample 1:

**Description**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: -0.434242
- Flow Pkts/Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Bytes: -0.536830

### BotNet_DDOS Sample 2:

**Description**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: -0.434242
- Flow Pkts/Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Bytes: -0.536830

### BotNet_DDOS Sample 3:

**Description**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: -0.434242
- Flow Pkts/Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Bytes: -0.536830

## Typical Value Ranges:

- **Fwd Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Bwd Header Size Max**: Median=-0.4342, Range=[-0.4342, -0.4342]
- **Flow Pkts Per Sec**: Median=0.0000, Range=[0.0000, 0.0000]
- **Resp Pkts**: Median=-0.5003, Range=[-0.5003, -0.5003]
- **Resp Ip Bytes**: Median=-0.5368, Range=[-0.5368, -0.5368]

## How to Classify:

1. Get your flow's feature values
2. **Compare directly** with the sample values above
3. Check if values are **similar** to the BotNet_DDOS samples
4. If similar → Classify as **BotNet_DDOS**


================================================================================
# HTTP_Flood
================================================================================

**Dataset Count**: 57,611 samples

## Real Samples from Dataset:

Compare your flow with these **actual HTTP_Flood samples**:

### HTTP_Flood Sample 1:

**Description**: Total packets: 3 (0 origin, 2 response). Total bytes: 3 (0 origin, 3 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: -0.434242
- Flow Pkts/Sec: 0.000000
- Resp Pkts: 2.264751
- Resp Bytes: 2.915949

### HTTP_Flood Sample 2:

**Description**: Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: -2.013114
- Bwd Header Max: 1.736247
- Flow Pkts/Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Bytes: -0.536830

### HTTP_Flood Sample 3:

**Description**: Total packets: 0 (-1 origin, 1 response). Total bytes: 1 (-1 origin, 1 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: -2.013114
- Bwd Header Max: 1.736247
- Flow Pkts/Sec: 0.000000
- Resp Pkts: 0.882229
- Resp Bytes: 1.189559

## Typical Value Ranges:

- **Fwd Header Size Max**: Median=0.1689, Range=[0.1689, 0.1689]
- **Bwd Header Size Max**: Median=-0.4342, Range=[-0.4342, 1.7362]
- **Flow Pkts Per Sec**: Median=0.0000, Range=[0.0000, 0.0000]
- **Resp Pkts**: Median=-0.5003, Range=[-0.5003, 0.8822]
- **Resp Ip Bytes**: Median=-0.5368, Range=[-0.5368, 1.1896]

## How to Classify:

1. Get your flow's feature values
2. **Compare directly** with the sample values above
3. Check if values are **similar** to the HTTP_Flood samples
4. If similar → Classify as **HTTP_Flood**


================================================================================
# ICMP_Flood
================================================================================

**Dataset Count**: 27,167 samples

## Real Samples from Dataset:

Compare your flow with these **actual ICMP_Flood samples**:

### ICMP_Flood Sample 1:

**Description**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.09 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166099s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: 1.374499
- Flow Pkts/Sec: 0.087822
- Resp Pkts: 0.882229
- Resp Bytes: 1.032615

### ICMP_Flood Sample 2:

**Description**: Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: 1.374499
- Flow Pkts/Sec: 0.000086
- Resp Pkts: 3.647273
- Resp Bytes: 4.328450

### ICMP_Flood Sample 3:

**Description**: Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.14 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166259s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 0.168930
- Bwd Header Max: 1.374499
- Flow Pkts/Sec: 0.135477
- Resp Pkts: 0.882229
- Resp Bytes: 1.032615

## Typical Value Ranges:

- **Fwd Header Size Max**: Median=0.1689, Range=[0.1689, 0.6053]
- **Bwd Header Size Max**: Median=1.3745, Range=[1.3745, 1.7362]
- **Flow Pkts Per Sec**: Median=0.0008, Range=[0.0001, 0.0091]
- **Resp Pkts**: Median=0.8822, Range=[0.8822, 3.6473]
- **Resp Ip Bytes**: Median=1.0326, Range=[1.0326, 4.3284]

## How to Classify:

1. Get your flow's feature values
2. **Compare directly** with the sample values above
3. Check if values are **similar** to the ICMP_Flood samples
4. If similar → Classify as **ICMP_Flood**


================================================================================
# Quick Comparison Guide
================================================================================

## Key Differences Between Classes:

### Arp_Spoofing:
- **Fwd Header Max**: Usually > 1.4 (see samples above)
- **Bwd Header Max**: Usually > 1.3 (see samples above)
- Compare with Arp_Spoofing samples

### BotNet_DDOS:
- **Flow Pkts/Sec**: Usually ≈ 0.0 (see samples above)
- **Resp Pkts**: Usually negative (see samples above)
- Compare with BotNet_DDOS samples

### HTTP_Flood:
- Check actual samples above for patterns
- Compare feature values

### ICMP_Flood:
- Check actual samples above for patterns
- Compare feature values

### Normal:
- Check actual samples above for patterns
- Compare feature values

## Classification Process:

1. Extract your flow's feature values
2. Compare with samples from each class
3. Find which class's samples match best
4. Classify accordingly
