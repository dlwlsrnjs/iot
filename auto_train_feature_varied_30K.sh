#!/bin/bash
# 30K 파일 완성 감시 후 자동 학습 시작 - Feature Variation 버전

echo "=========================================="
echo "30K Feature Variation 파일 감시 및 자동 학습"
echo "=========================================="

TARGET_FILE="train_data_feature_varied_30K.jsonl"
ORIGINAL_SIZE=$(stat -c%s train_data_feature_varied.jsonl)
CHECK_INTERVAL=60  # 60초마다 체크

echo "원본 파일 크기: $ORIGINAL_SIZE bytes"
echo "대상 파일: $TARGET_FILE"
echo "감시 시작..."

# Split 스크립트 실행 대기
while true; do
    if [ -f "$TARGET_FILE" ]; then
        CURRENT_SIZE=$(stat -c%s "$TARGET_FILE")
        CURRENT_TIME=$(date '+%Y-%m-%d %H:%M:%S')
        
        echo "[$CURRENT_TIME] 현재 크기: $CURRENT_SIZE bytes"
        
        # 원본과 크기가 같거나 크면 (약간의 여유 허용)
        if [ $CURRENT_SIZE -ge $ORIGINAL_SIZE ]; then
            echo ""
            echo "✓ 30K 파일 생성 완료 감지!"
            echo "  크기: $CURRENT_SIZE bytes"
            
            # 10초 대기 (파일 쓰기 완전 완료 보장)
            echo "  안정화 대기 10초..."
            sleep 10
            
            # Split 실행
            echo ""
            echo "=========================================="
            echo "Train/Val Split 실행 중..."
            echo "=========================================="
            python split_progressive_datasets.py
            
            # Train/Val 파일 생성 확인
            if [ -f "train_feature_varied_30K.jsonl" ] && [ -f "val_feature_varied_30K.jsonl" ]; then
                echo ""
                echo "✓ Train/Val Split 완료"
                echo "  train_feature_varied_30K.jsonl: $(stat -c%s train_feature_varied_30K.jsonl) bytes"
                echo "  val_feature_varied_30K.jsonl: $(stat -c%s val_feature_varied_30K.jsonl) bytes"
                
                # 학습 시작
                echo ""
                echo "=========================================="
                echo "30K Feature Variation 학습 시작!"
                echo "=========================================="
                
                # 학습 스크립트 생성
                cat > train_feature_varied_30K.py << 'EOFPYTHON'
#!/usr/bin/env python3
"""
Qwen 모델 파인튜닝 - Feature Variation 30K
"""
import json
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import Dataset
from peft import LoraConfig, get_peft_model, TaskType

print("=" * 100)
print("Qwen2.5-1.5B 파인튜닝 - Feature Variation 30K")
print("=" * 100)

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

print("\n[1단계] JSONL 데이터 로드...")
train_data = load_jsonl('train_feature_varied_30K.jsonl')
val_data = load_jsonl('val_feature_varied_30K.jsonl')
print(f"✓ 학습 데이터: {len(train_data):,}개")
print(f"✓ 검증 데이터: {len(val_data):,}개")

print("\n[2단계] Qwen2.5-1.5B 모델 로드...")
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
print(f"✓ 모델 로드 완료")

print("\n[3단계] LoRA 설정...")
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    bias="none"
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

print("\n[4단계] 데이터 전처리...")
def prepare_dataset(data):
    texts = []
    for sample in data:
        text = tokenizer.apply_chat_template(
            sample['messages'],
            tokenize=False,
            add_generation_prompt=False
        )
        texts.append(text)
    return Dataset.from_dict({"text": texts})

train_dataset = prepare_dataset(train_data)
val_dataset = prepare_dataset(val_data)

def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        padding="max_length",
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

print("✓ 토크나이징...")
train_dataset = train_dataset.map(tokenize_function, batched=True, remove_columns=["text"])
val_dataset = val_dataset.map(tokenize_function, batched=True, remove_columns=["text"])

print("\n[5단계] 학습 설정...")
training_args = TrainingArguments(
    output_dir="./qwen_iot_feature_varied_30K",
    num_train_epochs=5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    weight_decay=0.01,
    logging_steps=100,
    eval_strategy="steps",
    eval_steps=500,
    save_strategy="steps",
    save_steps=500,
    save_total_limit=3,
    fp16=False,
    bf16=True,
    warmup_steps=100,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    report_to="none"
)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator
)

print("\n[6단계] 학습 시작...")
print("=" * 100)
trainer.train()

print("\n✓ 학습 완료!")
trainer.save_model()
tokenizer.save_pretrained(training_args.output_dir)
print("=" * 100)
EOFPYTHON

                nohup python train_feature_varied_30K.py > train_feature_varied_30K.log 2>&1 &
                TRAIN_PID=$!
                
                echo "  학습 프로세스 시작: PID $TRAIN_PID"
                echo "  로그: train_feature_varied_30K.log"
                echo "  모델 출력: qwen_iot_feature_varied_30K"
                echo ""
                echo "✓ 자동 학습 시작 완료!"
                
                break
            else
                echo "⚠ Train/Val 파일 생성 실패, 재시도..."
                sleep 30
            fi
        fi
    else
        echo "[$CURRENT_TIME] 파일 대기 중..."
    fi
    
    sleep $CHECK_INTERVAL
done

echo ""
echo "=========================================="
echo "감시 및 자동 학습 완료"
echo "=========================================="
