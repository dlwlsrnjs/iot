"""
공격 유형별 데이터 특성 분석
각 공격 유형과 정상 트래픽의 통계적 특성을 분석하여 RAG 문서 생성
"""

import pandas as pd
import numpy as np
from collections import defaultdict
import json

# 라벨 매핑
LABEL_MAP = {
    0: "Normal",
    1: "Arp_Spoofing",
    2: "BotNet_DDOS",
    3: "HTTP_Flood",
    4: "ICMP_Flood",
    5: "MQTT_Flood",
    6: "Port_Scanning",
    7: "TCP_Flood",
    8: "UDP_Flood"
}

def analyze_class_characteristics(df, label_col='traffic'):
    """각 클래스별 통계적 특성 분석"""
    characteristics = {}
    
    # 숫자형 특징만 선택
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if label_col in numeric_cols:
        numeric_cols.remove(label_col)
    
    for label_num, label_name in LABEL_MAP.items():
        if label_num not in df[label_col].values:
            continue
            
        class_data = df[df[label_col] == label_num][numeric_cols]
        
        if len(class_data) == 0:
            continue
        
        stats = {
            'count': len(class_data),
            'features': {}
        }
        
        # 각 특징별 통계
        for col in numeric_cols:
            if col in class_data.columns:
                col_data = class_data[col].dropna()
                if len(col_data) > 0:
                    stats['features'][col] = {
                        'mean': float(col_data.mean()),
                        'median': float(col_data.median()),
                        'std': float(col_data.std()),
                        'min': float(col_data.min()),
                        'max': float(col_data.max()),
                        'q25': float(col_data.quantile(0.25)),
                        'q75': float(col_data.quantile(0.75))
                    }
        
        characteristics[label_name] = stats
    
    return characteristics

def create_rag_documentation(stats):
    """통계를 RAG 문서로 변환"""
    documents = []
    
    for label_name, data in stats.items():
        count = data['count']
        features = data['features']
        
        # 주요 특징 선택 (변동성이 큰 특징들)
        important_features = []
        for feat_name, feat_stats in features.items():
            if feat_stats['std'] > 0:
                cv = feat_stats['std'] / abs(feat_stats['mean']) if feat_stats['mean'] != 0 else feat_stats['std']
                important_features.append((feat_name, feat_stats, cv))
        
        # 변동 계수로 정렬
        important_features.sort(key=lambda x: x[2], reverse=True)
        important_features = important_features[:15]  # 상위 15개
        
        # 문서 생성
        doc_parts = [f"# {label_name} Network Traffic Characteristics\n"]
        doc_parts.append(f"## Overview\n")
        doc_parts.append(f"This document describes the statistical characteristics of {label_name} network traffic based on analysis of {count:,} flow samples.\n")
        
        if label_name == "Normal":
            doc_parts.append(f"## Traffic Type\n")
            doc_parts.append(f"Normal network traffic represents legitimate, non-malicious network communication patterns.\n")
        else:
            doc_parts.append(f"## Attack Type\n")
            doc_parts.append(f"{label_name} is a network attack that exhibits specific behavioral patterns.\n")
        
        doc_parts.append(f"## Key Statistical Characteristics\n")
        doc_parts.append(f"The following features show distinctive patterns for {label_name} traffic:\n\n")
        
        for feat_name, feat_stats, cv in important_features:
            # 특징 이름을 읽기 쉽게 변환
            readable_name = feat_name.replace('_', ' ').title()
            
            doc_parts.append(f"### {readable_name} ({feat_name})\n")
            doc_parts.append(f"- **Mean Value**: {feat_stats['mean']:.4f}\n")
            doc_parts.append(f"- **Median Value**: {feat_stats['median']:.4f}\n")
            doc_parts.append(f"- **Standard Deviation**: {feat_stats['std']:.4f}\n")
            doc_parts.append(f"- **Range**: {feat_stats['min']:.4f} to {feat_stats['max']:.4f}\n")
            doc_parts.append(f"- **Interquartile Range (IQR)**: {feat_stats['q25']:.4f} to {feat_stats['q75']:.4f}\n")
            
            # 패턴 설명 추가
            if 'packet' in feat_name.lower() or 'pkt' in feat_name.lower():
                if feat_stats['mean'] > 100:
                    doc_parts.append(f"- **Pattern**: High packet count indicates frequent communication\n")
                elif feat_stats['mean'] < 10:
                    doc_parts.append(f"- **Pattern**: Low packet count indicates minimal communication\n")
            
            if 'byte' in feat_name.lower():
                if feat_stats['mean'] > 10000:
                    doc_parts.append(f"- **Pattern**: Large data transfer volume\n")
                elif feat_stats['mean'] < 100:
                    doc_parts.append(f"- **Pattern**: Small data transfer volume\n")
            
            if 'rate' in feat_name.lower() or 'per_sec' in feat_name.lower():
                if feat_stats['mean'] > 100:
                    doc_parts.append(f"- **Pattern**: High rate indicates rapid communication\n")
                elif feat_stats['mean'] < 1:
                    doc_parts.append(f"- **Pattern**: Low rate indicates slow communication\n")
            
            if 'iat' in feat_name.lower() or 'inter' in feat_name.lower():
                if feat_stats['mean'] < 0.01:
                    doc_parts.append(f"- **Pattern**: Very short inter-arrival time indicates burst traffic\n")
                elif feat_stats['mean'] > 1.0:
                    doc_parts.append(f"- **Pattern**: Long inter-arrival time indicates sparse communication\n")
            
            if 'ratio' in feat_name.lower():
                if feat_stats['mean'] > 10:
                    doc_parts.append(f"- **Pattern**: Highly asymmetric traffic (mostly download)\n")
                elif feat_stats['mean'] < 0.1:
                    doc_parts.append(f"- **Pattern**: Highly asymmetric traffic (mostly upload)\n")
                else:
                    doc_parts.append(f"- **Pattern**: Relatively balanced bidirectional traffic\n")
            
            doc_parts.append("\n")
        
        # 비교 정보 추가
        doc_parts.append(f"## Distinguishing Features\n")
        doc_parts.append(f"When identifying {label_name} traffic, look for:\n")
        
        # 가장 특징적인 값들
        top_features = important_features[:5]
        for feat_name, feat_stats, cv in top_features:
            readable_name = feat_name.replace('_', ' ').title()
            doc_parts.append(f"- {readable_name}: typically around {feat_stats['mean']:.2f} (range: {feat_stats['min']:.2f} - {feat_stats['max']:.2f})\n")
        
        documents.append({
            'label': label_name,
            'content': '\n'.join(doc_parts),
            'metadata': {
                'type': 'attack_pattern' if label_name != 'Normal' else 'normal_pattern',
                'sample_count': count,
                'feature_count': len(important_features)
            }
        })
    
    return documents

