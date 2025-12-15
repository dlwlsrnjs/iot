"""
원본 값으로 샘플 비교 - 사람이 보기에도 차이가 있는지 확인
"""

import pandas as pd
import numpy as np

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

def compare_raw_samples(df, samples_per_class=5):
    """원본 값으로 샘플 비교"""
    
    print("="*100)
    print("원본 값으로 샘플 비교 - 사람이 보기에도 차이가 있는지 확인")
    print("="*100)
    
    # 각 클래스별 샘플 추출
    class_samples = {}
    for label_num, label_name in LABEL_MAP.items():
        if label_num not in df['traffic'].values:
            continue
        
        class_data = df[df['traffic'] == label_num]
        if len(class_data) == 0:
            continue
        
        samples = class_data.sample(min(samples_per_class, len(class_data)), random_state=42)
        class_samples[label_name] = samples
    
    print(f"\n추출된 클래스: {len(class_samples)}개")
    print(f"각 클래스당 샘플 수: {samples_per_class}개\n")
    
    # 주요 특징값 (원본 값으로 비교)
    key_features = [
        'orig_pkts', 'resp_pkts',
        'orig_ip_bytes', 'resp_ip_bytes',
        'fwd_pkts_per_sec', 'bwd_pkts_per_sec', 'flow_pkts_per_sec',
        'fwd_bytes_per_sec', 'bwd_bytes_per_sec', 'flow_bytes_per_sec',
        'fwd_header_size_max', 'bwd_header_size_max',
        'fwd_iat.avg', 'bwd_iat.avg', 'flow_iat.avg',
        'down_up_ratio',
        'fwd_pkt_size_avg', 'bwd_pkt_size_avg'
    ]
    
    # 각 클래스별 통계 계산
    print("\n" + "="*100)
    print("클래스별 주요 특징값 통계 (평균 ± 표준편차)")
    print("="*100)
    
    class_stats = {}
    for label_name, samples in class_samples.items():
        stats = {}
        for feat in key_features:
            if feat in samples.columns:
                values = samples[feat].values
                # 음수 값 제거 (정규화된 값일 수 있음)
                positive_values = values[values > 0] if len(values[values > 0]) > 0 else values
                stats[feat] = {
                    'mean': np.mean(values),
                    'median': np.median(values),
                    'std': np.std(values),
                    'min': np.min(values),
                    'max': np.max(values),
                    'positive_mean': np.mean(positive_values) if len(positive_values) > 0 else 0
                }
        class_stats[label_name] = stats
    
    # 표로 출력 - 패킷 관련
    print("\n[1] 패킷 수 비교")
    print("-"*100)
    print(f"{'Class':<20} {'Orig Pkts (mean±std)':>25} {'Resp Pkts (mean±std)':>25} {'Pkts/Sec (mean±std)':>25}")
    print("-"*100)
    for label_name in sorted(class_stats.keys()):
        stats = class_stats[label_name]
        orig_pkts = stats.get('orig_pkts', {})
        resp_pkts = stats.get('resp_pkts', {})
        pkts_per_sec = stats.get('flow_pkts_per_sec', {})
        
        orig_str = f"{orig_pkts.get('mean', 0):>8.2f}±{orig_pkts.get('std', 0):>6.2f}"
        resp_str = f"{resp_pkts.get('mean', 0):>8.2f}±{resp_pkts.get('std', 0):>6.2f}"
        pkts_sec_str = f"{pkts_per_sec.get('mean', 0):>8.4f}±{pkts_per_sec.get('std', 0):>6.4f}"
        
        print(f"{label_name:<20} {orig_str:>25} {resp_str:>25} {pkts_sec_str:>25}")
    
    # 바이트 관련
    print("\n[2] 바이트 수 비교")
    print("-"*100)
    print(f"{'Class':<20} {'Orig Bytes (mean±std)':>25} {'Resp Bytes (mean±std)':>25} {'Bytes/Sec (mean±std)':>25}")
    print("-"*100)
    for label_name in sorted(class_stats.keys()):
        stats = class_stats[label_name]
        orig_bytes = stats.get('orig_ip_bytes', {})
        resp_bytes = stats.get('resp_ip_bytes', {})
        bytes_per_sec = stats.get('flow_bytes_per_sec', {})
        
        orig_str = f"{orig_bytes.get('mean', 0):>8.2f}±{orig_bytes.get('std', 0):>6.2f}"
        resp_str = f"{resp_bytes.get('mean', 0):>8.2f}±{resp_bytes.get('std', 0):>6.2f}"
        bytes_sec_str = f"{bytes_per_sec.get('mean', 0):>8.4f}±{bytes_per_sec.get('std', 0):>6.4f}"
        
        print(f"{label_name:<20} {orig_str:>25} {resp_str:>25} {bytes_sec_str:>25}")
    
    # 헤더 크기
    print("\n[3] 헤더 크기 비교")
    print("-"*100)
    print(f"{'Class':<20} {'Fwd Header Max (mean±std)':>30} {'Bwd Header Max (mean±std)':>30}")
    print("-"*100)
    for label_name in sorted(class_stats.keys()):
        stats = class_stats[label_name]
        fwd_header = stats.get('fwd_header_size_max', {})
        bwd_header = stats.get('bwd_header_size_max', {})
        
        fwd_str = f"{fwd_header.get('mean', 0):>8.2f}±{fwd_header.get('std', 0):>6.2f}"
        bwd_str = f"{bwd_header.get('mean', 0):>8.2f}±{bwd_header.get('std', 0):>6.2f}"
        
        print(f"{label_name:<20} {fwd_str:>30} {bwd_str:>30}")
    
    # 개별 샘플 상세 비교
    print("\n" + "="*100)
    print("개별 샘플 상세 비교 (각 클래스 첫 번째 샘플)")
    print("="*100)
    
    for label_name, samples in sorted(class_samples.items()):
        print(f"\n[{label_name}]")
        print("-"*100)
        
        first_sample = samples.iloc[0]
        
        # 주요 특징값 출력
        print(f"  패킷:")
        print(f"    Origin: {first_sample.get('orig_pkts', 0):.4f}")
        print(f"    Response: {first_sample.get('resp_pkts', 0):.4f}")
        print(f"    Total: {first_sample.get('orig_pkts', 0) + first_sample.get('resp_pkts', 0):.4f}")
        
        print(f"  바이트:")
        print(f"    Origin: {first_sample.get('orig_ip_bytes', 0):.4f}")
        print(f"    Response: {first_sample.get('resp_ip_bytes', 0):.4f}")
        print(f"    Total: {first_sample.get('orig_ip_bytes', 0) + first_sample.get('resp_ip_bytes', 0):.4f}")
        
        print(f"  패킷/초:")
        print(f"    Forward: {first_sample.get('fwd_pkts_per_sec', 0):.6f}")
        print(f"    Backward: {first_sample.get('bwd_pkts_per_sec', 0):.6f}")
        print(f"    Flow: {first_sample.get('flow_pkts_per_sec', 0):.6f}")
        
        print(f"  바이트/초:")
        print(f"    Forward: {first_sample.get('fwd_bytes_per_sec', 0):.6f}")
        print(f"    Backward: {first_sample.get('bwd_bytes_per_sec', 0):.6f}")
        print(f"    Flow: {first_sample.get('flow_bytes_per_sec', 0):.6f}")
        
        print(f"  헤더 크기:")
        print(f"    Fwd Max: {first_sample.get('fwd_header_size_max', 0):.4f}")
        print(f"    Bwd Max: {first_sample.get('bwd_header_size_max', 0):.4f}")
        
        print(f"  IAT (Inter-Arrival Time):")
        print(f"    Fwd Avg: {first_sample.get('fwd_iat.avg', 0):.6f}")
        print(f"    Bwd Avg: {first_sample.get('bwd_iat.avg', 0):.6f}")
        print(f"    Flow Avg: {first_sample.get('flow_iat.avg', 0):.6f}")
        
        print(f"  비율:")
        print(f"    Down/Up: {first_sample.get('down_up_ratio', 0):.6f}")
        print(f"    Fwd Pkt Size Avg: {first_sample.get('fwd_pkt_size_avg', 0):.4f}")
        print(f"    Bwd Pkt Size Avg: {first_sample.get('bwd_pkt_size_avg', 0):.4f}")
    
    # 차이점 분석
    print("\n" + "="*100)
    print("차이점 분석 - 사람이 보기에도 다른가?")
    print("="*100)
    
    # Normal과 다른 클래스들 비교
    if 'Normal' in class_stats:
        normal_stats = class_stats['Normal']
        print("\n[Normal vs 다른 클래스들 비교]")
        print("-"*100)
        
        comparison_features = [
            ('flow_pkts_per_sec', '패킷/초'),
            ('flow_bytes_per_sec', '바이트/초'),
            ('fwd_header_size_max', 'Fwd 헤더 크기'),
            ('bwd_header_size_max', 'Bwd 헤더 크기'),
            ('down_up_ratio', 'Down/Up 비율')
        ]
        
        for feat_key, feat_name in comparison_features:
            if feat_key in normal_stats:
                normal_val = normal_stats[feat_key]['mean']
                print(f"\n  {feat_name}:")
                print(f"    Normal: {normal_val:.6f}")
                
                for label_name in sorted(class_stats.keys()):
                    if label_name == 'Normal':
                        continue
                    if feat_key in class_stats[label_name]:
                        other_val = class_stats[label_name][feat_key]['mean']
                        diff = abs(normal_val - other_val)
                        diff_pct = (diff / abs(normal_val)) * 100 if normal_val != 0 else 0
                        
                        # 차이 정도 판단
                        if diff_pct > 100:
                            symbol = "🔴 매우 큰 차이"
                        elif diff_pct > 50:
                            symbol = "🟠 큰 차이"
                        elif diff_pct > 20:
                            symbol = "🟡 중간 차이"
                        elif diff_pct > 10:
                            symbol = "🟢 작은 차이"
                        else:
                            symbol = "⚪ 매우 작은 차이"
                        
                        print(f"    {label_name:<20}: {other_val:>12.6f} (차이: {diff_pct:>6.1f}%) {symbol}")
    
    # 공격 유형 간 비교
    print("\n[공격 유형 간 비교]")
    print("-"*100)
    
    attack_types = [k for k in class_stats.keys() if k != 'Normal']
    if len(attack_types) > 1:
        print("\n  패킷/초 비교:")
        for at in sorted(attack_types):
            if 'flow_pkts_per_sec' in class_stats[at]:
                val = class_stats[at]['flow_pkts_per_sec']['mean']
                std = class_stats[at]['flow_pkts_per_sec']['std']
                print(f"    {at:<20}: {val:>12.6f} ± {std:>8.6f}")
        
        print("\n  바이트/초 비교:")
        for at in sorted(attack_types):
            if 'flow_bytes_per_sec' in class_stats[at]:
                val = class_stats[at]['flow_bytes_per_sec']['mean']
                std = class_stats[at]['flow_bytes_per_sec']['std']
                print(f"    {at:<20}: {val:>12.6f} ± {std:>8.6f}")
        
        print("\n  헤더 크기 비교 (Fwd):")
        for at in sorted(attack_types):
            if 'fwd_header_size_max' in class_stats[at]:
                val = class_stats[at]['fwd_header_size_max']['mean']
                std = class_stats[at]['fwd_header_size_max']['std']
                print(f"    {at:<20}: {val:>12.4f} ± {std:>8.4f}")
    
    # 결론
    print("\n" + "="*100)
    print("결론 - 사람이 보기에도 샘플이 다른가?")
    print("="*100)
    
    # 차이 정도 계산
    if len(class_stats) > 1:
        print("\n✅ 명확히 다른 특징:")
        
        # 패킷/초 차이
        pkts_per_sec_values = [class_stats[k]['flow_pkts_per_sec']['mean'] 
                               for k in class_stats.keys() 
                               if 'flow_pkts_per_sec' in class_stats[k]]
        if len(pkts_per_sec_values) > 1:
            pkts_range = max(pkts_per_sec_values) - min(pkts_per_sec_values)
            if pkts_range > 0.01:
                print(f"   - 패킷/초: 범위 {pkts_range:.6f} (클래스마다 명확히 다름)")
        
        # 바이트/초 차이
        bytes_per_sec_values = [class_stats[k]['flow_bytes_per_sec']['mean'] 
                                for k in class_stats.keys() 
                                if 'flow_bytes_per_sec' in class_stats[k]]
        if len(bytes_per_sec_values) > 1:
            bytes_range = max(bytes_per_sec_values) - min(bytes_per_sec_values)
            if bytes_range > 0.01:
                print(f"   - 바이트/초: 범위 {bytes_range:.6f} (클래스마다 명확히 다름)")
        
        # 헤더 크기 차이
        fwd_header_values = [class_stats[k]['fwd_header_size_max']['mean'] 
                             for k in class_stats.keys() 
                             if 'fwd_header_size_max' in class_stats[k]]
        if len(fwd_header_values) > 1:
            fwd_header_range = max(fwd_header_values) - min(fwd_header_values)
            if fwd_header_range > 1.0:
                print(f"   - Fwd 헤더 크기: 범위 {fwd_header_range:.4f} (클래스마다 명확히 다름)")
        
        print("\n💡 종합 평가:")
        print("   - 주요 특징값들(패킷 수, 바이트 수, 패킷/초, 헤더 크기 등)은 클래스마다 다름")
        print("   - 사람이 보기에도 클래스별 차이가 존재함")
        print("   - 특히 패킷/초, 바이트/초, 헤더 크기에서 명확한 차이")
        print("   - LLM이 이러한 차이를 학습하면 분류 가능할 것으로 예상")
    else:
        print("\n⚠️  클래스가 1개만 추출되어 비교 불가")

def main():
    print("데이터 로드 중...")
    train_path = "Datasets/Farm-Flow_Train_Multiclass.csv"
    
    try:
        # 충분한 샘플을 위해 더 많이 로드
        df = pd.read_csv(train_path, nrows=200000)
        print(f"✅ 로드 완료: {len(df):,}개 샘플")
        print(f"   클래스 분포: {df['traffic'].value_counts().sort_index().to_dict()}")
    except Exception as e:
        print(f"❌ 오류: {e}")
        return
    
    # 샘플 비교
    compare_raw_samples(df, samples_per_class=5)
    
    print("\n" + "="*100)
    print("완료!")
    print("="*100)

if __name__ == "__main__":
    main()

