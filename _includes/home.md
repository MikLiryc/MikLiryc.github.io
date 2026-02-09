# 김재현 (Cyril)
**Unity Client Developer (4+ Years)**  
견고한 시스템 설계와 집요한 최적화로 가치 있는 플레이 경험을 만듭니다.

- Email: **jay.kim1994@gmail.com**
- GitHub: **https://github.com//MikLiryc**
- Focus: `Unity` `C#` `Architecture` `Optimization` `Tools` `LBS` `Timeline(Cinemachine)`

---

## TL;DR (한 번에 보는 강점)
- **전투 연출 파이프라인 리팩토링**: Timeline/Cinemachine 기반 연출 흐름을 구조화하여 유지보수성과 안정성을 개선
- **테스트/툴링**: Input System 기반 **맵 테스트 시뮬레이터**, **폰트 일괄 교체 툴** 등 반복 작업을 자동화
- **지도/외부 의존 대응**: MapBox Static Image API 변경 대응, Satellite 모드 비용 절감을 위한 빌드 분기 적용

---

## Links
- **원페이지 이력서(A)**: **[/resume/](/resume/)**
- **블로그(B)**: **[/blog/](/blog/)**

---

## Professional Summary
4년 차 유니티 클라이언트 개발자로 **확장성 있는 아키텍처 설계**, **개발 프로세스 효율화(툴링)**, **성능 최적화**에 강점이 있습니다.  
대형 모바일 프로젝트에서 전투·LBS·시스템 코어를 개발하며, 이슈를 “수정”으로 끝내지 않고 **재현 → 원인 분석 → 구조 개선**으로 안정화하는 방향을 선호합니다.

---

## Skills
### Languages / Engine
- C# (Advanced), HLSL (Basic)
- Unity 2022/2023, Git

### Architecture / Patterns
- FSM, Command, Observer, Memento
- 자료구조: Dictionary, Queue/Stack, SortedList, Graph(Node–Edge)

### Performance / Optimization
- Object Pooling, Mesh Combine, DrawCall Batching
- GC Alloc Reduction, UI Virtualization(EnhancedScroller)

### Tools / Pipeline
- Unity Editor Scripting (GraphView, Custom Inspector)
- Addressables, MapBox SDK, Unity Input System

---

## Experience
### (주)스노우파이프 — Unity Client Developer
- **Transformers Alliance (Mobile)**: 2022.12 – 현재
  - 클라이언트 팀원(2022.12 – 2024.11)
  - 클라이언트 파트장(2024.11 – 현재)
- **피구왕 통키 M (Live Ops)**: 2021.04 – 2022.12

---

## Portfolio — Transformers Alliance (Selected Case Studies)
> 정량 지표는 추후 확보 시 업데이트 예정 (FPS/로딩/메모리/작업시간 등)

### 1) 전투 연출 파이프라인 리팩토링 (Timeline / Cinemachine)
- 목표: Intro → Confrontation → Skill Ready/Fail/StrongSkill → HealthCheck 흐름을 **상태 기반으로 구조화**
- 포인트:
  - 연출 프리팹/PlayableDirector를 상태 단위로 관리하여 “누가 무엇을 언제 잡는지” 명확화
  - 전환 타이밍에서 한 프레임 튐 등 체감 이슈를 완화하기 위한 트랜지션 루틴 정리
  - 강스킬/HealthCheck 구간의 카메라/트랜스포머 위치 예외 케이스 수정

### 2) LBS 맵 테스트 시뮬레이터 (Unity Input System)
- 목표: GPS 의존을 낮추고 에디터에서 **재현 가능한 이동/줌/상태 테스트 환경** 구축
- 포인트:
  - 입력(Action) 기반 이동, 스크롤 줌 등 테스트 루프 단축
  - 타일 로딩/생성/파괴 진행 상태를 콜백으로 수집해 디버깅 편의 개선

### 3) MapBox Static Image API 변경 대응 + Satellite 모드 비용 절감
- 목표: 외부 API 변경으로 인한 지도 로딩 이슈 대응 + Satellite 모드에서 불필요 레이어 빌드 방지
- 포인트:
  - Static Image URL/영역 산정 로직 보정
  - Satellite 배경 사용 시 도로/물/빌딩 등의 레이어 생성 스킵 분기로 비용 감소

### 4) UI 폰트 일괄 교체 툴 (Prefab 재귀 탐색)
- 목표: 대량 프리팹 폰트 교체 작업을 자동화하고 휴먼 에러/불필요 변경을 최소화
- 포인트:
  - 프리팹 내 텍스트를 재귀 탐색하여 대상 폰트 교체
  - “변경이 없는 프리팹은 저장하지 않음”으로 변경 노이즈 감소

---

## Technical Log (Monthly)
### 2026
- 02월: 폰트 일괄 교체/에셋 최적화 툴 고도화(변경 없으면 저장하지 않음 등)
- 01월: Input System 기반 맵 테스트 시뮬레이터, Satellite 동적 로딩/타일 로직 보정

### 2025
- 12월: AR 평면 인식 정밀도 개선, 글리치 쉐이더
- 11월: 오디오 분석 기반 립싱크, Memento 패턴 상태 저장
- 10월: 데미지 폰트 풀링, 난수 시드 동기화
- 08–09월: Dictionary/SortedList 기반 대용량 데이터 리팩토링
- 06–07월: GraphView 다이얼로그 에디터, UI 가상화
- 04–05월: 베지어 투사체, 슬로우 모션 연출
- 02–03월: ATB 행동바, UI 컴포넌트 일괄 교체 툴

### 2024
- 10–12월: 전투 FSM 아키텍처 설계, Addressables 최적화
- 04–09월: Vector2d 좌표계, 메쉬 병합 기반 렌더링 최적화
- 01–03월: 제네릭 데이터 매니저, 소셜 로그인 모듈 연동