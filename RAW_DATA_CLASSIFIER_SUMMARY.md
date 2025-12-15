# 원시 데이터 기반 LLM 분류기 요약

## 생성된 파일

1. **create_raw_data_classifier.py** - 원시 데이터 패턴 분석 및 분류기
2. **create_improved_raw_classifier.py** - 개선된 분류기
3. **create_final_raw_classifier.py** - IF-THEN 형식 분류기
4. **create_step_by_step_raw_classifier.py** - 단계별 분류기
5. **raw_data_classification_guide.md** - 원시 데이터 기반 가이드 문서

## 프롬프트 구조

### 포함된 원시 데이터 특징:
- **Protocol (proto)**: tcp, udp, icmp, arp
- **Service**: mqtt, http, dns, icmp 등
- **Connection State (conn_state)**: SF, S0, S1, SHR, OTH 등
- **IP 주소**: id.orig_h, id.resp_h
- **포트**: id.orig_p, id.resp_p
- **패킷/바이트**: orig_pkts, resp_pkts, orig_bytes, resp_bytes

### 분류 규칙 (단계별):

**Step 1: Protocol 체크**
- proto = 'arp' → Arp_Spoofing
- proto = 'icmp' → ICMP_Flood
- proto = 'udp' → UDP_Flood

**Step 2: Connection State & Packets 체크**
- conn_state = 'SHR' AND orig_pkts = 0 AND resp_pkts = 1 → Arp_Spoofing
- conn_state = 'S0' AND orig_pkts = 1 AND resp_pkts = 0 → Port_Scanning
- conn_state = 'S0' AND orig_pkts > resp_pkts → TCP_Flood

**Step 3: Service & Port 체크**
- service = 'http' AND port 80/443/1880 → HTTP_Flood
- service = 'mqtt' AND port 1883 → MQTT_Flood

**Step 4: Default**
- None match → Normal

## 테스트 결과

- **정확도**: 25.0% (3/12)
- **Normal**: 100% (3/3) ✅
- **Port_Scanning**: 0% (0/3) ❌
- **Arp_Spoofing**: 0% (0/3) ❌
- **HTTP_Flood**: 0% (0/3) ❌

## 문제점

1. LLM이 단계별 체크를 제대로 수행하지 않음
2. Port_Scanning (conn_state='S0', orig=1, resp=0)이 Normal로 오분류됨
3. Arp_Spoofing (conn_state='SHR', orig=0, resp=1)이 Normal로 오분류됨
4. HTTP_Flood가 Normal로 오분류됨

## 개선 방안

1. 프롬프트에 각 단계의 실제 값 비교를 명시적으로 요청
2. 예시 추가
3. 더 큰 모델 사용 고려
4. Few-shot 예시 추가

## 사용 방법

```python
from create_step_by_step_raw_classifier import StepByStepRawDataClassifier
import pandas as pd

# 데이터 로드
df = pd.read_csv("Datasets/Farm-Flows.csv")

# 분류기 초기화
classifier = StepByStepRawDataClassifier()

# 분류
row = df.iloc[0]
pred_label, conf, info = classifier.classify(row)
print(f"Predicted: {pred_label}")
print(f"Response: {info['raw_response']}")
```

