# Network Traffic Classification - Data-Based Rules

This guide contains classification rules based on actual data analysis.
Rules are designed to match at least 70% of samples in each class.


================================================================================
# Arp_Spoofing
================================================================================

Sample Count: 57,611

## Classification Rules:

### Forward Header Size Max (`fwd_header_size_max`)
- **Rule**: If this value is **> 1.4782**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 2.3510
- **Range**: [-1.1403, 3.6602]

### Backward Header Size Max (`bwd_header_size_max`)
- **Rule**: If this value is **> 1.3745**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 2.4597
- **Range**: [-0.4342, 4.9920]

### Flow Packets Per Second (`flow_pkts_per_sec`)
- **Rule**: If this value is **> 0.0002**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 0.1440
- **Range**: [0.0000, 1.0000]

### Response Packets (`resp_pkts`)
- **Rule**: If this value is **> 0.8822**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 0.8822
- **Range**: [-0.5003, 2.2648]

### Response IP Bytes (`resp_ip_bytes`)
- **Rule**: If this value is **> 1.0326**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 1.5034
- **Range**: [-0.5368, 4.4854]

### Origin Packets (`orig_pkts`)
- **Rule**: If this value is **< -0.0678**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: -0.0678
- **Range**: [-0.0678, 1.8263]

### Origin IP Bytes (`orig_ip_bytes`)
- **Rule**: If this value is **< 2.6770**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: -0.0622
- **Range**: [-0.2767, 7.6779]

### Forward Packets Per Second (`fwd_pkts_per_sec`)
- **Rule**: If this value is **> 0.0002**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 0.1065
- **Range**: [0.0000, 0.7360]

### Backward Packets Per Second (`bwd_pkts_per_sec`)
- **Rule**: If this value is **> 0.0002**, it suggests Arp_Spoofing (75% of samples satisfy this)
- **Median**: 0.1440
- **Range**: [0.0000, 1.0000]

## Key Indicators:

When classifying Arp_Spoofing, check these features first:

- Forward Header Size Max > 1.4782
- Backward Header Size Max > 1.3745
- Flow Packets Per Second > 0.0002


================================================================================
# BotNet_DDOS
================================================================================

Sample Count: 57,611

## Classification Rules:

### Forward Header Size Max (`fwd_header_size_max`)
- **Rule**: If this value is **> 0.1689**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: 0.1689
- **Range**: [-2.0131, 2.7874]

### Backward Header Size Max (`bwd_header_size_max`)
- **Rule**: If this value is **< -0.4342**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: -0.4342
- **Range**: [-0.4342, 3.1832]

### Flow Packets Per Second (`flow_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests BotNet_DDOS
- **Median**: 0.0000
- **Range**: [0.0000, 0.7267]

### Response Packets (`resp_pkts`)
- **Rule**: If this value is **< -0.5003**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: -0.5003
- **Range**: [-0.5003, -0.5003]

### Response IP Bytes (`resp_ip_bytes`)
- **Rule**: If this value is **< -0.5368**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: -0.5368
- **Range**: [-0.5368, -0.5368]

### Origin Packets (`orig_pkts`)
- **Rule**: If this value is **< -0.0678**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: -0.0678
- **Range**: [-0.0678, 0.8792]

### Origin IP Bytes (`orig_ip_bytes`)
- **Rule**: If this value is **< -0.2767**, it suggests BotNet_DDOS (75% of samples satisfy this)
- **Median**: -0.2767
- **Range**: [-0.2767, 0.5032]

### Forward Packets Per Second (`fwd_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests BotNet_DDOS
- **Median**: 0.0000
- **Range**: [0.0000, 0.5349]

### Backward Packets Per Second (`bwd_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests BotNet_DDOS
- **Median**: 0.0000
- **Range**: [0.0000, 0.7267]

## Key Indicators:

When classifying BotNet_DDOS, check these features first:

- Forward Header Size Max > 0.1689
- Backward Header Size Max < -0.4342
- Flow Packets Per Second ≈ 0.0


