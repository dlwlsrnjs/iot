# 최종 원시 데이터 기반 LLM 분류기

## 생성된 파일

**create_simple_comparison_classifier.py** - 실제 샘플과 직접 비교하는 분류기

## 프롬프트 구조

### 포함된 원시 데이터 특징:
- **Protocol (proto)**: tcp, udp, icmp, arp
- **Service**: mqtt, http, dns 등
- **Connection State (conn_state)**: SF, S0, S1, SHR, OTH 등
- **포트**: id.orig_p, id.resp_p
- **패킷**: orig_pkts, resp_pkts

### 분류 규칙 (순서대로 체크):

1. **Port_Scanning**: ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0
2. **Arp_Spoofing**: ConnectionState='SHR' AND OrigPkts=0 AND RespPkts=1
3. **HTTP_Flood**: Service='http' AND Port IN (80,443,1880)
4. **MQTT_Flood**: Service='mqtt' AND Port=1883
5. **ICMP_Flood**: Protocol='icmp'
6. **UDP_Flood**: Protocol='udp'
7. **Arp_Spoofing**: Protocol='arp'
8. **Normal**: Default

### 프롬프트 특징:
- 실제 샘플 예시 포함
- 간단한 규칙 명시
- 직접 비교 가능한 형식

## 테스트 결과

- **정확도**: 50.0% (6/12)
- **Normal**: 100% (3/3) ✅
- **Port_Scanning**: 100% (3/3) ✅
- **Arp_Spoofing**: 0% (0/3) ❌
- **HTTP_Flood**: 0% (0/3) ❌

## 개선 사항

1. ✅ 실제 샘플과 직접 비교
2. ✅ 간단하고 명확한 규칙
3. ✅ Port_Scanning 100% 정확도 달성
4. ⚠️ Arp_Spoofing과 HTTP_Flood 개선 필요

## 사용 방법

```python
from create_simple_comparison_classifier import SimpleComparisonClassifier
import pandas as pd

# 데이터 로드
df = pd.read_csv("Datasets/Farm-Flows.csv")
examples_df = df.sample(1000, random_state=42)

# 분류기 초기화
classifier = SimpleComparisonClassifier(examples_df=examples_df)

# 분류
row = df.iloc[0]
pred_label, conf, info = classifier.classify(row)
print(f"Predicted: {pred_label}")
```

