# Network Traffic Classification - Improved Distinction Rules

**IMPORTANT**: Check conditions in order. Use exclusion rules to avoid misclassification.

## Quick Exclusion Rule:

**IF Fwd Header Max < 1.4782 → NOT Arp_Spoofing**

(This is the most important distinction - Arp_Spoofing has high Fwd Header Max)


================================================================================
# Arp_Spoofing
================================================================================
**What it is**: ARP spoofing attack - falsified ARP messages.

**Arp_Spoofing Sample Values:**

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

IF Fwd Header Max > 1.4782 AND Bwd Header Max > 1.3745
THEN classify as Arp_Spoofing

**Exclusion**: If Fwd Header Max < 1.4782, it's NOT Arp_Spoofing


================================================================================
# BotNet_DDOS
================================================================================
**What it is**: BotNet DDoS attack - coordinated attack from multiple sources.

**BotNet_DDOS Sample Values:**

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

IF Flow Pkts/Sec ≈ 0.0 AND Resp Pkts < 0
AND Fwd Header Max < 1.4782  # NOT Arp_Spoofing
THEN classify as BotNet_DDOS

**Key**: BotNet_DDOS has very low Fwd Header Max (≈0.17), which is much lower than Arp_Spoofing (≥1.48)


================================================================================
# HTTP_Flood
================================================================================
**What it is**: HTTP flood attack - excessive HTTP requests.

**HTTP_Flood Sample Values:**

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

IF (Resp Pkts > -0.5003 OR values match samples above)
AND Fwd Header Max < 1.4782  # NOT Arp_Spoofing
THEN classify as HTTP_Flood

**Key**: HTTP_Flood has low Fwd Header Max (≈0.17), which is much lower than Arp_Spoofing (≥1.48)


================================================================================
# ICMP_Flood
================================================================================
**What it is**: ICMP flood attack - ping flood.

**ICMP_Flood Sample Values:**

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

IF Flow Pkts/Sec > 0.009119
AND Fwd Header Max < 1.4782  # NOT Arp_Spoofing
THEN classify as ICMP_Flood

**Key**: ICMP_Flood has low Fwd Header Max (≈0.17), which is much lower than Arp_Spoofing (≥1.48)


================================================================================
# Classification Order (Check in this order)
================================================================================

1. **First, check Fwd Header Max:**
   - IF Fwd Header Max < 1.4782 → NOT Arp_Spoofing
   - Then check other classes (BotNet_DDOS, HTTP_Flood, ICMP_Flood, etc.)
   
2. **IF Fwd Header Max ≥ 1.4782:**
   - Check Bwd Header Max
   - IF Bwd Header Max > 1.3745 → Arp_Spoofing
   - ELSE → Check other classes

3. **For other classes (Fwd Header Max < 1.4782):**
   - BotNet_DDOS: Flow Pkts/Sec ≈ 0.0 AND Resp Pkts < 0
   - HTTP_Flood: Check Resp Pkts and Resp Bytes with samples
   - ICMP_Flood: Flow Pkts/Sec > 0.0091
   - Normal: Balanced values, not matching attack patterns

**Key Insight**: Fwd Header Max is the most distinguishing feature!
- Arp_Spoofing: Fwd Header Max ≥ 1.4782
- All other classes: Fwd Header Max < 1.4782 (usually ≈ 0.17)
