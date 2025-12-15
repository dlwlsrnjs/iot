# RAG 기반 LLM 시스템 가이드

## 개요

이 시스템은 IoT 네트워크 트래픽 분류를 위해 Retrieval-Augmented Generation (RAG)을 활용한 LLM 기반 분류기를 제공합니다. 전통적인 머신러닝 모델보다 높은 성능을 목표로 합니다.

## 시스템 아키텍처

```
┌─────────────────┐
│  Network Flow   │
│     Data        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Flow to Text    │  네트워크 플로우 특징을 의미있는 텍스트로 변환
│   Converter     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Vector Store   │  유사한 패턴 검색 (ChromaDB + Sentence Transformers)
│  (ChromaDB)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LLM Classifier │  컨텍스트 기반 분류 (OpenAI GPT)
│   (OpenAI)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Classification │
│     Result      │
└─────────────────┘
```

## 핵심 아이디어

### 1. 텍스트 변환 (Flow to Text)
- 네트워크 플로우의 수치적 특징을 자연어 설명으로 변환
- 예: "High packet rate: 1500 packets/second, asymmetric traffic pattern"
- 도메인 지식 통합 (공격 유형별 특징 패턴)

### 2. 유사 패턴 검색 (Retrieval)
- 벡터 임베딩을 사용하여 유사한 트래픽 패턴 검색
- 학습 데이터에서 가장 유사한 K개 예제 추출
- LLM에 컨텍스트 제공

### 3. LLM 기반 분류 (Generation)
- 검색된 유사 예제를 컨텍스트로 활용
- LLM의 추론 능력을 활용한 정확한 분류
- 도메인 지식과 패턴 인식 결합

## 설치 방법

### 1. 의존성 설치

```bash
pip install -r requirements_rag.txt
```

### 2. Hugging Face 모델 사용 (기본값, API 키 불필요)

시스템은 기본적으로 Hugging Face의 로컬 모델을 사용합니다. API 키가 필요 없습니다.

**권장 모델:**
- `Qwen/Qwen2.5-0.5B-Instruct` (기본값, 작고 빠름)
- `microsoft/Phi-3-mini-4k-instruct` (작고 효율적)
- `mistralai/Mistral-7B-Instruct-v0.2` (더 정확하지만 더 큼)

**OpenAI 사용 (선택사항):**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 사용 방법

### 1. 벡터 데이터베이스 구축

```python
from rag_llm_system import (
    RAGVectorStore, 
    FlowToTextConverter, 
    build_rag_database
)

# 초기화
converter = FlowToTextConverter()
vector_store = RAGVectorStore(persist_directory="./chroma_db")

# 데이터베이스 구축 (다중 분류)
build_rag_database(
    csv_path="Datasets/Farm-Flow_Train_Multiclass.csv",
    vector_store=vector_store,
    converter=converter,
    task_type="multiclass",
    sample_size=50000,  # 전체 데이터 사용 시 None
    label_column="traffic"
)
```

### 2. 분류 수행

```python
from rag_llm_system import RAGLLMClassifier, RAGVectorStore
import pandas as pd

# 분류기 초기화 (Hugging Face 모델 사용)
vector_store = RAGVectorStore()
classifier = RAGLLMClassifier(
    vector_store,
    llm_provider="huggingface",
    model_name="Qwen/Qwen2.5-0.5B-Instruct"  # 또는 다른 모델
)

# OpenAI 사용 시
# classifier = RAGLLMClassifier(
#     vector_store,
#     llm_provider="openai",
#     model_name="gpt-4o-mini"
# )

# 테스트 데이터 로드
test_df = pd.read_csv("Datasets/Farm-Flow_Test_Multiclass.csv", nrows=10)

# 분류
for idx, row in test_df.iterrows():
    predicted_label, confidence, context = classifier.classify(
        row, 
        task_type="multiclass",
        top_k=5
    )
    print(f"Sample {idx}: {predicted_label} (confidence: {confidence:.2f})")
```

### 3. 평가 스크립트 실행

```bash
# 기본 평가 (100개 샘플)
python evaluate_rag_system.py --task multiclass --sample-size 100

# ML 모델과 비교
python evaluate_rag_system.py --task multiclass --sample-size 100 --compare-ml

# 이진 분류 평가
python evaluate_rag_system.py --task binary --sample-size 100
```

## 성능 향상 전략

### 1. 데이터베이스 크기 최적화
- **더 많은 학습 데이터 사용**: `sample_size=None`으로 전체 데이터 사용
- **균형잡힌 샘플링**: 각 클래스에서 동일한 수의 샘플 선택

