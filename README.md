# IoT Network Attack Classification with LLM

## 프로젝트 개요
Farm-Flow IoT 데이터셋을 활용한 **설명 가능한 AI 공격 분류 시스템**

- **목표**: AutoML 수준의 정확도 (96.95%) + LLM의 해석 가능성
- **모델**: Qwen2.5-1.5B-Instruct (LoRA fine-tuning)
- **데이터**: 347,685 samples, 7 attack classes
- **핵심 전략**: GPT-4o-mini 기반 데이터 증강 (Paraphrasing vs Feature Variation)

## 주요 성과

### 데이터 증강 효과
| 방법 | Loss (10K) | 개선율 |
|------|-----------|-------|
| Original GPT | 0.3440 | Baseline |
| Feature Variation | 0.1139 | 3.0x ↑ |
| **Paraphrasing** ⭐ | **0.1003** | **3.4x ↑** |

### 핵심 발견
1. **원본 데이터 85.31% 중복** → 데이터 증강 필수
2. **Paraphrasing > Feature Variation** → Feature 통계 보존이 중요
3. **Progressive Training (10K→30K→70K→150K→ALL)** → 단계적 학습 효과적

## 디렉토리 구조

```
iot/
├── RESEARCH_METHODOLOGY.txt              # 전체 연구 방법론 (1,633 lines)
├── DATA_AUGMENTATION_PROMPTS.txt         # 데이터 증강 프롬프트 가이드
│
├── 데이터 생성 스크립트
│   ├── create_gpt_training_data.py       # 원본 GPT 데이터 생성 (347K samples)
│   ├── paraphrase_duplicates.py          # Paraphrasing 증강 (80% 완료)
│   ├── paraphrase_with_feature_variation.py  # Feature Variation 증강
│   ├── progressive_paraphrasing.py       # Progressive 단계별 Paraphrasing
│   ├── progressive_feature_variation.py  # Progressive 단계별 Feature Variation
│   └── split_progressive_datasets.py     # 10K/30K/70K/150K/ALL 분할
│
├── 학습 스크립트
│   ├── finetune_qwen.py                  # Qwen2.5-1.5B LoRA 학습
│   ├── train_paraphrased_10K.py          # Paraphrasing 10K 학습
│   ├── train_paraphrased_30K.py          # Paraphrasing 30K 학습
│   ├── train_feature_varied_10K.py       # Feature Variation 10K 학습
│   ├── train_feature_varied_30K.py       # Feature Variation 30K 학습
│   ├── auto_train_paraphrased_30K.sh     # 자동 학습 스크립트
│   ├── auto_train_feature_varied_30K.sh  # 자동 학습 스크립트
│   └── run_progressive_all.sh            # 전체 Progressive 학습
│
├── 분석 스크립트
│   ├── automl_correct.py                 # AutoML 베이스라인 (96.95%)
│   ├── check_data_leakage.py             # 데이터 중복 분석 (85.31%)
│   ├── compare_raw_samples.py            # 샘플 비교 분석
│   └── analyze_attack_patterns.py        # 공격 패턴 분석
│
├── 문서
│   ├── CLASSIFICATION_GUIDE_REPORT.md    # 분류 가이드 리포트
│   ├── DATABASE_QUALITY_REPORT.md        # 데이터 품질 분석
│   ├── DATA_MISMATCH_SUMMARY.md          # 데이터셋 버전 불일치 분석
│   └── HUGGINGFACE_MODELS.md             # HuggingFace 모델 정보
│
└── 데이터
    ├── train_data_original_size.jsonl    # 원본 GPT 생성 데이터
    ├── train_data_paraphrased.jsonl      # Paraphrasing 증강 데이터
    ├── train_data_feature_varied.jsonl   # Feature Variation 증강 데이터
    ├── train_paraphrased_10K.jsonl       # Progressive 10K
    ├── train_paraphrased_30K.jsonl       # Progressive 30K
    └── ... (70K, 150K, ALL splits)
```

## 빠른 시작

### 1. 환경 설정
```bash
pip install -r requirements_rag.txt
```

### 2. AutoML 베이스라인 실행
```bash
python automl_correct.py
```

### 3. GPT 데이터 생성 (40 Workers 병렬)
```bash
python create_gpt_training_data.py
```

### 4. Progressive Augmentation
```bash
# Paraphrasing Track
python progressive_paraphrasing.py

# Feature Variation Track
python progressive_feature_variation.py
```

