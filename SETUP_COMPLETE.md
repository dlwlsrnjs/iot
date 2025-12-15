# RAG 시스템 설정 완료 가이드

## ✅ 완료된 작업

1. ✅ 가상환경 생성 (`rag_env`)
2. ✅ 필요한 패키지 설치
3. ✅ Hugging Face 모델 통합 (Qwen/Qwen2.5-0.5B-Instruct)
4. ✅ RAG 벡터 데이터베이스 구축 중

## 현재 상태

### 데이터베이스 구축 진행 중
- 다중 분류: 진행 중 (약 40만 개 예상)
- 이진 분류: 대기 중

### 모델
- Hugging Face: Qwen/Qwen2.5-0.5B-Instruct
- 위치: 자동 다운로드됨 (~/.cache/huggingface/)
- 디바이스: CUDA (GPU 사용 가능 시)

## 사용 방법

### 1. 가상환경 활성화

```bash
cd /home/work/skku/iot
source rag_env/bin/activate
```

### 2. 데이터베이스 상태 확인

```bash
python check_rag_status.py
```

### 3. 전체 데이터베이스 구축 (백그라운드)

```bash
# 백그라운드로 실행
nohup python build_full_rag_database.py <<< "y" > build_log.txt 2>&1 &

# 진행 상황 확인
tail -f build_log.txt
```

### 4. 빠른 테스트

```bash
python test_rag_setup.py
```

### 5. 평가 실행

```bash
# 다중 분류 평가 (100개 샘플)
python evaluate_rag_system.py --task multiclass --sample-size 100

# ML 모델과 비교
python evaluate_rag_system.py --task multiclass --sample-size 100 --compare-ml
```

## 파일 구조

```
/home/work/skku/iot/
├── rag_env/                    # 가상환경
├── chroma_db/                  # 벡터 데이터베이스 (자동 생성)
├── rag_llm_system.py          # 핵심 RAG 시스템
├── evaluate_rag_system.py     # 평가 스크립트
├── build_full_rag_database.py # 전체 DB 구축
├── test_rag_setup.py          # 테스트 스크립트
├── check_rag_status.py        # 상태 확인
└── requirements_rag.txt       # 패키지 목록
```

## 주요 명령어

### 데이터베이스 구축
```bash
# 전체 데이터 (약 40만 개, 시간 소요)
python build_full_rag_database.py

# 샘플 데이터 (1000개, 빠른 테스트)
python test_rag_setup.py
```

### 분류 실행
```python
from rag_llm_system import RAGLLMClassifier, RAGVectorStore
import pandas as pd

# 초기화
vector_store = RAGVectorStore()
classifier = RAGLLMClassifier(
    vector_store,
    llm_provider="huggingface",
    model_name="Qwen/Qwen2.5-0.5B-Instruct"
)

# 분류
test_df = pd.read_csv("Datasets/Farm-Flow_Test_Multiclass.csv", nrows=10)
for idx, row in test_df.iterrows():
    pred, conf, ctx = classifier.classify(row, task_type="multiclass")
    print(f"예측: {pred}, 신뢰도: {conf:.2f}")
```

## 문제 해결

### 데이터베이스 구축이 느림
- 정상입니다. 전체 데이터(40만 개)는 시간이 걸립니다
- 백그라운드로 실행하거나 샘플로 먼저 테스트하세요

### 메모리 부족
- 배치 크기를 줄이세요 (기본값: 1000)
- 더 작은 모델 사용: `Qwen/Qwen2.5-0.5B-Instruct`

### 모델 다운로드 실패
- 인터넷 연결 확인
- Hugging Face 로그인: `huggingface-cli login`

## 다음 단계

1. 데이터베이스 구축 완료 대기
2. 평가 실행하여 성능 확인
3. 필요시 모델 변경 (더 큰 모델 = 더 정확)
4. 프롬프트 튜닝으로 성능 개선

## 참고 문서

- `RAG_SYSTEM_GUIDE.md`: 상세 사용 가이드
- `HUGGINGFACE_MODELS.md`: 모델 선택 가이드
- `CHANGELOG_HUGGINGFACE.md`: 변경사항

