"""
데이터 누수 및 과적합 가능성 확인 스크립트
"""
import pandas as pd
import numpy as np

print("=" * 80)
print("데이터 누수 및 특징 분석")
print("=" * 80)

# 이진 분류 데이터 로드
print("\n[1] 이진 분류 데이터 분석")
df_train_bin = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Train_Binary.csv')
df_test_bin = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Test_Binary.csv')

print(f"훈련 데이터: {df_train_bin.shape}")
print(f"테스트 데이터: {df_test_bin.shape}")
print(f"\n컬럼 목록:\n{df_train_bin.columns.tolist()}")

# 라벨 분포 확인
print(f"\n훈련 라벨 분포:")
print(df_train_bin['is_attack'].value_counts(normalize=True))
print(f"\n테스트 라벨 분포:")
print(df_test_bin['is_attack'].value_counts(normalize=True))

# 특징 통계 확인
print(f"\n[2] 특징 통계 분석")
numeric_cols = df_train_bin.select_dtypes(include=[np.number]).columns
numeric_cols = [col for col in numeric_cols if col != 'is_attack']

print(f"\n숫자형 특징 수: {len(numeric_cols)}")
print(f"특징 목록: {numeric_cols[:10]}...")

# 클래스별 평균 차이 확인
print(f"\n[3] 클래스 간 특징 차이 분석 (상위 10개)")
class_diff = {}
for col in numeric_cols:
    normal_mean = df_train_bin[df_train_bin['is_attack'] == 0][col].mean()
    attack_mean = df_train_bin[df_train_bin['is_attack'] == 1][col].mean()
    diff = abs(normal_mean - attack_mean)
    class_diff[col] = diff

sorted_diff = sorted(class_diff.items(), key=lambda x: x[1], reverse=True)
for col, diff in sorted_diff[:10]:
    normal_val = df_train_bin[df_train_bin['is_attack'] == 0][col].mean()
    attack_val = df_train_bin[df_train_bin['is_attack'] == 1][col].mean()
    print(f"{col:30s} | 정상: {normal_val:12.2f} | 공격: {attack_val:12.2f} | 차이: {diff:12.2f}")

# 중복 샘플 확인
print(f"\n[4] 데이터 중복 확인")
train_duplicates = df_train_bin.duplicated().sum()
test_duplicates = df_test_bin.duplicated().sum()
print(f"훈련 중복: {train_duplicates} ({train_duplicates/len(df_train_bin)*100:.2f}%)")
print(f"테스트 중복: {test_duplicates} ({test_duplicates/len(df_test_bin)*100:.2f}%)")

# 훈련-테스트 겹침 확인
print(f"\n[5] 훈련-테스트 데이터 겹침 확인")
train_set = set(df_train_bin.drop(columns=['is_attack']).apply(tuple, axis=1))
test_set = set(df_test_bin.drop(columns=['is_attack']).apply(tuple, axis=1))
overlap = len(train_set.intersection(test_set))
print(f"겹치는 샘플 수: {overlap} ({overlap/len(df_test_bin)*100:.2f}%)")

# 다중 분류 데이터 분석
print(f"\n" + "=" * 80)
print("[6] 다중 분류 데이터 분석")
print("=" * 80)
df_train_multi = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Train_Multiclass.csv')
df_test_multi = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Test_Multiclass.csv')

print(f"\n훈련 라벨 분포:")
print(df_train_multi['traffic'].value_counts())
print(f"\n테스트 라벨 분포:")
print(df_test_multi['traffic'].value_counts())

# 클래스 불균형 확인
print(f"\n[7] 클래스 불균형 비율")
class_counts = df_train_multi['traffic'].value_counts()
max_count = class_counts.max()
min_count = class_counts.min()
imbalance_ratio = max_count / min_count
print(f"최대 클래스: {class_counts.idxmax()} ({max_count:,})")
print(f"최소 클래스: {class_counts.idxmin()} ({min_count:,})")
print(f"불균형 비율: {imbalance_ratio:.2f}:1")

print("\n" + "=" * 80)
print("분석 완료")
print("=" * 80)
