# 가이드 내용 요약 - 각 클래스 설명과 선택 조건

## 현재 가이드에 포함된 내용

### ✅ 각 클래스가 무엇인지 설명
### ✅ 어떤 경우에 해당 클래스를 선택해야 하는지 IF-THEN 규칙
### ✅ 실제 샘플 예시

## 각 클래스별 내용

### 1. Arp_Spoofing

**클래스 설명:**
- ARP spoofing is an attack where an attacker sends falsified ARP messages to link their MAC address with a legitimate IP address, causing network disruption.

**IF-THEN 규칙:**
```
IF Forward Header Size Max > 1.4782 AND Backward Header Size Max > 1.3745
THEN classify as Arp_Spoofing

OR

IF the flow's feature values are similar to the Arp_Spoofing samples above
THEN classify as Arp_Spoofing
```

**실제 샘플 예시:**
- Sample 1: Fwd Header Max: 2.350975, Bwd Header Max: 3.183240
- Sample 2: Fwd Header Max: 2.350975, Bwd Header Max: 3.183240
- Sample 3: Fwd Header Max: 2.350975, Bwd Header Max: 1.374499

### 2. BotNet_DDOS

**클래스 설명:**
- BotNet DDoS is a distributed denial-of-service attack launched by a botnet, showing coordinated attack patterns from multiple compromised devices.

**IF-THEN 규칙:**
```
IF Flow Packets Per Second ≈ 0.0 AND Response Packets < 0 (negative)
THEN classify as BotNet_DDOS

OR

IF the flow's feature values match the BotNet_DDOS samples above 
(Flow Pkts/Sec ≈ 0.0, negative packet values)
THEN classify as BotNet_DDOS
```

**실제 샘플 예시:**
- Sample 1: Flow Pkts/Sec: 0.000000, Resp Pkts: -0.500293, Resp Bytes: -0.536830
- Sample 2: Flow Pkts/Sec: 0.000000, Resp Pkts: -0.500293, Resp Bytes: -0.536830
- Sample 3: Flow Pkts/Sec: 0.000000, Resp Pkts: -0.500293, Resp Bytes: -0.536830

### 3. HTTP_Flood

**클래스 설명:**
- HTTP flood is an attack that overwhelms a web server by sending excessive HTTP requests, exhausting server resources.

**IF-THEN 규칙:**
```
IF the flow's feature values are similar to the HTTP_Flood samples above
THEN classify as HTTP_Flood

(Compare Response Packets and Response IP Bytes with samples)
```

**실제 샘플 예시:**
- Sample 1: Resp Pkts: 2.264751, Resp Bytes: 2.915949
- Sample 2: Resp Pkts: -0.500293, Resp Bytes: -0.536830
- Sample 3: Resp Pkts: 0.882229, Resp Bytes: 1.189559

### 4. ICMP_Flood

**클래스 설명:**
- ICMP flood is an attack that floods the target with ICMP packets (ping flood), causing network saturation.

**IF-THEN 규칙:**
```
IF Flow Packets Per Second > 0.0091 OR values match ICMP_Flood samples above
THEN classify as ICMP_Flood
```

**실제 샘플 예시:**
- Sample 1: Flow Pkts/Sec: 0.087822, Resp Pkts: 0.882229
- Sample 2: Flow Pkts/Sec: 0.000086, Resp Pkts: 3.647273
- Sample 3: Flow Pkts/Sec: 0.135477, Resp Pkts: 0.882229

### 5. Normal

**클래스 설명:**
- Normal network traffic represents legitimate, non-malicious communication between devices in an IoT network.

**IF-THEN 규칙:**
```
IF the flow shows balanced, moderate values AND matches Normal samples above
THEN classify as Normal

IF the flow does NOT match any attack class conditions above
THEN classify as Normal (default)
```

## 결론

✅ **가이드에 포함된 내용:**
1. 각 클래스가 무엇인지 설명 ✅
2. 어떤 경우에 해당 클래스를 선택해야 하는지 IF-THEN 규칙 ✅
3. 실제 샘플 예시 ✅

❌ **문제점:**
- LLM이 IF-THEN 규칙을 따르지 않음
- 여전히 모든 샘플을 Normal로 분류
- 정확도: 0.0%

## 생성된 파일

- `if_then_classification_guide.md` - IF-THEN 형식 가이드
- `explicit_classification_guide.md` - 명시적 가이드
- `GUIDE_CONTENT_SUMMARY.md` - 본 요약 문서

