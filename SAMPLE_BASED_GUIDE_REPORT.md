# 실제 샘플 기반 가이드 구현 보고서

## 구현 개요

사용자의 요청에 따라 **실제 샘플에서 나오는 패턴을 반영**한 가이드를 생성했습니다. LLM이 샘플을 보고 바로 비교할 수 있도록 구성했습니다.

## 생성된 가이드

### 1. 기본 샘플 기반 가이드
- **파일**: `sample_based_classification_guide.md` (18,767자)
- **내용**: 각 클래스별 실제 샘플 5개 + 패턴 요약

### 2. 개선된 샘플 기반 가이드
- **파일**: `improved_sample_based_guide.md` (9,870자)
- **내용**: 각 클래스별 실제 샘플 3개 + 간결한 패턴 요약

## 가이드 구조

각 클래스별로:

1. **Real Samples from Dataset**
   - 실제 데이터셋에서 추출한 샘플
   - Flow Description (텍스트 변환)
   - Exact Feature Values (정확한 숫자 값)

2. **Typical Value Ranges**
   - 중앙값, 25%ile, 75%ile
   - 전체 범위

3. **How to Classify**
   - 샘플과 직접 비교하는 방법

## 가이드 예시 (Arp_Spoofing)

```
### Arp_Spoofing Sample 1:

**Description**: Total packets: 1 (-0 origin, 1 response). Total bytes: 1 (-0 origin, 1 response). 
Low packet rate: 0.00 packets/second. Balanced bidirectional traffic: ratio 0.12. 
Very short inter-arrival time: -0.014119s (burst traffic pattern). Small payload: -0 bytes.

**Key Feature Values:**
- Fwd Header Max: 2.350975
- Bwd Header Max: 3.183240
- Flow Pkts/Sec: 0.000047
- Resp Pkts: 0.882229
- Resp Bytes: 1.032615
```

## 테스트 결과

### 성능
- **정확도**: 0.0% (0/12)
- 모든 샘플을 Normal로 분류

### 문제점
1. **LLM이 샘플 비교를 하지 않음**
   - 실제 샘플을 제공했지만 비교하지 않음
   - 여전히 Normal로 분류하는 경향

2. **프롬프트가 너무 길 수 있음**
   - 가이드가 9,870-18,767자로 길어서 LLM이 집중하지 못할 수 있음

3. **모델 한계**
   - 1.5B 모델이 복잡한 비교 작업을 수행하기 어려울 수 있음

## 발견 사항

### 실제 샘플 패턴 확인

**Arp_Spoofing 샘플들**:
- Fwd Header Max: 2.35, 2.35, 2.35 (일관됨)
- Bwd Header Max: 3.18, 3.18, 1.37 (대부분 높음)
- Flow Pkts/Sec: 0.000047, 0.000036, 0.082291 (낮음)

**BotNet_DDOS 샘플들**:
- Flow Pkts/Sec: 0.000000 (모두 0)
- Resp Pkts: -0.500293 (음수)
- Resp Bytes: -0.536830 (음수)

**패턴이 명확함**: 실제 샘플들을 보면 각 클래스의 패턴이 명확히 다릅니다.

## 개선 방안

### 1. 프롬프트 단순화
- 가이드를 더 짧게 (핵심만)
- 직접적인 비교 요청
- 예: "Your Bwd Header Max is 3.5. Arp_Spoofing samples show 3.1, 3.2. Are they similar? Yes → Arp_Spoofing"

### 2. Few-shot 예시 추가
- "이 샘플은 Bwd Header Max가 3.5이므로 Arp_Spoofing입니다" 같은 예시
- LLM이 따라할 수 있는 패턴 제공

### 3. 더 큰 모델 사용
- 1.5B 대신 3B 이상 모델 시도
- 또는 GPT-3.5/4 같은 더 강력한 모델

### 4. 규칙 기반 하이브리드
- LLM 대신 규칙 기반 분류기 사용
- LLM은 설명만 생성

## 결론

✅ **성공**: 실제 샘플 패턴을 반영한 가이드 생성 완료
- 실제 데이터셋의 샘플 포함
- 정확한 특징값 포함
- LLM이 비교할 수 있는 구조

❌ **문제**: LLM이 샘플을 비교하지 않음
- 여전히 모든 것을 Normal로 분류
- 프롬프트 개선 필요
- 모델 한계 가능성

## 생성된 파일

- `sample_based_classification_guide.md` - 기본 샘플 기반 가이드
- `improved_sample_based_guide.md` - 개선된 가이드
- `create_sample_based_guide.py` - 가이드 생성 스크립트
- `create_improved_sample_guide.py` - 개선된 가이드 생성 스크립트
- `test_with_sample_guide.py` - 테스트 스크립트
- `test_improved_sample_guide.py` - 개선된 테스트 스크립트

