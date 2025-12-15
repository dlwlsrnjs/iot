#!/usr/bin/env python3
"""
Qwen2.5-1.5B 모델 파인튜닝 - IoT 공격 분류
LoRA 방식 사용
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
import os

print("=" * 100)
print("Qwen2.5-1.5B 파인튜닝 - IoT 공격 분류")
print("=" * 100)

# 1. 데이터 로드
print("\n[1단계] 학습 데이터 로드...")

with open('llm_training_dataset.json', 'r', encoding='utf-8') as f:
    train_data = json.load(f)

with open('llm_validation_dataset.json', 'r', encoding='utf-8') as f:
    val_data = json.load(f)

print(f"✓ 학습 데이터: {len(train_data)}개")
print(f"✓ 검증 데이터: {len(val_data)}개")

# 2. 모델 및 토크나이저 로드
print("\n[2단계] Qwen2.5-1.5B 모델 로드...")

model_name = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map={"": 0},  # 명시적으로 GPU 0번만 사용
    trust_remote_code=True
)

print(f"✓ 모델 로드 완료 (디바이스: {model.device})")

# 3. LoRA 설정
print("\n[3단계] LoRA 설정...")

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,  # LoRA rank
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    bias="none"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# 4. 데이터 전처리
print("\n[4단계] 데이터 전처리...")

# Dataset 생성
print("✓ Dataset 객체 생성...")
train_dataset = Dataset.from_list(train_data)
val_dataset = Dataset.from_list(val_data)

def format_prompt(sample):
    """프롬프트 형식화 - 간단한 방식"""
    text = f"<|im_start|>user\n{sample['input']}<|im_end|>\n<|im_start|>assistant\n{sample['output']}<|im_end|>"
    return {"text": text}

print("✓ 프롬프트 형식화...")
train_dataset = train_dataset.map(format_prompt, num_proc=1)
val_dataset = val_dataset.map(format_prompt, num_proc=1)

print(f"✓ 학습 데이터셋 준비 완료")

# 토크나이즈
def tokenize_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=256,  # 512 -> 256 (메모리 절약)
        padding="max_length"
    )

print("✓ 토크나이징...")
train_dataset = train_dataset.map(tokenize_function, batched=True, remove_columns=train_dataset.column_names)
val_dataset = val_dataset.map(tokenize_function, batched=True, remove_columns=val_dataset.column_names)

# 5. 학습 설정
print("\n[5단계] 학습 설정...")

training_args = TrainingArguments(
    output_dir="./qwen_iot_attack_classifier",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    weight_decay=0.01,
    warmup_steps=50,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_steps=100,
    save_total_limit=2,
    fp16=False,
    bf16=True,
    push_to_hub=False,
    report_to="none",
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    remove_unused_columns=False,  # 추가: 컬럼 제거 방지
)

print(f"✓ 학습 설정 완료")
print(f"  - Batch size: {2} x {8} = {16} (effective)")
print(f"  - Learning rate: {2e-4}")
print(f"  - Epochs: {3}")

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator,
)

# 6. 학습 시작
print("\n[6단계] 학습 시작...")
print("=" * 100)

trainer.train()

print("\n" + "=" * 100)
print("학습 완료!")
print("=" * 100)

# 7. 모델 저장
print("\n[7단계] 모델 저장...")

model.save_pretrained("./qwen_iot_attack_classifier_final")
tokenizer.save_pretrained("./qwen_iot_attack_classifier_final")

print("✓ 모델 저장 완료: ./qwen_iot_attack_classifier_final")

print("\n" + "=" * 100)
print("파인튜닝 완료!")
print("=" * 100)
print(f"학습된 모델 경로: ./qwen_iot_attack_classifier_final")
print("이제 이 모델로 공격 분류를 수행할 수 있습니다.")
