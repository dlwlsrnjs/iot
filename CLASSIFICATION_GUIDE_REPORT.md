# 분류 가이드 문서 생성 보고서

## 실행 개요

### 목적
LLM이 실제로 분류를 수행할 때 필요한 실용적인 정보를 제공하는 문서 생성

### 핵심 인사이트
**"분류를 잘하려면 분류에 필요한 정보가 문서에 있어야 한다"**

기존 문서는 통계에 치우쳐 있었지만, 실제 분류에는:
- 각 공격 유형이 무엇인지 (개념)
- 어떻게 동작하는지 (행동 패턴)
- 어떤 특징값을 확인해야 하는지 (분류 규칙)
- 실제 예시

등이 필요합니다.

## 생성된 문서

### 문서 구조
각 분류 가이드 문서는 다음을 포함:

1. **What is [Class]?** - 개념 설명
   - 공격 유형의 정의
   - 정상 트래픽의 특성

2. **How does [Class] behave?** - 동작 방식
   - 네트워크에서 어떻게 나타나는지
   - 패턴 설명

3. **Classification Rules** - 분류 규칙
   - Key Indicators: 주요 지표
   - Feature Value Criteria: 특징값 기준
   - Classification Rule: 구체적인 판단 기준

4. **How to Distinguish** - 구별 방법
   - 다른 클래스와의 차이점

5. **Practical Classification Example** - 실전 예시
   - 실제 플로우 분석 예시
   - 단계별 분석 과정

6. **Quick Reference** - 빠른 참조
   - Decision Tree
   - 체크리스트

### 생성된 문서 목록

1. **Normal_classification_guide.md** (3,996자)
   - 정상 트래픽의 개념과 특성
   - 균형잡힌 통신 패턴 설명

2. **Arp_Spoofing_classification_guide.md** (5,254자)
   - ARP 스푸핑 개념
   - 헤더 크기 기반 분류 규칙
   - 주요 지표: Fwd Header Size Max > 1.5

3. **BotNet_DDOS_classification_guide.md** (1,834자)
   - 봇넷 DDoS 개념
   - 높은 패킷 비율 기반 분류

4. **HTTP_Flood_classification_guide.md** (2,781자)
   - HTTP 플러드 개념
   - HTTP 요청 비율 기반 분류

5. **ICMP_Flood_classification_guide.md** (4,492자)
   - ICMP 플러드 개념
   - ICMP 패킷 비율 기반 분류

6. **MQTT_Flood_classification_guide.md** (1,730자)
   - MQTT 플러드 개념
   - MQTT 메시지 비율 기반 분류

7. **Port_Scanning_classification_guide.md** (1,822자)
   - 포트 스캔 개념
   - 다중 포트 접근 패턴 기반 분류

8. **TCP_Flood_classification_guide.md** (1,776자)
   - TCP 플러드 개념
   - TCP 연결 시도 기반 분류

## 주요 개선 사항

### 이전 문서 (통계 중심)
- ❌ 통계 수치만 나열
- ❌ "어떻게 분류해야 하는지" 불명확
- ❌ 개념 설명 부족
- ❌ 실전 활용 어려움

### 새로운 문서 (분류 중심)
- ✅ 개념 설명 포함
- ✅ 동작 방식 설명
- ✅ 구체적인 분류 규칙
- ✅ 특징값 기준 제시
- ✅ 실전 예시 제공
- ✅ Decision Tree 포함

## 분류 규칙 예시

### Arp_Spoofing 분류 규칙
```
Key Indicators:
- Fwd Header Size Max > 1.5 (very high compared to other classes)
- Fwd Header Size Min > 1.5 (very high)
- Bwd Header Size Max > 2.0 (very high)
- Flow Pkts Per Sec > 0.3 (high packet rate)
- Short inter-arrival times (burst pattern)

Classification Rules:
- If Bwd Header Size Max > 1.374, it strongly suggests Arp_Spoofing
- If Fwd Header Size Min > 1.566, it strongly suggests Arp_Spoofing
- If Fwd Header Size Max > 1.478, it strongly suggests Arp_Spoofing
```

### Normal 분류 규칙
```
Key Indicators:
- Balanced bidirectional communication
- Regular packet intervals
- Moderate packet sizes
- Expected protocol patterns

Classification Rules:
- If Bwd Header Size Tot > 0.523, it strongly suggests Normal
- If Fwd Header Size Tot > 0.227, it strongly suggests Normal
- If Resp Pkts > 0.882, it suggests Normal
```

## RAG 데이터베이스 통합

### 추가된 컬렉션
- **classification_guides**: 8개 분류 가이드 문서
- 검색 테스트: ✅ 정상 작동

### 검색 예시
- "How to classify ARP spoofing attacks?" → Arp_Spoofing 가이드 검색 ✅
- "What are the classification rules for normal traffic?" → Normal 가이드 검색 ✅
- "How to identify HTTP flood attacks?" → HTTP_Flood 가이드 검색 ✅

## 테스트 결과

### 현재 상태
- 분류 가이드 문서: ✅ 생성 완료
- RAG 통합: ✅ 완료
- 검색 기능: ✅ 정상 작동

### 성능 이슈
- 현재 테스트에서 모든 샘플이 Normal로 예측됨
- **원인 분석 필요**:
  1. 플로우 데이터베이스가 올바른 라벨로 구축되지 않음
  2. 프롬프트 최적화 필요
  3. LLM이 가이드를 충분히 활용하지 못함

## 다음 단계

### 즉시 개선
1. **플로우 데이터베이스 재구축**
   - 올바른 라벨로 전체 데이터베이스 재구축
   - 클래스 균형 샘플링

2. **프롬프트 최적화**
   - 분류 가이드의 핵심 정보를 더 명확히 강조
   - 단계별 분석 과정 명시

3. **가이드 개선**
   - 더 구체적인 임계값 제시
   - 더 많은 예시 추가

### 장기 개선
1. **하이브리드 검색**
   - 통계 문서 + 분류 가이드 + 유사 예제 결합
   - 각 문서 유형의 가중치 조정

2. **동적 가이드 생성**
   - 쿼리 기반 맞춤 가이드 생성
   - 실시간 임계값 계산

3. **검증 및 개선**
   - 오분류 사례 분석
   - 가이드 업데이트

## 결론

### 성공한 부분
✅ **분류 가이드 문서 생성**: LLM이 실제로 분류할 때 필요한 정보 제공
✅ **구조화된 정보**: 개념, 동작, 규칙, 예시 포함
✅ **RAG 통합**: 검색 기능 정상 작동

### 개선 필요
⚠️ **데이터베이스 재구축**: 올바른 라벨로 플로우 데이터 재구축 필요
⚠️ **프롬프트 최적화**: 가이드를 더 효과적으로 활용하도록 개선
⚠️ **성능 검증**: 재구축 후 성능 재평가 필요

**전체 평가**: 분류 가이드 문서가 성공적으로 생성되어 LLM이 실제 분류에 필요한 정보를 제공합니다. 데이터베이스 재구축과 프롬프트 최적화를 통해 분류 성능이 크게 개선될 것으로 예상됩니다.

## 생성된 파일

### 분석 스크립트
- `create_classification_guide.py` - 분류 가이드 생성
- `add_classification_guides_to_rag.py` - RAG DB에 추가
- `test_with_classification_guides.py` - 테스트

### 문서
- `rag_classification_guides/*.md` - 8개 분류 가이드 문서
- `rag_classification_guides/classification_guides.json` - JSON 메타데이터

