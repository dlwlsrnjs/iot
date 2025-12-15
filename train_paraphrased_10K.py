#!/usr/bin/env python3
"""
JSONL 데이터로 Qwen 모델 파인튜닝 - Paraphrasing 10K 버전
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
print("Qwen2.5-1.5B 파인튜닝 - Paraphrasing 10K")
print("=" * 100)

# 1. JSONL 데이터 로드
print("\n[1단계] JSONL 데이터 로드...")

def load_jsonl(file_path):
    """JSONL 파일 로드"""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

train_data = load_jsonl('train_paraphrased_10K.jsonl')
val_data = load_jsonl('val_paraphrased_10K.jsonl')

print(f"✓ 학습 데이터: {len(train_data):,}개")
print(f"✓ 검증 데이터: {len(val_data):,}개")

# 2. 모델 및 토크나이저 로드
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

print(f"✓ 모델 로드 완료: {model_name}")

# 3. LoRA 설정
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

# 4. 데이터 전처리
print("\n[4단계] 데이터 전처리...")

def prepare_dataset(data):
    """Chat template 적용"""
    texts = []
    for sample in data:
        messages = sample['messages']
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False
        )
        texts.append(text)
    
    return Dataset.from_dict({"text": texts})

print("✓ Dataset 객체 생성...")
train_dataset = prepare_dataset(train_data)
val_dataset = prepare_dataset(val_data)

print("✓ Chat template 적용...")
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

print("✓ 전처리 완료")

# 5. 학습 설정
print("\n[5단계] 학습 설정...")

training_args = TrainingArguments(
    output_dir="./qwen_iot_paraphrased_10K",
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

print("✓ 학습 설정 완료")
print(f"  - Batch size: {training_args.per_device_train_batch_size} x {training_args.gradient_accumulation_steps} = {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps} (effective)")
print(f"  - Learning rate: {training_args.learning_rate}")
print(f"  - Epochs: {training_args.num_train_epochs}")
print(f"  - Total steps: ~{len(train_dataset) // (training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps) * training_args.num_train_epochs:,}")

# 6. Trainer 생성
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator
)

# 7. 학습 시작
print("\n[6단계] 학습 시작...")
print("=" * 100)

trainer.train()

print("\n✓ 학습 완료!")
print(f"✓ 모델 저장: {training_args.output_dir}")

# 8. 최종 저장
trainer.save_model()
tokenizer.save_pretrained(training_args.output_dir)

print("\n" + "=" * 100)
print("파인튜닝 완료 - Paraphrasing 10K")
print("=" * 100)
