# 데이터셋 검증 보고서

## 실제 데이터셋 컬럼 확인 결과

### ✅ 존재하는 컬럼:
- `orig_pkts`, `resp_pkts` - 패킷 수
- `orig_ip_bytes`, `resp_ip_bytes` - 바이트 수  
- `fwd_pkts_per_sec`, `flow_pkts_per_sec` - 초당 패킷 수
- `fwd_header_size_max`, `bwd_header_size_max` - 헤더 크기
- `missed_bytes`, `pkts_difference` - 기타 특징
- `traffic` - 라벨

### ❌ 존재하지 않는 컬럼:
- `duration`, `flow_duration` - 지속 시간
- `proto`, `protocol` - 프로토콜
- `conn_state`, `connection_state` - 연결 상태
- `id.orig_p`, `id.resp_p` - 포트
- `id.orig_h`, `id.resp_h` - IP 주소
- `service` - 서비스
- `orig_bytes`, `resp_bytes` (대신 `orig_ip_bytes`, `resp_ip_bytes` 사용)

## 중요 발견

**실제 데이터셋은 이미 특징 추출(feature extraction) 과정을 거친 정규화된 수치형 특징값들로 구성되어 있습니다.**

사용자가 언급한 컬럼들(`proto`, `conn_state`, `id.orig_p` 등)은 **원시 네트워크 트래픽 데이터**에 있는 컬럼들이며, 현재 데이터셋에는 이미 특징 추출 과정을 통해 변환된 수치형 특징값들만 존재합니다.

## 결론

사용자의 설명은 **원시 네트워크 트래픽 데이터**에 대한 설명이며, 현재 데이터셋의 **정규화된 특징값**과는 직접적으로 매칭되지 않습니다.

하지만 설명의 **의도와 개념**은 맞습니다:
- 정상 트래픽: 안정적인 패턴
- ARP 스푸핑: 높은 헤더 크기
- BotNet_DDOS: 낮은 패킷 속도, 음수 응답 패킷
- HTTP/ICMP/MQTT Flood: 높은 패킷/바이트 수
- Port Scanning: 낮은 바이트 수
- TCP/UDP Flood: 불완전한 연결 패턴

이러한 특성들이 **정규화된 특징값**으로 변환되어 데이터셋에 반영되어 있습니다.

