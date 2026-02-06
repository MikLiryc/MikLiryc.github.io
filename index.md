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

## Work Experience

### **Project: Transformers Alliance**
**Position:** 클라이언트 개발자 (Unity) 
**기간:** 2022.12 ~ 현재

#### **1. 전투 시스템 (Battle System)**
**"유연하고 확장 가능한 턴제 전투 아키텍처 설계"**

* **견고한 FSM 구조 도입**: 복잡한 전투 로직을 `Ready` → `TurnCheck` → `Action` → `Result` 상태로 모듈화하여, 유지보수가 용이하고 확장에 유연한 **BattleStateMachine**을 설계했습니다.
* **정교한 ATB 시뮬레이션**: 유닛의 Speed 스탯에 따라 틱(Tick)이 차오르는 정교한 게이지 시스템을 구현하여 전략적인 전투 흐름을 완성했습니다.
* **의존성 최소화 (Decoupling)**: `IBattleAnimationControllerDelegate` 인터페이스를 정의하여, 로직(Model)과 연출(View) 간의 결합도를 낮춘 **유연한 코드 구조**를 확립했습니다.
* **결정론적(Deterministic) 동기화**: 서버 Seed 기반의 난수 시스템을 구축하여, 모든 디바이스에서 **동일한 전투 결과**를 보장하는 신뢰성 있는 로직을 구현했습니다.
* **메모리 최적화**: `Stack<T>` 기반의 커스텀 오브젝트 풀링을 적용, 빈번한 객체 생성/파괴로 인한 GC 스파이크를 방지하고 **안정적인 프레임**을 확보했습니다.

#### **2. LBS (Location Based Service) & Map**
**"기술적 한계를 극복한 대규모 맵 시스템 구축"**

* **정밀한 좌표계 처리**: `float`의 정밀도 한계를 극복하기 위해 `Double Precision` 기반의 `Vector2d` 구조체를 직접 구현하여, GPS 좌표 오차 없는 **정확한 위치 서비스**를 제공했습니다.
* **렌더링 성능 최적화**:
    * MapBox 타일 생성 시 `Mesh.CombineMeshes`를 활용한 병합 로직으로 Draw Call을 획기적으로 줄였습니다.
    * 불필요한 레이어(Road, Water) 생성을 원천 차단하는 로직으로 메모리 사용량을 **효율적으로 개선**했습니다.
* **테스트 효율화 주도**: GPS 모듈 없이도 에디터에서 이동 테스트가 가능한 `Input System` 기반 시뮬레이터를 **주도적으로 개발**하여 QA 및 개발 효율을 크게 높였습니다.

#### **3. 툴 개발 (Tools & Editor Extension)**
**"개발 생산성을 높이는 직관적인 파이프라인 구축"**

* **직관적인 다이얼로그 에디터**: Unity **GraphView API**를 활용하여, 기획자가 복잡한 대화 분기를 시각적으로 제어할 수 있는 노드 에디터를 개발했습니다.
* **데이터 관리 자동화**: 그래프 데이터를 런타임에 최적화된 `ScriptableObject` 구조로 직렬화(Serialization)하는 빌드 파이프라인을 구축했습니다.
* **스마트한 에셋 관리 툴**: 프리팹 내부를 재귀적으로 탐색하여 폰트를 일괄 교체하고, 변경된 에셋만 선별적으로 저장하는 **지능형 자동화 툴**을 제작해 반복 작업을 제거했습니다.

#### **4. 시스템 및 컨텐츠 (System & Contents)**
**"몰입감을 극대화하는 연출 및 데이터 시스템"**

* **정교한 연출 동기화**: 텍스트 태그(`<shake>`, `<cmd>`)를 파싱하여 타이핑 시점에 정확히 연출을 실행하는 **Command Pattern** 기반 시퀀서를 구현했습니다.
* **실시간 립싱크 기술**: 오디오 파형(RMS) 분석 알고리즘을 통해 캐릭터 입모양(BlendShape)을 실시간으로 제어하는 **생동감 있는 연출**을 구현했습니다.
* **고성능 데이터 처리**: 미션 데이터 컨테이너를 `Dictionary` 및 `SortedList`로 재설계하여 탐색 속도를 **획기적으로 개선**(`O(n)` → `O(1)`)했습니다.
* **UI 가상화(Virtualization)**: `EnhancedScroller`를 도입하여 대량의 리스트도 끊김 없이 렌더링하는 **최적화된 UI 시스템**을 완성했습니다.

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