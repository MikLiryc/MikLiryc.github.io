---
layout: post
title: "Game Client Developer Portfolio - Cyril"
date: 2026-02-06
categories: [Resume, Portfolio]
tags: [Unity, C#, Client Developer]
---

# 김재현 (Cyril)
> **Unity Client Developer**
>
> **"견고한 시스템 설계와 집요한 최적화로 가치 있는 플레이 경험을 만듭니다."**

- **Email:** jay.kim1994@gmail.com
- **Github:** https://github.com/Mikliryc

---

## Professional Summary

4년 차 유니티 클라이언트 개발자로, **확장성 있는 아키텍처 설계**와 **개발 프로세스 효율화**에 강점이 있습니다.
트랜스포머 IP 기반의 대형 모바일 프로젝트에서 전투, LBS, 시스템 등 핵심 코어를 **주도적으로 개발**했습니다.
단순한 기능 구현을 넘어, `Vector2d` 좌표계 구현이나 메쉬 병합과 같은 기술적 난제를 해결하며 **안정적이고 최적화된 서비스 환경**을 구축하는 데 기여했습니다.

---

## Technical Skills

### Languages & Engines
* **Language**: C# (Advanced), HLSL (Basic)
* **Engine**: Unity 2022/2023
* **Version Control**: Git

### Core Competencies
* **Architecture**: FSM (Finite State Machine), Command Pattern, Observer Pattern, Memento Pattern
* **Data Structure**: Dictionary, Queue, Stack, SortedList, Graph (Node-Edge)
* **Optimization**: Object Pooling, Mesh Combine, DrawCall Batching, GC Alloc Reduction
* **Tools**: Unity Editor Scripting (GraphView, Custom Inspector), Addressables, MapBox SDK

---

## Experience

### **Project: Transformers Alliance**

### **(주)스노우파이프**

<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 5px;">
  <span style="font-weight: bold; font-size: 1.1em; color: #eeeeee;">클라이언트 파트장</span>
  <span style="color: #666; font-family: monospace; font-size: 0.9em;">2024.11 ~ 현재</span>
</div>

> **Role: 팀 개발 인프라 구축, 생산성 도구 개발, 코어 시스템 리팩토링 및 기술 리딩**

* **개발 생산성 도구 (DevOps & Tools)**
  * **다이얼로그 노드 에디터**: Unity `GraphView` API를 활용하여 기획자가 대화 분기 및 연출을 시각적으로 제어할 수 있는 전용 에디터 개발. (XML/Excel 의존성 제거)
  * **맵 테스트 시뮬레이터**: GPS 하드웨어 의존성을 제거하기 위해 Unity `Input System` 기반의 가상 위치 시뮬레이터를 구축하여 QA 및 개발 테스트 효율 증대.
  * **에셋 관리 자동화**: 프리팹 내부를 재귀적으로 탐색하는 알고리즘을 적용, 변경된 폰트/UI 리소스만 선별적으로 저장하는 툴을 제작하여 휴먼 에러 방지.

* **시스템 아키텍처 및 최적화 (Architecture & Optimization)**
  * **전투 시스템 FSM 리팩토링**: 기존 스파게티 코드를 `BattleStateMachine` 기반의 FSM(유한 상태 머신) 구조로 재설계하여 유지보수성 및 확장성 확보.
  * **데이터 구조 최적화**: 미션 시스템의 탐색 로직을 `List`에서 `Dictionary`/`SortedList`로 전면 교체하여 데이터 조회 성능 개선 (**O(n) → O(1)**).
  * **메모리 관리 (Pooling & Virtualization)**:
    * 전투 이펙트/데미지 폰트에 `Generic Object Pool` 도입으로 GC Alloc 최소화.
    * `EnhancedScroller` 기반의 UI 가상화 적용으로 대용량 리스트 렌더링 성능 최적화.

* **테크니컬 아트 및 고급 연출 (Tech Art)**
  * **AR 쉐이더 구현**: Stencil Buffer를 활용한 마스킹 쉐이더(Masking Shader)를 직접 작성하여 현실 공간에 균열이 생긴듯한 AR 연출 구현.
  * **립싱크 자동화 시스템**: 오디오 파형(RMS) 분석 알고리즘을 통해 별도의 애니메이션 작업 없이 사운드에 맞춰 입모양(BlendShape)이 동기화되는 시스템 구축.

<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 5px;">
  <span style="font-weight: bold; font-size: 1.1em; color: #eeeeee;">클라이언트 팀원</span>
  <span style="color: #666; font-family: monospace; font-size: 0.9em;">2022.12 ~ 2024.11</span>
</div>

> **Role: LBS 엔진 코어 구현, 전투 시스템 프로토타이핑 및 콘텐츠 개발**

* **LBS 엔진 코어 (Location Based Service)**
  * **고정밀 좌표계 구현**: `float`의 정밀도 한계를 극복하기 위해 `Vector2d` (Double Precision) 구조체를 자체 구현하여 GPS 좌표 오차 해결.
  * **맵 렌더링 최적화**: MapBox 타일 생성 시 `Mesh.CombineMeshes`를 활용한 배칭(Batching) 처리를 구현하여 모바일 환경에서의 Draw Call 방어.
  * **좌표 변환 유틸리티**: WGS84(위경도) 좌표계와 Unity World 좌표계 간의 상호 변환 로직 및 동적 오브젝트 배치 시스템 구현.

* **전투 및 성장 시스템 구현 (Gameplay)**
  * **ATB 전투 로직**: 유닛의 Speed 스탯에 따라 턴을 획득하는 Active Time Battle(ATB)의 초기 알고리즘 및 틱(Tick) 시뮬레이션 구현.
  * **결정론적 동기화**: 서버로부터 수신한 Seed 값을 기반으로 난수를 생성하는 로직을 적용하여, 클라이언트 간 전투 결과 불일치 문제 해결.
  * **성장 및 관리 콘텐츠**: 캐릭터 도감, 파워칩 장착/해제, 강화 등 성장 관련 UI 및 클라이언트 데이터 처리 로직 구현.

* **데이터 및 네트워크 (Foundation)**
  * **제네릭 데이터 매니저**: JSON/CSV 포맷의 테이블 데이터를 제네릭(`DataManager<T>`) 형태로 파싱하고 관리하는 기반 클래스 설계.
  * **네트워크 기본 모듈**: 로그인(Auth), 서버 시간 동기화, 기본 패킷 송수신 처리를 위한 통신 모듈 구현.

### **Project: 피구왕 통키 M**

<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 5px;">
  <span style="font-weight: bold; font-size: 1.1em; color: #eeeeee;">(주)스노우파이프</span>
  <span style="color: #666; font-family: monospace; font-size: 0.9em;">2021.04 ~ 2022.12</span>
</div>

> *피구왕 통키 M 한국 라이브 서버 유지보수 및 대만 서버 유지보수/업데이트 작업*

---

## Detailed Technical Log (Monthly)

### **2026**
* **02월 (Tools)**: 재귀 탐색 알고리즘을 적용한 폰트 일괄 교체 및 에셋 최적화 툴 고도화.
* **01월 (LBS)**: 위성 지도 동적 로딩 기능 및 Input System 기반 맵 테스트 시뮬레이터 구축.

### **2025**
* **12월 (AR/System)**: AR 평면 인식 정밀도 개선 및 통신 글리치(Glitch) 쉐이더 구현.
* **11월 (Dialog)**: 오디오 분석 기반 실시간 립싱크 및 Memento 패턴을 활용한 상태 저장 시스템.
* **10월 (Battle/Opt)**: 데미지 폰트 전용 오브젝트 풀링(Stack) 적용 및 난수 시드 동기화 로직.
* **08월 ~ 09월 (Mission)**: 대규모 데이터 처리를 위한 자료구조 리팩토링(Dictionary/SortedList).
* **06월 ~ 07월 (Tools/UI)**: GraphView 기반 다이얼로그 노드 에디터 및 UI 무한 스크롤(Virtualization) 적용.
* **04월 ~ 05월 (Visual)**: 베지어 곡선 투사체 및 AnimationCurve 기반 슬로우 모션 연출 구현.
* **02월 ~ 03월 (Battle)**: ATB 행동바(Action Bar) 로직 설계 및 UI 컴포넌트 일괄 교체 툴 제작.

### **2024**
* **10월 ~ 12월 (Arch)**: 유연한 확장성을 고려한 전투 FSM 아키텍처 설계 및 Addressables 최적화.
* **04월 ~ 09월 (LBS)**: 고정밀 Vector2d 좌표계 구현 및 메쉬 병합(Combine)을 통한 렌더링 최적화.
* **01월 ~ 03월 (Core)**: 제네릭 기반 데이터 매니저 설계 및 소셜 로그인 모듈 연동.