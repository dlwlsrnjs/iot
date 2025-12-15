# Network Traffic Classification Guide - Based on Actual Samples

This guide contains **actual sample patterns** from the dataset.
When classifying a flow, compare it with these actual samples and their patterns.


================================================================================
# Arp_Spoofing
================================================================================

**Total Samples in Dataset**: 57,611

## Actual Sample Examples:

These are **real samples** from the dataset. Compare your flow with these:

### Sample 1:

**Flow Description:**
Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 2.350975
- Bwd Header Size Max: 3.183240
- Flow Pkts Per Sec: 0.000047
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.081724
- Fwd Pkts Per Sec: 0.000039
- Bwd Pkts Per Sec: 0.000040

### Sample 2:

**Flow Description:**
Total packets: 1 (-0 origin, 1 response). Total bytes: 4 (2 origin, 2 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 2.350975
- Bwd Header Size Max: 3.183240
- Flow Pkts Per Sec: 0.000036
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.503448
- Orig Pkts: -0.067784
- Orig Ip Bytes: 2.306590
- Fwd Pkts Per Sec: 0.000030
- Bwd Pkts Per Sec: 0.000031

### Sample 3:

**Flow Description:**
Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.08 packets/second. Balanced bidirectional traffic: ratio 0.17. Very short inter-arrival time: -0.167218s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 2.350975
- Bwd Header Size Max: 1.374499
- Flow Pkts Per Sec: 0.082291
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.081724
- Fwd Pkts Per Sec: 0.060566
- Bwd Pkts Per Sec: 0.082291

### Sample 4:

**Flow Description:**
Total packets: 3 (1 origin, 2 response). Total bytes: 9 (5 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.17. Very short inter-arrival time: -0.027567s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 2.350975
- Bwd Header Size Max: 3.183240
- Flow Pkts Per Sec: 0.000059
- Resp Pkts: 2.264751
- Resp Ip Bytes: 3.857616
- Orig Pkts: 0.879234
- Orig Ip Bytes: 4.782638
- Fwd Pkts Per Sec: 0.000043
- Bwd Pkts Per Sec: 0.000059

### Sample 5:

**Flow Description:**
Total packets: 1 (0 origin, 1 response). Total bytes: 2 (1 origin, 2 response). Low packet rate: 0.01 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166212s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 1.478157
- Bwd Header Size Max: 2.459743
- Flow Pkts Per Sec: 0.007974
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.974282
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.522666
- Fwd Pkts Per Sec: 0.007825
- Bwd Pkts Per Sec: 0.005316

## Pattern Summary:

Based on analysis of all samples, here are the typical patterns:

### Fwd Header Size Max:
- **Typical Range**: 1.4782 ~ 2.3510 (50% of samples)
- **Median**: 2.3510
- **Mean**: 1.9698
- **Full Range**: [-1.1403, 3.6602]

### Bwd Header Size Max:
- **Typical Range**: 1.3745 ~ 3.1832 (50% of samples)
- **Median**: 2.4597
- **Mean**: 2.3161
- **Full Range**: [-0.4342, 4.9920]

### Flow Pkts Per Sec:
- **Typical Range**: 0.0002 ~ 0.6649 (50% of samples)
- **Median**: 0.1440
- **Mean**: 0.3214
- **Full Range**: [0.0000, 1.0000]

### Resp Pkts:
- **Typical Range**: 0.8822 ~ 0.8822 (50% of samples)
- **Median**: 0.8822
- **Mean**: 1.0581
- **Full Range**: [-0.5003, 2.2648]

### Resp Ip Bytes:
- **Typical Range**: 1.0326 ~ 1.5034 (50% of samples)
- **Median**: 1.5034
- **Mean**: 1.6289
- **Full Range**: [-0.5368, 4.4854]

## How to Classify:

When you see a flow, compare it with the **actual samples above**:

1. **Look at the flow description** - Does it match the patterns in the samples?
2. **Check the feature values** - Are they similar to the sample values?
3. **Compare with pattern summary** - Do the values fall within typical ranges?
4. **If patterns match** → Classify as **{label_name}**


================================================================================
# BotNet_DDOS
================================================================================

**Total Samples in Dataset**: 57,611

## Actual Sample Examples:

These are **real samples** from the dataset. Compare your flow with these:

### Sample 1:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 2:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 3:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 4:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 5:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Long inter-arrival time: 2.787841s (low frequency). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000004
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000006
- Bwd Pkts Per Sec: 0.000000

## Pattern Summary:

Based on analysis of all samples, here are the typical patterns:

### Fwd Header Size Max:
- **Typical Range**: 0.1689 ~ 0.1689 (50% of samples)
- **Median**: 0.1689
- **Mean**: 0.1675
- **Full Range**: [-2.0131, 2.7874]

### Bwd Header Size Max:
- **Typical Range**: -0.4342 ~ -0.4342 (50% of samples)
- **Median**: -0.4342
- **Mean**: -0.4318
- **Full Range**: [-0.4342, 3.1832]

### Flow Pkts Per Sec:
- **Typical Range**: 0.0000 ~ 0.0000 (50% of samples)
- **Median**: 0.0000
- **Mean**: 0.0000
- **Full Range**: [0.0000, 0.7267]

### Resp Pkts:
- **Typical Range**: -0.5003 ~ -0.5003 (50% of samples)
- **Median**: -0.5003
- **Mean**: -0.5003
- **Full Range**: [-0.5003, -0.5003]

### Resp Ip Bytes:
- **Typical Range**: -0.5368 ~ -0.5368 (50% of samples)
- **Median**: -0.5368
- **Mean**: -0.5368
- **Full Range**: [-0.5368, -0.5368]

## How to Classify:

When you see a flow, compare it with the **actual samples above**:

1. **Look at the flow description** - Does it match the patterns in the samples?
2. **Check the feature values** - Are they similar to the sample values?
3. **Compare with pattern summary** - Do the values fall within typical ranges?
4. **If patterns match** → Classify as **{label_name}**


================================================================================
# HTTP_Flood
================================================================================

**Total Samples in Dataset**: 57,611

## Actual Sample Examples:

These are **real samples** from the dataset. Compare your flow with these:

### Sample 1:

**Flow Description:**
Total packets: 3 (0 origin, 2 response). Total bytes: 3 (0 origin, 3 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: 2.264751
- Resp Ip Bytes: 2.915949
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.113241
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 2:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: -2.013114
- Bwd Header Size Max: 1.736247
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 3:

**Flow Description:**
Total packets: 0 (-1 origin, 1 response). Total bytes: 1 (-1 origin, 1 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: -2.013114
- Bwd Header Size Max: 1.736247
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.189559
- Orig Pkts: -0.541294
- Orig Ip Bytes: -0.666617
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 4:

**Flow Description:**
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: -2.013114
- Bwd Header Size Max: 1.736247
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: -0.500293
- Resp Ip Bytes: -0.536830
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

### Sample 5:

**Flow Description:**
Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: -0.434242
- Flow Pkts Per Sec: 0.000000
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.189559
- Orig Pkts: -0.067784
- Orig Ip Bytes: -0.276688
- Fwd Pkts Per Sec: 0.000000
- Bwd Pkts Per Sec: 0.000000

## Pattern Summary:

Based on analysis of all samples, here are the typical patterns:

### Fwd Header Size Max:
- **Typical Range**: 0.1689 ~ 0.1689 (50% of samples)
- **Median**: 0.1689
- **Mean**: -0.3189
- **Full Range**: [-2.0131, 2.3510]

### Bwd Header Size Max:
- **Typical Range**: -0.4342 ~ 1.7362 (50% of samples)
- **Median**: -0.4342
- **Mean**: 0.4805
- **Full Range**: [-0.4342, 3.1832]

### Flow Pkts Per Sec:
- **Typical Range**: 0.0000 ~ 0.0000 (50% of samples)
- **Median**: 0.0000
- **Mean**: 0.0524
- **Full Range**: [0.0000, 1.0000]

### Resp Pkts:
- **Typical Range**: -0.5003 ~ 0.8822 (50% of samples)
- **Median**: -0.5003
- **Mean**: 0.1756
- **Full Range**: [-0.5003, 3.6473]

### Resp Ip Bytes:
- **Typical Range**: -0.5368 ~ 1.1896 (50% of samples)
- **Median**: -0.5368
- **Mean**: 0.3070
- **Full Range**: [-0.5368, 4.6423]

## How to Classify:

When you see a flow, compare it with the **actual samples above**:

1. **Look at the flow description** - Does it match the patterns in the samples?
2. **Check the feature values** - Are they similar to the sample values?
3. **Compare with pattern summary** - Do the values fall within typical ranges?
4. **If patterns match** → Classify as **{label_name}**


================================================================================
# ICMP_Flood
================================================================================

**Total Samples in Dataset**: 27,167

## Actual Sample Examples:

These are **real samples** from the dataset. Compare your flow with these:

### Sample 1:

**Flow Description:**
Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.09 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166099s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: 1.374499
- Flow Pkts Per Sec: 0.087822
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.113241
- Fwd Pkts Per Sec: 0.086183
- Bwd Pkts Per Sec: 0.058548

### Sample 2:

**Flow Description:**
Total packets: 5 (1 origin, 4 response). Total bytes: 7 (3 origin, 4 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.14. Very short inter-arrival time: -0.093479s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: 1.374499
- Flow Pkts Per Sec: 0.000086
- Resp Pkts: 3.647273
- Resp Ip Bytes: 4.328450
- Orig Pkts: 1.352744
- Orig Ip Bytes: 2.696519
- Fwd Pkts Per Sec: 0.000068
- Bwd Pkts Per Sec: 0.000080

### Sample 3:

**Flow Description:**
Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.14 packets/second. Highly asymmetric traffic: download/upload ratio 0.08 (mostly upload). Very short inter-arrival time: -0.166259s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: 1.374499
- Flow Pkts Per Sec: 0.135477
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.113241
- Fwd Pkts Per Sec: 0.132948
- Bwd Pkts Per Sec: 0.090318

### Sample 4:

**Flow Description:**
Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.17. Very short inter-arrival time: -0.108615s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.168930
- Bwd Header Size Max: 1.374499
- Flow Pkts Per Sec: 0.000108
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.113241
- Fwd Pkts Per Sec: 0.000080
- Bwd Pkts Per Sec: 0.000108

### Sample 5:

**Flow Description:**
Total packets: 1 (0 origin, 1 response). Total bytes: 1 (0 origin, 1 response). Low packet rate: 0.01 packets/second. Balanced bidirectional traffic: ratio 0.12. Very short inter-arrival time: -0.166523s (burst traffic pattern). Small payload: -0 bytes.

**Exact Feature Values:**
- Fwd Header Size Max: 0.605339
- Bwd Header Size Max: 1.736247
- Flow Pkts Per Sec: 0.008493
- Resp Pkts: 0.882229
- Resp Ip Bytes: 1.032615
- Orig Pkts: 0.405725
- Orig Ip Bytes: 0.113241
- Fwd Pkts Per Sec: 0.007144
- Bwd Pkts Per Sec: 0.007280

## Pattern Summary:

Based on analysis of all samples, here are the typical patterns:

### Fwd Header Size Max:
- **Typical Range**: 0.1689 ~ 0.6053 (50% of samples)
- **Median**: 0.1689
- **Mean**: 0.2191
- **Full Range**: [-2.0131, 2.7874]

### Bwd Header Size Max:
- **Typical Range**: 1.3745 ~ 1.7362 (50% of samples)
- **Median**: 1.3745
- **Mean**: 1.4009
- **Full Range**: [-0.4342, 3.5450]

### Flow Pkts Per Sec:
- **Typical Range**: 0.0001 ~ 0.0091 (50% of samples)
- **Median**: 0.0008
- **Mean**: 0.0143
- **Full Range**: [0.0000, 0.2772]

### Resp Pkts:
- **Typical Range**: 0.8822 ~ 3.6473 (50% of samples)
- **Median**: 0.8822
- **Mean**: 2.1372
- **Full Range**: [-0.5003, 3.6473]

### Resp Ip Bytes:
- **Typical Range**: 1.0326 ~ 4.3284 (50% of samples)
- **Median**: 1.0326
- **Mean**: 2.5286
- **Full Range**: [-0.5368, 4.6423]

## How to Classify:

When you see a flow, compare it with the **actual samples above**:

1. **Look at the flow description** - Does it match the patterns in the samples?
2. **Check the feature values** - Are they similar to the sample values?
3. **Compare with pattern summary** - Do the values fall within typical ranges?
4. **If patterns match** → Classify as **{label_name}**


================================================================================
# How to Distinguish Between Classes
================================================================================

When classifying, compare your flow with samples from different classes:

## Key Differences:

### Arp_Spoofing vs Others:
- Arp_Spoofing typically has **higher header sizes** (Fwd > 1.4, Bwd > 1.3)
- Compare with actual Arp_Spoofing samples above

### BotNet_DDOS vs Others:
- BotNet_DDOS has **very low packet rates** (≈ 0.0) and **negative packet/byte values**
- Compare with actual BotNet_DDOS samples above

### HTTP_Flood vs Others:
- HTTP_Flood patterns vary - check actual samples above
- Compare feature values with HTTP_Flood samples

### ICMP_Flood vs Others:
- ICMP_Flood may have **slightly higher packet rates** than others
- Compare with actual ICMP_Flood samples above

### Normal vs Others:
- Normal has **balanced, moderate values**
- Compare with actual Normal samples above

## Classification Process:

1. Get the flow's feature values
2. Compare with actual samples from each class (see examples above)
3. Find which class's samples match best
4. Check if values fall within typical ranges
5. Classify accordingly