def main():
    print("="*60)
    print("공격 유형별 데이터 특성 분석")
    print("="*60)
    
    # 데이터 로드
    print("\n[1] 데이터 로드 중...")
    train_path = "Datasets/Farm-Flow_Train_Multiclass.csv"
    
    try:
        # 전체 데이터 로드 (메모리 고려하여 샘플링 가능)
        print("   전체 데이터 로드 중... (시간이 걸릴 수 있습니다)")
        df = pd.read_csv(train_path)
        print(f"   ✅ 로드 완료: {len(df):,}개 샘플")
    except Exception as e:
        print(f"   ❌ 오류: {e}")
        return
    
    # 클래스별 통계 분석
    print("\n[2] 클래스별 통계 분석 중...")
    stats = analyze_class_characteristics(df)
    
    print(f"\n   분석된 클래스:")
    for label_name, data in stats.items():
        print(f"   - {label_name}: {data['count']:,}개 샘플")
    
    # RAG 문서 생성
    print("\n[3] RAG 문서 생성 중...")
    documents = create_rag_documentation(stats)
    
    print(f"   ✅ {len(documents)}개 문서 생성 완료")
    
    # 문서 저장
    print("\n[4] 문서 저장 중...")
    output_dir = "rag_documentation"
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    for doc in documents:
        filename = f"{output_dir}/{doc['label']}_characteristics.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(doc['content'])
        print(f"   ✅ 저장: {filename}")
    
    # JSON으로도 저장 (메타데이터 포함)
    json_file = f"{output_dir}/attack_patterns.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(documents, f, indent=2, ensure_ascii=False)
    print(f"   ✅ 저장: {json_file}")
    
    print("\n" + "="*60)
    print("분석 완료!")
    print("="*60)
    print(f"\n생성된 문서: {len(documents)}개")
    print(f"저장 위치: {output_dir}/")
    print("\n다음 단계:")
    print("1. RAG 데이터베이스에 문서 추가")
    print("2. LLM 테스트 실행")

if __name__ == "__main__":
    main()

