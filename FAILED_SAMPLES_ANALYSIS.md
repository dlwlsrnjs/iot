# 실패 샘플 분석 및 개선 방안

## 실패 샘플 패턴 분석

### 1. Port_Scanning 오분류

**실패 패턴**:
- ConnectionState='S0', OrigPkts=1, RespPkts=0인데도 Arp_Spoofing 또는 HTTP_Flood로 분류됨

**실제 실패 샘플들**:
```
Port_Scanning 샘플 1:
  Protocol: tcp
  Service: -
  ConnectionState: S0
  Port: 902
  OrigPkts: 1
  RespPkts: 0
  FlowPktsPerSec: 17367.72
  → 오분류: Arp_Spoofing

Port_Scanning 샘플 2:
  Protocol: tcp
  Service: -
  ConnectionState: S0
  Port: 2111
  OrigPkts: 1
  RespPkts: 0
  FlowPktsPerSec: 14388.69
  → 오분류: Arp_Spoofing

Port_Scanning 샘플 3:
  Protocol: tcp
  Service: -
  ConnectionState: S0
  Port: 13782
  OrigPkts: 1
  RespPkts: 0
  FlowPktsPerSec: 5.39
  → 오분류: HTTP_Flood
```

**차별점**:
- Port_Scanning: ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0 (명확한 패턴)
- FlowPktsPerSec 값과 무관하게 이 패턴이면 Port_Scanning

**개선 방안**:
- ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0 → Port_Scanning (절대적 규칙)
- FlowPktsPerSec 값은 무시

### 2. HTTP_Flood 오분류

**실패 패턴**:
- Service='http'인데도 Normal로 분류되거나, ConnectionState='S0'인 경우 Port_Scanning으로 오분류됨

**실제 실패 샘플들**:
```
HTTP_Flood 샘플 1:
  Protocol: tcp
  Service: http
  ConnectionState: S1
  Port: 1880
  OrigPkts: 9
  RespPkts: 9
  FlowPktsPerSec: 9709.04
  → 정확히 분류됨 ✅

HTTP_Flood 샘플 2:
  Protocol: tcp
  Service: -
  ConnectionState: OTH
  Port: 1880
  OrigPkts: 11
  RespPkts: 10
  FlowPktsPerSec: 99864.38
  → 오분류: Arp_Spoofing
```

**차별점**:
- HTTP_Flood: Service='http' AND Port IN (80,443,1880) (ConnectionState는 다양함)
- ConnectionState='S0'이 아닌 경우에만 HTTP_Flood 가능

**개선 방안**:
- Service='http' AND Port IN (80,443,1880) AND ConnectionState != 'S0' → HTTP_Flood
- ConnectionState='S0'인 경우는 Port_Scanning 우선

### 3. Normal 오분류

**실패 패턴**:
- Normal 트래픽이 HTTP_Flood나 Arp_Spoofing으로 오분류됨

**실제 실패 샘플들**:
```
Normal 샘플 1:
  Protocol: tcp
  Service: http
  ConnectionState: S1
  Port: 1880
  OrigPkts: 4
  RespPkts: 3
  FlowPktsPerSec: 7.07
  → 오분류: HTTP_Flood

Normal 샘플 2:
  Protocol: tcp
  Service: -
  ConnectionState: OTH
  Port: 1883
  OrigPkts: 14
  RespPkts: 12
  FlowPktsPerSec: 6.68
  → 오분류: Arp_Spoofing
```

**차별점**:
- Normal: FlowPktsPerSec가 낮음 (median=7.37)
- HTTP_Flood: FlowPktsPerSec가 높음 (median=6579.30)
- Normal: Service='http'이지만 FlowPktsPerSec < 100

**개선 방안**:
- Service='http' AND FlowPktsPerSec < 100 → Normal (HTTP_Flood 아님)
- ConnectionState='OTH' AND OrigPkts > 0 AND RespPkts > 0 → Normal 가능

## 발견된 추가 원시 데이터 차별점

### 1. flow_pkts_per_sec (초당 플로우 패킷 수)

**클래스별 분포**:
- Port_Scanning: median=14652.69 (매우 높음)
- HTTP_Flood: median=6579.30 (높음)
- Normal: median=7.37 (낮음)
- Arp_Spoofing: median=0.00 (거의 0)

**차별점**:
- Port_Scanning vs Arp_Spoofing: 14652.69 vs 0.00 (매우 큰 차이)
- HTTP_Flood vs Normal: 6579.30 vs 7.37 (매우 큰 차이)

### 2. fwd_pkts_per_sec (초당 전송 패킷 수)

**클래스별 분포**:
- Port_Scanning: median=7326.35
- HTTP_Flood: median=3310.42
- Normal: median=3.75
- Arp_Spoofing: median=0.00

### 3. duration (연결 지속 시간)

**클래스별 분포**:
- HTTP_Flood: median=0.01 (매우 짧음)
- Normal: median=4.10 (길음)
- Arp_Spoofing: median=1.69

**차별점**:
- HTTP_Flood vs Normal: 0.01 vs 4.10 (매우 큰 차이)

### 4. fwd_header_size_max (최대 전송 헤더 크기)

**클래스별 분포**:
- HTTP_Flood: median=32.00
- Port_Scanning: median=24.00
- Normal: median=20.00
- Arp_Spoofing: median=8.00

**차별점**:
- Port_Scanning vs Arp_Spoofing: 24.00 vs 8.00

## 개선된 프롬프트 규칙

### 우선순위 규칙:

1. **Protocol 체크** (최우선)
   - Protocol='arp' → Arp_Spoofing
   - Protocol='icmp' → ICMP_Flood
   - Protocol='udp' → UDP_Flood

2. **ConnectionState='S0' 체크** (Port_Scanning 우선)
   - ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0 → Port_Scanning (절대적)
   - ConnectionState='S0' AND OrigPkts>RespPkts → TCP_Flood

3. **ConnectionState='SHR' 체크** (Arp_Spoofing)
   - ConnectionState='SHR' AND OrigPkts=0 AND RespPkts=1 → Arp_Spoofing

4. **Service 체크** (HTTP_Flood, ConnectionState != 'S0'인 경우만)
   - Service='http' AND Port IN (80,443,1880) AND ConnectionState != 'S0' → HTTP_Flood
   - Service='mqtt' AND Port=1883 → MQTT_Flood

5. **Default**
   - Normal

## 문서에 추가할 내용

1. **Port_Scanning 구분 규칙**:
   - ConnectionState='S0' AND OrigPkts=1 AND RespPkts=0 → Port_Scanning (절대적 규칙)
   - FlowPktsPerSec 값과 무관

2. **HTTP_Flood 구분 규칙**:
   - Service='http' AND Port IN (80,443,1880) AND ConnectionState != 'S0' → HTTP_Flood
   - ConnectionState='S0'인 경우는 Port_Scanning 우선

3. **Normal 구분 규칙**:
   - Service='http'이지만 FlowPktsPerSec < 100 → Normal
   - ConnectionState='OTH' AND OrigPkts > 0 AND RespPkts > 0 → Normal 가능

4. **추가 특징 활용**:
   - flow_pkts_per_sec: Port_Scanning (높음) vs Arp_Spoofing (0)
   - duration: HTTP_Flood (짧음) vs Normal (길음)
   - fwd_header_size_max: Port_Scanning (24) vs Arp_Spoofing (8)

