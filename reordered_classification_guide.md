# Network Traffic Classification - Reordered Rules

**CRITICAL**: Check classes in THIS ORDER. Arp_Spoofing is checked LAST.

## Classification Order (MUST follow this order):

1. **First, check Fwd Header Max:**
   - IF Fwd Header Max < 1.4782 → Check other classes (NOT Arp_Spoofing)
   - IF Fwd Header Max ≥ 1.4782 → Skip to Arp_Spoofing check (last)

2. **For Fwd Header Max < 1.4782, check these classes FIRST:**
   - BotNet_DDOS
   - HTTP_Flood
   - ICMP_Flood
   - Other classes

3. **ONLY if none of the above match, check Arp_Spoofing LAST**


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
AND Fwd Header Max < 1.4782  # MUST be < 1.4782
THEN classify as BotNet_DDOS


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
AND Fwd Header Max < 1.4782  # MUST be < 1.4782
THEN classify as HTTP_Flood


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
AND Fwd Header Max < 1.4782  # MUST be < 1.4782
THEN classify as ICMP_Flood


================================================================================
# Arp_Spoofing (CHECK LAST)
================================================================================

**⚠️ IMPORTANT: Check Arp_Spoofing ONLY AFTER checking all other classes!**

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

**When to classify as Arp_Spoofing (LAST RESORT):**

IF Fwd Header Max ≥ 1.4782 AND Bwd Header Max > 1.3745
AND all other classes above did NOT match
THEN classify as Arp_Spoofing

**Key**: Arp_Spoofing has HIGH Fwd Header Max (≥1.4782)
