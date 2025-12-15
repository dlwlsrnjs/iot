# Network Traffic Classification - Direct Sample Comparison

Compare your flow's feature values DIRECTLY with the sample values below.


================================================================================
# Arp_Spoofing
================================================================================
**What it is**: ARP spoofing attack - falsified ARP messages.

**Arp_Spoofing Sample Values (compare with these):**

Sample 1:
  Fwd Header Max: 2.350975
  Bwd Header Max: 3.183240
  Flow Pkts/Sec: 0.000047
  Resp Pkts: 0.882229
  Resp Bytes: 1.032615

Sample 2:
  Fwd Header Max: 2.350975
  Bwd Header Max: 3.183240
  Flow Pkts/Sec: 0.000036
  Resp Pkts: 0.882229
  Resp Bytes: 1.503448

**When to classify as Arp_Spoofing:**

- IF Fwd Header Max > 1.4782 AND Bwd Header Max > 1.3745 → Arp_Spoofing


================================================================================
# BotNet_DDOS
================================================================================
**What it is**: BotNet DDoS attack - coordinated attack from multiple sources.

**BotNet_DDOS Sample Values (compare with these):**

Sample 1:
  Fwd Header Max: 0.168930
  Bwd Header Max: -0.434242
  Flow Pkts/Sec: 0.000000
  Resp Pkts: -0.500293
  Resp Bytes: -0.536830

Sample 2:
  Fwd Header Max: 0.168930
  Bwd Header Max: -0.434242
  Flow Pkts/Sec: 0.000000
  Resp Pkts: -0.500293
  Resp Bytes: -0.536830

**When to classify as BotNet_DDOS:**

- IF Flow Pkts/Sec ≈ 0.0 AND Resp Pkts < 0 → BotNet_DDOS


================================================================================
# HTTP_Flood
================================================================================
**What it is**: HTTP flood attack - excessive HTTP requests.

**HTTP_Flood Sample Values (compare with these):**

Sample 1:
  Fwd Header Max: 0.168930
  Bwd Header Max: -0.434242
  Flow Pkts/Sec: 0.000000
  Resp Pkts: 2.264751
  Resp Bytes: 2.915949

Sample 2:
  Fwd Header Max: -2.013114
  Bwd Header Max: 1.736247
  Flow Pkts/Sec: 0.000000
  Resp Pkts: -0.500293
  Resp Bytes: -0.536830

**When to classify as HTTP_Flood:**

- Compare your values with the HTTP_Flood samples above
- If similar → HTTP_Flood


================================================================================
# ICMP_Flood
================================================================================
**What it is**: ICMP flood attack - ping flood.

**ICMP_Flood Sample Values (compare with these):**

Sample 1:
  Fwd Header Max: 0.168930
  Bwd Header Max: 1.374499
  Flow Pkts/Sec: 0.087822
  Resp Pkts: 0.882229
  Resp Bytes: 1.032615

Sample 2:
  Fwd Header Max: 0.168930
  Bwd Header Max: 1.374499
  Flow Pkts/Sec: 0.000086
  Resp Pkts: 3.647273
  Resp Bytes: 4.328450

**When to classify as ICMP_Flood:**

- IF Flow Pkts/Sec > 0.009119 → ICMP_Flood
