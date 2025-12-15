# 차별점을 포함한 개선된 프롬프트

## 발견된 주요 차별점

### 1. Port_Scanning vs Arp_Spoofing

**문제**: Port_Scanning (ConnectionState='S0', OrigPkts=1, RespPkts=0)이 Arp_Spoofing으로 오분류됨

**차별점**:
- **flow_pkts_per_sec**: Port_Scanning=14652.69, Arp_Spoofing=0.00 (매우 큰 차이!)
- **fwd_pkts_per_sec**: Port_Scanning=7326.35, Arp_Spoofing=0.00
- **bwd_pkts_per_sec**: Port_Scanning=7326.35, Arp_Spoofing=0.00
- **fwd_header_size_max**: Port_Scanning=24.00, Arp_Spoofing=8.00

**규칙 추가**:
- ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0인 경우:
  - FlowPktsPerSec > 1000 → Port_Scanning
  - FwdPktsPerSec > 1000 → Port_Scanning
  - FwdHeaderMax > 20 → Port_Scanning

### 2. HTTP_Flood vs Normal

**문제**: HTTP_Flood가 Normal로 오분류됨

**차별점**:
- **flow_pkts_per_sec**: HTTP_Flood=6579.30, Normal=7.37 (매우 큰 차이!)
- **duration**: HTTP_Flood=0.01, Normal=4.10
- **orig_pkts**: HTTP_Flood=2.00, Normal=14.00
- **resp_pkts**: HTTP_Flood=1.00, Normal=14.00
- **fwd_pkts_per_sec**: HTTP_Flood=3310.42, Normal=3.75
- **bwd_pkts_per_sec**: HTTP_Flood=3256.45, Normal=3.64

**규칙 추가**:
- Service='http' AND Port IN (80,443,1880)인 경우:
  - FlowPktsPerSec > 100 → HTTP_Flood
  - Duration < 0.1 → HTTP_Flood
- Service='http' OR Service='-' AND FlowPktsPerSec > 1000 AND Duration < 1.0 → HTTP_Flood

### 3. Arp_Spoofing 구분

**차별점**:
- **flow_pkts_per_sec**: Arp_Spoofing=0.00 (거의 0)
- ConnectionState='SHR' AND OrigPkts=0 AND RespPkts=1인 경우:
  - FlowPktsPerSec > 10 → NOT Arp_Spoofing
  - FwdPktsPerSec > 10 → NOT Arp_Spoofing

## 개선된 프롬프트 구조

### 포함된 추가 원시 데이터 특징:
- **flow_pkts_per_sec**: 초당 플로우 패킷 수
- **fwd_pkts_per_sec**: 초당 전송 패킷 수
- **bwd_pkts_per_sec**: 초당 수신 패킷 수
- **duration**: 연결 지속 시간
- **fwd_header_size_max**: 최대 전송 헤더 크기

### 분류 단계:

1. **Protocol 체크**: arp, icmp, udp
2. **ConnectionState='S0' 체크** (Port_Scanning 우선):
   - FlowPktsPerSec > 1000 → Port_Scanning
   - FwdPktsPerSec > 1000 → Port_Scanning
   - FwdHeaderMax > 20 → Port_Scanning
3. **ConnectionState='SHR' 체크** (Arp_Spoofing):
   - FlowPktsPerSec > 10 → NOT Arp_Spoofing
4. **Service 체크** (HTTP_Flood):
   - FlowPktsPerSec > 100 → HTTP_Flood
   - Duration < 0.1 → HTTP_Flood
5. **추가 특징 체크** (HTTP_Flood):
   - FlowPktsPerSec > 1000 AND Duration < 1.0 → HTTP_Flood
6. **Default**: Normal

## 예상 개선 효과

- **Port_Scanning**: FlowPktsPerSec 차별점으로 정확도 향상 예상
- **HTTP_Flood**: FlowPktsPerSec와 Duration 차별점으로 정확도 향상 예상
- **Arp_Spoofing**: FlowPktsPerSec ≈ 0 특징으로 오분류 방지

## 사용 방법

```python
from create_enhanced_with_distinctions import EnhancedDistinctionClassifier
import pandas as pd

# 데이터 로드
df = pd.read_csv("Datasets/Farm-Flows.csv")

# 분류기 초기화
classifier = EnhancedDistinctionClassifier()

# 분류
row = df.iloc[0]
pred_label, conf, info = classifier.classify(row)
print(f"Predicted: {pred_label}")
```

