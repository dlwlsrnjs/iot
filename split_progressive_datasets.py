#!/usr/bin/env python3
"""
단계별 파일을 train/val로 split (80:20)
- Paraphrasing 버전
- Feature 변형 버전
"""

import json
import random

VERSIONS = [
    ("train_data_paraphrased.jsonl", "10K", "para"),
    ("train_data_paraphrased_30K.jsonl", "30K", "para"),
    ("train_data_paraphrased_70K.jsonl", "70K", "para"),
    ("train_data_paraphrased_150K.jsonl", "150K", "para"),
    ("train_data_paraphrased_ALL.jsonl", "ALL", "para"),
    ("train_data_feature_varied.jsonl", "10K", "feat"),
    ("train_data_feature_varied_30K.jsonl", "30K", "feat"),
    ("train_data_feature_varied_70K.jsonl", "70K", "feat"),
    ("train_data_feature_varied_150K.jsonl", "150K", "feat"),
    ("train_data_feature_varied_ALL.jsonl", "ALL", "feat"),
]

print("=" * 80)
print("Train/Val Split (80:20)")
print("=" * 80)

for input_file, stage, version_type in VERSIONS:
    print(f"\n[처리] {input_file}")
    
    # 데이터 로드
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]
    except FileNotFoundError:
        print(f"  ⚠️  파일 없음 (아직 생성 안 됨)")
        continue
    
    print(f"  총 샘플: {len(data):,}개")
    
    # 셔플
    random.seed(42)  # 재현성
    random.shuffle(data)
    
    # 80:20 split
    split_idx = int(len(data) * 0.8)
    train_data = data[:split_idx]
    val_data = data[split_idx:]
    
    # 파일명
    if version_type == "para":
        train_file = f"train_paraphrased_{stage}.jsonl"
        val_file = f"val_paraphrased_{stage}.jsonl"
    else:
        train_file = f"train_feature_varied_{stage}.jsonl"
        val_file = f"val_feature_varied_{stage}.jsonl"
    
    # 저장
    with open(train_file, 'w', encoding='utf-8') as f:
        for sample in train_data:
            f.write(json.dumps(sample, ensure_ascii=False) + '\n')
    
    with open(val_file, 'w', encoding='utf-8') as f:
        for sample in val_data:
            f.write(json.dumps(sample, ensure_ascii=False) + '\n')
    
    print(f"  ✓ Train: {train_file} ({len(train_data):,}개)")
    print(f"  ✓ Val: {val_file} ({len(val_data):,}개)")

print("\n" + "=" * 80)
print("✓ 모든 split 완료!")
print("=" * 80)
print("""
생성된 파일 (Paraphrasing):
- train_paraphrased_10K.jsonl / val_paraphrased_10K.jsonl
- train_paraphrased_30K.jsonl / val_paraphrased_30K.jsonl
- train_paraphrased_70K.jsonl / val_paraphrased_70K.jsonl
- train_paraphrased_150K.jsonl / val_paraphrased_150K.jsonl
- train_paraphrased_ALL.jsonl / val_paraphrased_ALL.jsonl

생성된 파일 (Feature 변형):
- train_feature_varied_10K.jsonl / val_feature_varied_10K.jsonl
- train_feature_varied_30K.jsonl / val_feature_varied_30K.jsonl
- train_feature_varied_70K.jsonl / val_feature_varied_70K.jsonl
- train_feature_varied_150K.jsonl / val_feature_varied_150K.jsonl
- train_feature_varied_ALL.jsonl / val_feature_varied_ALL.jsonl
""")
