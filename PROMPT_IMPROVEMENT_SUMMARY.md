# 프롬프트 개선 요약

## 개선된 프롬프트 구조

### 최종 버전: `create_optimized_raw_classifier.py`

**프롬프트 특징:**
- 매우 간결하고 직접적
- 규칙을 명확하게 나열
- 순서대로 체크하도록 지시

### 포함된 원시 데이터 특징:
- **Protocol (proto)**: tcp, udp, icmp, arp
- **Service**: mqtt, http 등
- **Connection State (conn_state)**: S0, S1, SHR, OTH 등
- **포트**: id.resp_p
- **패킷**: orig_pkts, resp_pkts

### 분류 규칙 (순서대로):

1. Protocol='arp' → Arp_Spoofing
2. Protocol='icmp' → ICMP_Flood
3. Protocol='udp' → UDP_Flood
4. ConnectionState='SHR' AND OrigPkts=0 AND RespPkts=1 → Arp_Spoofing
5. ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0 → Port_Scanning
6. ConnectionState='S0' AND OrigPkts>RespPkts → TCP_Flood
7. Service='http' AND Port IN (80,443,1880) → HTTP_Flood
8. Service='mqtt' AND Port=1883 → MQTT_Flood
9. Else → Normal

## 개선 사항

1. ✅ 원시 데이터(proto, service, conn_state, IP, 포트) 사용
2. ✅ 각 클래스의 특징적인 패턴을 프롬프트에 포함
3. ✅ 간결하고 직접적인 규칙 명시
4. ✅ 순서대로 체크하도록 지시

## 현재 성능

- 정확도: 테스트 중
- Normal: 높은 정확도
- Port_Scanning: 높은 정확도 (이전 테스트에서 100%)
- Arp_Spoofing, HTTP_Flood: 개선 필요

## 사용 방법

```python
from create_optimized_raw_classifier import OptimizedRawDataClassifier
import pandas as pd

# 데이터 로드
df = pd.read_csv("Datasets/Farm-Flows.csv")

# 분류기 초기화
classifier = OptimizedRawDataClassifier()

# 분류
row = df.iloc[0]
pred_label, conf, info = classifier.classify(row)
print(f"Predicted: {pred_label}")
```

