# LLM에게 전달되는 프롬프트 분석

## 프롬프트 구조

LLM에게 전달되는 프롬프트는 다음과 같이 구성됩니다:

### 1. 기본 지시사항
```
You are an expert network security analyst. Classify the following network flow using the comprehensive documentation provided.
```

### 2. 분류할 네트워크 플로우
```
Network Flow to Classify:
Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 2 response). 
Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.17. 
Very short inter-arrival time: -0.129667s (burst traffic pattern). Small payload: -0 bytes.
```

### 3. RAG 컨텍스트 (92.3% 차지)

#### 3.1 Similar Flow Examples
- 유사한 플로우 예시 2개
- 각 예시의 레이블 포함
- 실제 플로우 설명

#### 3.2 Classification Guide for Arp_Spoofing
- Arp_Spoofing이 무엇인지
- 어떻게 동작하는지
- 분류 규칙 (Key Indicators, Feature Value Criteria)
- 구체적인 특징값 범위와 기준

#### 3.3 Detailed Pattern Analysis for Arp_Spoofing
- 주요 구별 특징
- 가장 높은/낮은 값들
- 다른 클래스와의 차이점
- 통계적 분석

#### 3.4 LLM Analyzed Example
- LLM이 분석한 예시
- "왜 이 클래스인지" 설명
- "다른 클래스와의 차이" 설명

### 4. 사용 가능한 클래스 목록
```
Available classes: Normal, Arp_Spoofing, BotNet_DDOS, HTTP_Flood, 
ICMP_Flood, MQTT_Flood, Port_Scanning, TCP_Flood, UDP_Flood
```

### 5. 중요 지시사항
- 분류 가이드, 패턴 분석, 예시 사용
- 구체적인 특징값에 주의
- 예시와 비교
- 가이드의 분류 규칙 따르기

### 6. 단계별 분류 과정
1. 플로우에서 주요 특징 추출
2. 분류 가이드와 비교
3. 패턴 분석에서 구별 특징 확인
4. 유사 예시와 매칭
5. 분류 수행

### 7. 응답 형식
```
Class: [one class name only]

Analysis:
```

## 프롬프트 통계

- **전체 프롬프트 길이**: 14,849자
- **플로우 설명 길이**: 255자 (1.7%)
- **RAG 컨텍스트 길이**: 13,704자 (92.3%)
- **지시사항 길이**: 890자 (6.0%)

## 포함된 문서 유형

1. **Similar Flow Examples** (network_flows 컬렉션)
   - 실제 플로우 예시
   - 레이블 정보

2. **Classification Guides** (classification_guides 컬렉션)
   - 각 클래스의 분류 가이드
   - 분류 규칙
   - 특징값 기준

3. **Detailed Pattern Analysis** (detailed_attack_patterns 컬렉션)
   - 상세한 패턴 분석
   - 구별 특징
   - 통계적 비교

4. **LLM Analyzed Examples** (llm_analyzed_examples 컬렉션)
   - LLM이 분석한 예시
   - 분석 과정 설명

## 문제점 및 개선사항

### 현재 문제점
1. **Arp_Spoofing 샘플인데 ICMP_Flood LLM 분석 예시가 포함됨**
   - 유사도 기반 검색이 정확하지 않을 수 있음
   - 레이블 기반 필터링 필요

2. **Classification Guides가 잘려서 전달될 수 있음**
   - 전체 가이드가 너무 길면 일부만 포함
   - 핵심 부분만 추출하는 로직 필요

### 개선 방안
1. **레이블 기반 필터링 추가**
   - 분류할 샘플의 예상 레이블에 맞는 문서 우선 검색
   - 유사도와 레이블 매칭 결합

2. **문서 요약 개선**
   - 핵심 정보만 추출하는 요약 로직
   - 분류 규칙 부분 우선 포함

3. **프롬프트 길이 최적화**
   - 너무 긴 프롬프트는 모델 성능 저하
   - 핵심 정보만 선별적으로 포함

## 파일 위치

- 전체 프롬프트: `full_prompt_to_llm.txt`
- 프롬프트 생성 스크립트: `show_full_prompt.py`

