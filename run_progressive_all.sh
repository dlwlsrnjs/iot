#!/bin/bash
# 단계적 데이터 생성 완전 자동화
# Paraphrasing + Feature 변형 동시 실행 + 자동 split

echo "=================================================================="
echo "단계적 데이터 생성 자동화 시작"
echo "=================================================================="

# 1. Progressive paraphrasing 시작
echo ""
echo "[1] Progressive Paraphrasing 시작 (40 workers)..."
nohup python progressive_paraphrasing.py > progressive_paraphrasing.log 2>&1 &
PARA_PID=$!
echo "  프로세스: $PARA_PID"

# 2. Progressive feature variation 시작
echo ""
echo "[2] Progressive Feature Variation 시작 (40 workers)..."
nohup python progressive_feature_variation.py > progressive_feature_variation.log 2>&1 &
FEAT_PID=$!
echo "  프로세스: $FEAT_PID"

echo ""
echo "=================================================================="
echo "두 프로세스 병렬 실행 중"
echo "=================================================================="
echo "Paraphrasing PID: $PARA_PID"
echo "Feature Variation PID: $FEAT_PID"
echo ""
echo "모니터링:"
echo "  tail -f progressive_paraphrasing.log"
echo "  tail -f progressive_feature_variation.log"
echo ""
echo "완료 대기 중... (12-15시간 예상)"

# 3. 완료 대기
wait $PARA_PID
PARA_EXIT=$?
echo ""
echo "[완료] Paraphrasing (exit code: $PARA_EXIT)"

wait $FEAT_PID
FEAT_EXIT=$?
echo "[완료] Feature Variation (exit code: $FEAT_EXIT)"

# 4. 자동 split
echo ""
echo "=================================================================="
echo "[3] Train/Val Split 자동 실행..."
echo "=================================================================="
python split_progressive_datasets.py

echo ""
echo "=================================================================="
echo "✓ 모든 작업 완료!"
echo "=================================================================="
echo ""
echo "생성된 단계별 파일:"
echo "  10K, 30K, 70K, 150K, ALL"
echo ""
echo "각 단계마다:"
echo "  - train_paraphrased_XXX.jsonl / val_paraphrased_XXX.jsonl"
echo "  - train_feature_varied_XXX.jsonl / val_feature_varied_XXX.jsonl"
echo ""
echo "다음 단계: 각 단계별로 학습 및 평가"
