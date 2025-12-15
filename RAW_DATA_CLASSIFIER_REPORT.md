# 원시 데이터 기반 LLM 분류기 보고서

## 생성된 파일

1. **create_raw_data_classifier.py** - 원시 데이터 패턴 분석 및 분류기
2. **create_improved_raw_classifier.py** - 개선된 분류기 (간결한 프롬프트)
3. **create_final_raw_classifier.py** - 최종 분류기 (IF-THEN 형식)
4. **raw_data_classification_guide.md** - 원시 데이터 기반 가이드 문서

## 프롬프트 구조

### 포함된 원시 데이터 특징:
- **Protocol (proto)**: tcp, udp, icmp, arp
- **Service**: mqtt, http, dns, icmp 등
- **Connection State (conn_state)**: SF, S0, S1, SHR, OTH 등
- **IP 주소**: id.orig_h, id.resp_h
- **포트**: id.orig_p, id.resp_p
- **패킷/바이트**: orig_pkts, resp_pkts, orig_bytes, resp_bytes
- **지속 시간**: duration, flow_duration

### IF-THEN 분류 규칙:

1. Protocol = 'arp' → Arp_Spoofing
2. Protocol = 'icmp' → ICMP_Flood
3. Protocol = 'udp' → UDP_Flood
4. Connection State = 'S0' AND orig_pkts=1 AND resp_pkts=0 → Port_Scanning
5. Connection State = 'S0' OR 'S1' AND orig_pkts > resp_pkts → TCP_Flood
6. Connection State = 'SHR' AND orig_pkts=0 AND resp_pkts=1 → Arp_Spoofing
7. Service = 'http' AND port 80/443/1880 → HTTP_Flood
8. Service = 'mqtt' AND port 1883 → MQTT_Flood
9. None match → Normal

## 테스트 결과

- **정확도**: 33.3% (4/12)
- **Port_Scanning**: 100% (3/3) ✅
- **HTTP_Flood**: 33.3% (1/3)
- **Normal**: 0% (0/3) ❌
- **Arp_Spoofing**: 0% (0/3) ❌

## 개선 사항

1. ✅ 원시 데이터(proto, service, conn_state, IP, 포트) 사용
2. ✅ 각 클래스의 특징적인 패턴을 프롬프트에 포함
3. ✅ IF-THEN 형식의 명확한 규칙 사용
4. ⚠️ Normal과 Arp_Spoofing 분류 개선 필요

## 사용 방법

```python
from create_final_raw_classifier import FinalRawDataClassifier
import pandas as pd

# 데이터 로드
df = pd.read_csv("Datasets/Farm-Flows.csv")

# 분류기 초기화
classifier = FinalRawDataClassifier()

# 분류
row = df.iloc[0]
pred_label, conf, info = classifier.classify(row)
print(f"Predicted: {pred_label}")
```

