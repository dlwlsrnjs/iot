# Hugging Face 모델 통합 변경사항

## 주요 변경사항

### ✅ Hugging Face 모델 지원 추가

시스템이 이제 Hugging Face의 오픈소스 LLM 모델을 사용할 수 있습니다.

### 변경된 파일

1. **rag_llm_system.py**
   - `RAGLLMClassifier` 클래스에 Hugging Face 지원 추가
   - 기본 LLM 프로바이더를 `huggingface`로 변경
   - `transformers` 라이브러리 통합
   - 로컬 모델 실행 지원 (API 키 불필요)

2. **requirements_rag.txt**
   - `transformers>=4.30.0` 추가
   - `accelerate>=0.20.0` 추가
   - OpenAI는 선택사항으로 변경

3. **evaluate_rag_system.py**
   - 기본 LLM 프로바이더를 `huggingface`로 변경

4. **quick_start_rag.py**
   - API 키 입력 제거
   - Hugging Face 모델 사용으로 변경

5. **RAG_SYSTEM_GUIDE.md**
   - Hugging Face 사용법 추가
   - 모델 선택 가이드 업데이트

6. **HUGGINGFACE_MODELS.md** (신규)
   - Hugging Face 모델 상세 가이드
   - 모델 비교 및 선택 가이드

## 사용법 변경

### 이전 (OpenAI)
```python
classifier = RAGLLMClassifier(
    vector_store,
    llm_provider="openai",
    model_name="gpt-4o-mini",
    api_key="your-key"
)
```

### 현재 (Hugging Face - 기본값)
```python
classifier = RAGLLMClassifier(
    vector_store,
    llm_provider="huggingface",  # 기본값
    model_name="Qwen/Qwen2.5-0.5B-Instruct"
)
```

### OpenAI 사용 (여전히 지원)
```python
classifier = RAGLLMClassifier(
    vector_store,
    llm_provider="openai",
    model_name="gpt-4o-mini"
)
```

## 장점

1. **비용 절감**: API 호출 비용 없음
2. **프라이버시**: 데이터가 로컬에서 처리됨
3. **오프라인 사용**: 인터넷 연결 불필요 (모델 다운로드 후)
4. **커스터마이징**: 모델 파인튜닝 가능

## 주의사항

1. **첫 실행 시**: 모델 다운로드로 시간이 걸릴 수 있음
2. **메모리 요구사항**: 모델 크기에 따라 다름 (0.5B ~ 7B)
3. **GPU 권장**: 큰 모델 사용 시 GPU가 있으면 더 빠름

## 추천 모델

- **빠른 테스트**: `Qwen/Qwen2.5-0.5B-Instruct` (기본값)
- **균형**: `microsoft/Phi-3-mini-4k-instruct`
- **정확도**: `mistralai/Mistral-7B-Instruct-v0.2` (GPU 권장)

## 마이그레이션 가이드

기존 OpenAI 코드를 사용 중이라면:
1. `llm_provider="openai"` 명시적으로 지정
2. 또는 코드 수정 없이 그대로 사용 가능 (기본값이 변경됨)

Hugging Face로 전환하려면:
1. `pip install -r requirements_rag.txt` 실행
2. 코드에서 `llm_provider="huggingface"` 지정
3. 원하는 모델 이름 지정