### 2. 프롬프트 엔지니어링
- **도메인 지식 강화**: 공격 유형별 특징을 프롬프트에 명시
- **Few-shot 예제**: 검색된 예제 외에 대표적인 패턴 예제 추가
- **체인 오브 사고**: 단계별 추론 과정 요청

### 3. 검색 전략 개선
- **하이브리드 검색**: 키워드 검색 + 벡터 검색 결합
- **재랭킹**: 초기 검색 결과를 더 정교한 모델로 재랭킹
- **메타데이터 필터링**: 특정 공격 유형에 대한 검색 범위 제한

### 4. LLM 모델 선택

**Hugging Face 모델 (기본, 추천):**
- **Qwen/Qwen2.5-0.5B-Instruct**: 작고 빠름, 기본값
- **microsoft/Phi-3-mini-4k-instruct**: 효율적이고 정확
- **mistralai/Mistral-7B-Instruct-v0.2**: 더 정확하지만 더 큼 (GPU 권장)
- **meta-llama/Llama-3.2-3B-Instruct**: 균형잡힌 성능

**OpenAI 모델 (선택사항):**
- **GPT-4**: 더 높은 정확도 (비용 증가)
- **GPT-4o-mini**: 속도와 비용의 균형

### 5. 앙상블 방법
- **다중 검색**: 다른 임베딩 모델로 여러 번 검색
- **투표 기반**: 여러 LLM 응답의 다수결
- **확률 가중**: LLM의 confidence score 활용

## 예상 성능 개선 포인트

### RAG의 장점
1. **컨텍스트 이해**: 유사한 패턴을 참고하여 더 정확한 판단
2. **도메인 지식 활용**: 공격 패턴에 대한 사전 지식 통합
3. **적응성**: 새로운 패턴에 대한 설명 가능한 추론
4. **불균형 데이터 처리**: 소수 클래스에 대한 더 나은 이해

### 전통적 ML의 한계
1. **고정된 특징 공간**: 학습 데이터에만 의존
2. **패턴 일반화 어려움**: 새로운 변형에 취약
3. **설명 불가능성**: 블랙박스 모델

## 실험 결과 해석

평가 스크립트는 다음 메트릭을 제공합니다:
- **Accuracy**: 전체 정확도
- **Precision**: 정밀도 (weighted average)
- **Recall**: 재현율 (weighted average)
- **F1-Score**: F1 점수 (weighted average)
- **Inference Time**: 샘플당 추론 시간

## 고급 사용법

### 커스텀 프롬프트

```python
class CustomRAGClassifier(RAGLLMClassifier):
    def _build_multiclass_prompt(self, query_text: str, context: str) -> str:
        return f"""당신은 IoT 네트워크 보안 전문가입니다.
        
다음 네트워크 플로우를 분석하고 공격 유형을 분류하세요.

분석 대상:
{query_text}

참고 예제:
{context}

단계별로 분석하세요:
1. 패킷 패턴 분석
2. 트래픽 특성 파악
3. 공격 유형 판단

분류 결과만 출력하세요."""
```

### 다른 임베딩 모델 사용

```python
from sentence_transformers import SentenceTransformer

# 더 큰 모델 사용 (더 정확하지만 느림)
vector_store.embedding_model = SentenceTransformer('all-mpnet-base-v2')
```

## 문제 해결

### 1. 모델 다운로드 오류
```
OSError: Can't load tokenizer
```
→ 인터넷 연결 확인, Hugging Face 계정 로그인 필요할 수 있음:
```bash
huggingface-cli login
```

### 2. 메모리 부족 (CUDA out of memory)
→ 더 작은 모델 사용:
```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="Qwen/Qwen2.5-0.5B-Instruct",  # 작은 모델
    device="cpu"  # CPU 사용
)
```

### 3. OpenAI API 키 오류 (OpenAI 사용 시)
```
ValueError: OpenAI API key not provided
```
→ 환경 변수 `OPENAI_API_KEY` 설정 확인

### 2. 메모리 부족
→ `sample_size` 파라미터로 데이터 크기 제한

### 3. 느린 추론 속도
→ `top_k` 파라미터 감소 (기본값: 5 → 3)
→ 더 작은 LLM 모델 사용 (Qwen2.5-0.5B-Instruct)
→ GPU 사용 (CUDA가 있으면 자동 사용)
→ 배치 처리 구현

### 4. 낮은 정확도
→ 벡터 데이터베이스 크기 증가
→ 더 많은 학습 데이터 사용
→ 프롬프트 개선

## 참고 자료

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- RAG 논문: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"

## 라이선스

이 코드는 연구 및 교육 목적으로 제공됩니다.

