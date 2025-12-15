# 입력 프롬프트와 샘플 형태 요약

## 샘플 데이터 형태

### 1. 원본 데이터 (pandas Series)
- **데이터 타입**: `pandas.core.series.Series`
- **총 특징 수**: 31개
- **주요 특징값들**:
  - `orig_pkts`: 원본 패킷 수 (정규화된 값, 예: -0.0678)
  - `resp_pkts`: 응답 패킷 수 (정규화된 값, 예: 0.8822)
  - `orig_ip_bytes`: 원본 IP 바이트 수
  - `resp_ip_bytes`: 응답 IP 바이트 수
  - `fwd_pkts_per_sec`: 전송 패킷/초
  - `bwd_pkts_per_sec`: 수신 패킷/초
  - `flow_pkts_per_sec`: 플로우 패킷/초
  - `fwd_header_size_max`: 전송 헤더 크기 최대값
  - `bwd_header_size_max`: 수신 헤더 크기 최대값
  - `fwd_iat.avg`: 전송 패킷 간 평균 시간
  - `bwd_iat.avg`: 수신 패킷 간 평균 시간
  - `down_up_ratio`: 다운로드/업로드 비율
  - `traffic`: 레이블 (0=Normal, 1=Arp_Spoofing, 2=BotNet_DDOS, ...)

### 2. 텍스트로 변환된 형태

**FlowToTextConverter**를 통해 자연어로 변환:

#### Arp_Spoofing 예시:
```
Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 2 response). 
Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.17. 
Very short inter-arrival time: -0.129667s (burst traffic pattern). Small payload: -0 bytes.
```

#### BotNet_DDOS 예시:
```
Low packet rate: 0.00 packets/second. Highly asymmetric traffic: download/upload ratio 0.00 (mostly upload). 
Very short inter-arrival time: -0.167367s (burst traffic pattern). Small payload: -0 bytes.
```

**특징**:
- 숫자 값들이 자연어 설명으로 변환됨
- 패턴 특성 설명 포함 (예: "burst traffic pattern")
- 텍스트 길이: 약 200-255자

### 3. RAG 컨텍스트

#### Similar Flow Examples
- 유사한 플로우 예시 2개
- 각 예시의 레이블 포함
- 실제 플로우 설명

#### Classification Guide
- 분류 가이드 (현재는 Normal 가이드가 검색됨 - 문제점)
- 분류 규칙
- 특징값 기준

## LLM에게 전달되는 전체 프롬프트 구조

```
You are an expert network security analyst. Classify the following network flow using the comprehensive documentation provided.

Network Flow to Classify:
[텍스트로 변환된 플로우 설명]

## Similar Flow Examples:
[유사한 플로우 예시들]

## Classification Guide:
[분류 가이드]

Available classes: Normal, Arp_Spoofing, BotNet_DDOS, HTTP_Flood, ICMP_Flood, MQTT_Flood, Port_Scanning, TCP_Flood, UDP_Flood

IMPORTANT: 
- Use the classification guides, pattern analyses, and examples above
- Pay attention to specific feature values mentioned in the guides
- Compare the flow's characteristics with the examples
- Follow the classification rules provided in the guides

Step-by-step classification:
1. Extract key features from the flow (packet rate, bytes, header size, etc.)
2. Compare with the classification guides above
3. Check the pattern analyses for distinguishing features
4. Match with similar examples
5. Make your classification

Respond in this exact format:
Class: [one class name only]

Analysis:
```

## 프롬프트 통계

### Arp_Spoofing 샘플:
- 전체 프롬프트 길이: 1,949자
- 플로우 설명: 255자 (13.1%)
- RAG 컨텍스트: 804자 (41.2%)

### BotNet_DDOS 샘플:
- 전체 프롬프트 길이: 1,894자
- 플로우 설명: 200자 (10.6%)
- RAG 컨텍스트: 804자 (42.5%)

## 발견된 문제점

### 1. 잘못된 가이드 검색
- **Arp_Spoofing 샘플**인데 **Normal 가이드**가 검색됨
- **BotNet_DDOS 샘플**인데 **Normal 가이드**가 검색됨
- **HTTP_Flood 샘플**인데 **Normal 가이드**가 검색됨

**원인**: 유사도 기반 검색이 정확하지 않음

### 2. 유사 플로우 예시도 부정확
- BotNet_DDOS 샘플인데 Arp_Spoofing 예시가 검색됨
- HTTP_Flood 샘플인데 Arp_Spoofing 예시가 검색됨

**원인**: 텍스트 변환 후 유사도가 낮아서 잘못된 예시가 검색됨

### 3. 특징값 정보 손실
- 원본 데이터의 정확한 숫자 값들이 텍스트 변환 과정에서 손실됨
- 예: `fwd_header_size_max: 1.478` → 텍스트에서는 "Low packet rate"로만 표현

## 개선 방안

### 1. 레이블 기반 필터링
- 샘플의 예상 레이블에 맞는 가이드 우선 검색
- 유사도와 레이블 매칭 결합

### 2. 특징값 직접 포함
- 텍스트 변환 시 정확한 숫자 값도 포함
- 예: "Fwd Header Size Max: 1.478 (very high)"

### 3. 프롬프트 개선
- 특징값 비교를 명시적으로 요청
- "Check if fwd_header_size_max > 1.5" 같은 구체적 지시

## 저장된 파일

- `prompt_sample_Arp_Spoofing.txt`: Arp_Spoofing 샘플의 전체 프롬프트
- `prompt_sample_BotNet_DDOS.txt`: BotNet_DDOS 샘플의 전체 프롬프트
- `prompt_sample_HTTP_Flood.txt`: HTTP_Flood 샘플의 전체 프롬프트
- `prompt_sample_ICMP_Flood.txt`: ICMP_Flood 샘플의 전체 프롬프트