================================================================================
# HTTP_Flood
================================================================================

Sample Count: 57,611

## Classification Rules:

### Forward Header Size Max (`fwd_header_size_max`)
- **Rule**: If this value is **> 0.1689**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: 0.1689
- **Range**: [-2.0131, 2.3510]

### Backward Header Size Max (`bwd_header_size_max`)
- **Rule**: If this value is **< 1.7362**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: -0.4342
- **Range**: [-0.4342, 3.1832]

### Flow Packets Per Second (`flow_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests HTTP_Flood
- **Median**: 0.0000
- **Range**: [0.0000, 1.0000]

### Response Packets (`resp_pkts`)
- **Rule**: If this value is **< 0.8822**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: -0.5003
- **Range**: [-0.5003, 3.6473]

### Response IP Bytes (`resp_ip_bytes`)
- **Rule**: If this value is **< 1.1896**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: -0.5368
- **Range**: [-0.5368, 4.6423]

### Origin Packets (`orig_pkts`)
- **Rule**: If this value is **< -0.0678**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: -0.0678
- **Range**: [-0.5413, 0.4057]

### Origin IP Bytes (`orig_ip_bytes`)
- **Rule**: If this value is **< -0.2767**, it suggests HTTP_Flood (75% of samples satisfy this)
- **Median**: -0.2767
- **Range**: [-0.6666, 0.1132]

### Forward Packets Per Second (`fwd_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests HTTP_Flood
- **Median**: 0.0000
- **Range**: [0.0000, 0.7360]

### Backward Packets Per Second (`bwd_pkts_per_sec`)
- **Rule**: If this value is **≈ 0.0** (between 0.0000 and 0.0000), it suggests HTTP_Flood
- **Median**: 0.0000
- **Range**: [0.0000, 1.0000]

## Key Indicators:

When classifying HTTP_Flood, check these features first:

- Forward Header Size Max > 0.1689
- Backward Header Size Max < 1.7362
- Flow Packets Per Second ≈ 0.0


================================================================================
# ICMP_Flood
================================================================================

Sample Count: 27,167

## Classification Rules:

### Forward Header Size Max (`fwd_header_size_max`)
- **Rule**: If this value is **> 0.1689**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.1689
- **Range**: [-2.0131, 2.7874]

### Backward Header Size Max (`bwd_header_size_max`)
- **Rule**: If this value is **> 1.3745**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 1.3745
- **Range**: [-0.4342, 3.5450]

### Flow Packets Per Second (`flow_pkts_per_sec`)
- **Rule**: If this value is **> 0.0001**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.0008
- **Range**: [0.0000, 0.2772]

### Response Packets (`resp_pkts`)
- **Rule**: If this value is **> 0.8822**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.8822
- **Range**: [-0.5003, 3.6473]

### Response IP Bytes (`resp_ip_bytes`)
- **Rule**: If this value is **> 1.0326**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 1.0326
- **Range**: [-0.5368, 4.6423]

### Origin Packets (`orig_pkts`)
- **Rule**: If this value is **> 0.4057**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.4057
- **Range**: [-0.0678, 1.8263]

### Origin IP Bytes (`orig_ip_bytes`)
- **Rule**: If this value is **> 0.1132**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.1132
- **Range**: [-0.2767, 3.0962]

### Forward Packets Per Second (`fwd_pkts_per_sec`)
- **Rule**: If this value is **> 0.0001**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.0006
- **Range**: [0.0000, 0.2040]

### Backward Packets Per Second (`bwd_pkts_per_sec`)
- **Rule**: If this value is **> 0.0001**, it suggests ICMP_Flood (75% of samples satisfy this)
- **Median**: 0.0008
- **Range**: [0.0000, 0.2772]

## Key Indicators:

When classifying ICMP_Flood, check these features first:

- Forward Header Size Max > 0.1689
- Backward Header Size Max > 1.3745
- Flow Packets Per Second > 0.0001
