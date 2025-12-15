# Hugging Face 모델 가이드

## 추천 모델 목록

### 1. 작은 모델 (빠른 추론, 낮은 메모리)

#### Qwen/Qwen2.5-0.5B-Instruct (기본값)
- **크기**: 0.5B 파라미터
- **메모리**: ~1GB RAM
- **속도**: 매우 빠름
- **정확도**: 양호
- **용도**: 빠른 테스트, 제한된 리소스 환경

```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="Qwen/Qwen2.5-0.5B-Instruct"
)
```

#### microsoft/Phi-3-mini-4k-instruct
- **크기**: 3.8B 파라미터
- **메모리**: ~8GB RAM
- **속도**: 빠름
- **정확도**: 좋음
- **용도**: 균형잡힌 선택

```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="microsoft/Phi-3-mini-4k-instruct"
)
```

### 2. 중간 모델 (균형잡힌 성능)

#### meta-llama/Llama-3.2-3B-Instruct
- **크기**: 3B 파라미터
- **메모리**: ~6GB RAM
- **속도**: 중간
- **정확도**: 좋음
- **용도**: 프로덕션 환경

**주의**: Llama 모델은 Hugging Face 허가가 필요할 수 있습니다.

### 3. 큰 모델 (높은 정확도, GPU 권장)

#### mistralai/Mistral-7B-Instruct-v0.2
- **크기**: 7B 파라미터
- **메모리**: ~14GB RAM (GPU 권장)
- **속도**: 느림 (CPU), 빠름 (GPU)
- **정확도**: 매우 좋음
- **용도**: 최고 정확도가 필요한 경우

```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="mistralai/Mistral-7B-Instruct-v0.2",
    device="cuda"  # GPU 사용
)
```

## 모델 선택 가이드

### 리소스별 추천

| 환경 | 추천 모델 | 이유 |
|------|----------|------|
| CPU, 4GB RAM | Qwen2.5-0.5B | 가장 작고 빠름 |
| CPU, 8GB RAM | Phi-3-mini | 좋은 성능/속도 균형 |
| CPU, 16GB RAM | Llama-3.2-3B | 더 나은 정확도 |
| GPU (8GB+) | Mistral-7B | 최고 정확도 |

### 사용 사례별 추천

| 목적 | 추천 모델 |
|------|----------|
| 빠른 프로토타이핑 | Qwen2.5-0.5B |
| 실험 및 개발 | Phi-3-mini |
| 프로덕션 (균형) | Llama-3.2-3B |
| 최고 정확도 | Mistral-7B |

## 모델 다운로드 및 설정

### 1. Hugging Face 계정 설정 (선택사항)

일부 모델은 로그인이 필요할 수 있습니다:

```bash
pip install huggingface_hub
huggingface-cli login
```

### 2. 모델 자동 다운로드

코드 실행 시 자동으로 다운로드됩니다. 첫 실행 시 시간이 걸릴 수 있습니다.

### 3. 수동 다운로드

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen2.5-0.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

## 성능 최적화

### 1. GPU 사용

```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="Qwen/Qwen2.5-0.5B-Instruct",
    device="cuda"  # GPU 사용
)
```

### 2. 양자화 (메모리 절약)

큰 모델 사용 시 양자화로 메모리 사용량을 줄일 수 있습니다:

```python
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config
)
```

### 3. 배치 처리

여러 샘플을 한 번에 처리:

```python
# 향후 구현 예정
predictions = classifier.classify_batch(test_df, batch_size=8)
```

## 문제 해결

### 모델을 찾을 수 없음

```
OSError: Can't load tokenizer for 'model-name'
```

→ 모델 이름 확인, 인터넷 연결 확인

### 메모리 부족

```
RuntimeError: CUDA out of memory
```

→ 더 작은 모델 사용 또는 CPU 사용:
```python
classifier = RAGLLMClassifier(
    vector_store,
    model_name="Qwen/Qwen2.5-0.5B-Instruct",
    device="cpu"
)
```

### 다운로드 속도가 느림

→ Hugging Face 미러 사용 또는 수동 다운로드

## 모델 비교 벤치마크

| 모델 | 정확도 | 속도 (s/sample) | 메모리 (GB) |
|------|--------|----------------|-------------|
| Qwen2.5-0.5B | 85-90% | 0.5-1.0 | 1-2 |
| Phi-3-mini | 88-92% | 1.0-2.0 | 4-8 |
| Llama-3.2-3B | 90-93% | 2.0-3.0 | 6-12 |
| Mistral-7B | 92-95% | 3.0-5.0 | 14-16 |

*실제 성능은 하드웨어와 데이터에 따라 다를 수 있습니다.*