### 5. 데이터셋 분할 (10K/30K/70K/150K/ALL)
```bash
python split_progressive_datasets.py
```

### 6. LoRA Fine-tuning
```bash
# Paraphrasing 10K
python train_paraphrased_10K.py

# Feature Variation 10K
python train_feature_varied_10K.py

# 전체 자동 실행
./run_progressive_all.sh
```

## 데이터 증강 전략

### 1. Original GPT Generation
- **Prompt**: 800-1000 단어 상세 분석 요구
- **Temperature**: 0.7
- **결과**: 347,685 samples, 85.31% 중복

### 2. Paraphrasing (⭐ Best)
- **방법**: Reasoning 표현만 다양화
- **Temperature**: 0.8 (높은 다양성)
- **결과**: Loss 0.1003 (3.4x 개선)

### 3. Feature Variation
- **방법**: Feature ±5% 노이즈 + Reasoning 재생성
- **Temperature**: 0.7
- **결과**: Loss 0.1139 (3.0x 개선)

## 비용 분석

| 항목 | 비용 |
|------|------|
| GPT-4o-mini API (원본 생성) | $150 |
| GPT-4o-mini API (Paraphrasing) | $200 |
| GPT-4o-mini API (Feature Variation) | $211 |
| GPU (H100, 예상) | $1,440-$4,400 |
| **총계** | **~$2,000-$5,000** |

## 데이터셋 정보

### Farm-Flow IoT Network Security
- **총 샘플**: 347,685 (논문: 405,296)
- **클래스**: 7개 (논문: 8개, UDP_Flood 누락)
- **Features**: 29개 (Z-score 정규화)
- **Split**: Train 278,148 / Val 69,537 (80:20)

### 클래스 분포
| Class | Samples | Duplication Rate |
|-------|---------|-----------------|
| HTTP_Flood | 57,611 | 97.23% |
| MQTT_Flood | 57,611 | 97.16% |
| Port_Scanning | 57,611 | 95.53% |
| Arp_Spoofing | 57,566 | 91.39% |
| ICMP_Flood | 57,605 | 85.91% |
| TCP_Flood | 57,611 | 46.19% |
| Normal | 2,019 | 41.16% |

## 학습 설정

### Model
- **Base**: Qwen2.5-1.5B-Instruct
- **Method**: LoRA (r=16, alpha=32)
- **Trainable**: 0.28% (6.9M / 2.4B params)

### Training
- **Batch Size**: 2 × 8 gradient accumulation = 16
- **Epochs**: 5
- **Learning Rate**: 2e-4
- **Precision**: bfloat16
- **Hardware**: 2x H100 80GB

### Progressive Strategy
- **10K**: 빠른 실험, 초기 개념 학습
- **30K**: 패턴 강화, 중간 평가
- **70K**: 일반화 능력 향상
- **150K**: 대규모 학습
- **ALL**: 전체 데이터 (278K)

## 추론 최적화 계획

### 현재 성능
- **측정값**: 47초/sample (5 models competing for GPU)
- **예상 (dedicated)**: 6.7-9.4초/sample

### 최적화 전략
1. **GPU Dedication**: 5-7x speedup
2. **Batch Processing** (size 32): 4x speedup
3. **Token Reduction** (512→256): 2x speedup
4. **INT8 Quantization**: 1.5-2x speedup
5. **FlashAttention-2**: 1.2-1.5x speedup

### 목표 성능
- **Conservative**: 1.5-2초/sample (bf16 + batch + Flash)
- **Balanced**: 0.7-1초/sample (INT8 + batch + Flash) ✅
- **Aggressive**: 0.2-0.4초/sample (INT4 + batch + Flash)

### 배포 하드웨어
- **RTX 3060 (12GB)**: Batch 16, INT8, 1-2초/sample ✅ 충분
- **RTX 4090 (24GB)**: Batch 32, INT8, 0.8-1.5초/sample
- **H100 (80GB)**: Batch 64, all optimizations, 0.5-1초/sample

## 참고 문헌

1. Farm-Flow IoT Dataset (2024)
2. Qwen2.5 Technical Report
3. LoRA: Low-Rank Adaptation of Large Language Models
4. AutoGluon: AutoML for Deep Learning

## 라이선스

MIT License

## 연락처

GitHub: [@dlwlsrnjs](https://github.com/dlwlsrnjs)

## Acknowledgments

- OpenAI GPT-4o-mini API
- Alibaba Qwen Team
- H100 GPU Support
