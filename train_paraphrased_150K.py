#!/usr/bin/env python3
"""
Qwen 모델 파인튜닝 - Paraphrasing 150K
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
print("Qwen2.5-1.5B 파인튜닝 - Paraphrasing 150K")
print("=" * 100)

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

print("\n[1단계] JSONL 데이터 로드...")
train_data = load_jsonl('train_paraphrased_150K.jsonl')
val_data = load_jsonl('val_paraphrased_150K.jsonl')
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
    output_dir="./qwen_iot_paraphrased_150K",
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
