"""
중복 제거 및 올바른 데이터 분할
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
from flaml import AutoML
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("중복 제거 및 올바른 AutoML 학습")
print("=" * 80)

# =========================
# 이진 분류
# =========================
print("\n[1] 이진 분류 데이터 처리")

# 데이터 로드
df_train = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Train_Binary.csv')
df_test = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Test_Binary.csv')

# 전체 데이터 합치기
df_all = pd.concat([df_train, df_test], ignore_index=True)
print(f"전체 데이터: {df_all.shape}")

# 중복 제거 (특징만 사용)
feature_cols = [col for col in df_all.columns if col not in ['is_attack', 'traffic']]
df_unique = df_all.drop_duplicates(subset=feature_cols, keep='first')
print(f"중복 제거 후: {df_unique.shape} ({len(df_unique)/len(df_all)*100:.1f}%)")

# 특징과 라벨 분리
X = df_unique[feature_cols].select_dtypes(include=[np.number])
y = df_unique['is_attack']

print(f"특징 수: {X.shape[1]}")
print(f"라벨 분포:\n{y.value_counts()}")

# 새로운 train/test 분할 (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n새로운 분할:")
print(f"훈련: {X_train.shape[0]}, 테스트: {X_test.shape[0]}")
print(f"훈련 라벨: {y_train.value_counts().to_dict()}")
print(f"테스트 라벨: {y_test.value_counts().to_dict()}")

# 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# AutoML 학습
print(f"\n[2] FLAML AutoML 학습 (5분) - GPU 활용 (XGBoost)")

# XGBoost만 GPU 사용, LightGBM은 CPU
from flaml.automl.model import LGBMEstimator, XGBoostSklearnEstimator

automl = AutoML()

settings = {
    "time_budget": 300,  # 5분
    "metric": "roc_auc",
    "task": "classification",
    "seed": 42,
    "verbose": 1,
    "eval_method": "cv",
    "n_splits": 5,
    "estimator_list": ["lgbm", "xgboost"],
    "custom_hp": {
        "xgboost": {
            "tree_method": {"domain": "hist"},
            "device": {"domain": "cuda:0"},
        },
    }
}

automl.fit(X_train_scaled, y_train, **settings)

print(f"\n최적 모델: {automl.best_estimator}")
print(f"CV 검증 성능: {1 - automl.best_loss:.4f}")
print(f"최적 하이퍼파라미터:\n{automl.best_config}")

# 테스트 세트 평가
print(f"\n[3] 독립 테스트 세트 평가")
y_pred = automl.predict(X_test_scaled)
y_pred_proba = automl.predict_proba(X_test_scaled)[:, 1]

acc = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"\n정확도: {acc:.4f}")
print(f"ROC-AUC: {auc:.4f}")
print(f"\n분류 보고서:")
print(classification_report(y_test, y_pred, target_names=['정상', '공격']))

# =========================
# 다중 분류
# =========================
print("\n" + "=" * 80)
print("[4] 다중 분류 데이터 처리")
print("=" * 80)

df_train_multi = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Train_Multiclass.csv')
df_test_multi = pd.read_csv('/home/work/skku/iot/Datasets/Farm-Flow_Test_Multiclass.csv')

# 전체 데이터 합치기
df_all_multi = pd.concat([df_train_multi, df_test_multi], ignore_index=True)
print(f"전체 데이터: {df_all_multi.shape}")

# 중복 제거
feature_cols_multi = [col for col in df_all_multi.columns if col not in ['is_attack', 'traffic']]
df_unique_multi = df_all_multi.drop_duplicates(subset=feature_cols_multi, keep='first')
print(f"중복 제거 후: {df_unique_multi.shape} ({len(df_unique_multi)/len(df_all_multi)*100:.1f}%)")

# 특징과 라벨 분리
X_multi = df_unique_multi[feature_cols_multi].select_dtypes(include=[np.number])
y_multi = df_unique_multi['traffic']

print(f"\n라벨 분포:\n{y_multi.value_counts()}")

# 새로운 train/test 분할
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42, stratify=y_multi
)

print(f"\n새로운 분할:")
print(f"훈련: {X_train_m.shape[0]}, 테스트: {X_test_m.shape[0]}")

# 정규화
scaler_m = StandardScaler()
X_train_m_scaled = scaler_m.fit_transform(X_train_m)
X_test_m_scaled = scaler_m.transform(X_test_m)

# AutoML 학습
print(f"\n[5] FLAML AutoML 학습 (5분) - GPU 활용 (XGBoost)")
automl_multi = AutoML()

settings_multi = {
    "time_budget": 300,  # 5분
    "metric": "log_loss",
    "task": "classification",
    "seed": 42,
    "verbose": 1,
    "eval_method": "cv",
    "n_splits": 5,
    "estimator_list": ["lgbm", "xgboost"],
    "custom_hp": {
        "xgboost": {
            "tree_method": {"domain": "hist"},
            "device": {"domain": "cuda:0"},
        },
    }
}

automl_multi.fit(X_train_m_scaled, y_train_m, **settings_multi)

print(f"\n최적 모델: {automl_multi.best_estimator}")
print(f"CV 검증 성능: {automl_multi.best_loss:.4f}")

# 테스트 세트 평가
print(f"\n[6] 독립 테스트 세트 평가")
y_pred_m = automl_multi.predict(X_test_m_scaled)

acc_m = accuracy_score(y_test_m, y_pred_m)
print(f"\n정확도: {acc_m:.4f}")
print(f"\n분류 보고서:")
print(classification_report(y_test_m, y_pred_m))

print("\n" + "=" * 80)
print("완료!")
print("=" * 80)
print("\n💡 결과 해석:")
print("- 이전 결과(ROC-AUC=1.0000)는 데이터 중복(89%)으로 인한 과적합이었습니다.")
print("- 중복 제거 후 현재 결과가 실제 모델 성능입니다.")
print("- 논문에서 보고된 성능과 비교해보세요!")
