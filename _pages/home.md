<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=900, initial-scale=1.0">
  <title>김재현 (Cyril) - Resume</title>
  <link rel="stylesheet" href="/assets/main.css">
  <style>
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
    }
    body {
      min-height: 100vh;
      background: #181c22;
      color: #f3f3f3;
      font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .resume-container {
      max-width: 900px;
      width: 100%;
      margin: 40px auto;
      background: #23272e;
      border-radius: 12px;
      box-shadow: 0 2px 16px 0 rgba(0,0,0,0.10);
      padding: 40px 36px 48px 36px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    h1 { font-size: 2.3rem; font-weight: 800; margin-bottom: 0.2em; }
    h2 { font-size: 1.3rem; font-weight: 700; margin-top: 2.5em; margin-bottom: 0.7em; border-bottom: 1px solid #444; padding-bottom: 0.2em; }
    h3 { font-size: 1.08rem; font-weight: 600; margin-top: 1.5em; margin-bottom: 0.5em; }
    .subtitle { color: #bdbdbd; font-size: 1.1em; margin-bottom: 1.2em; }
    .section { margin-bottom: 2.5em; width: 100%; }
    .date-col { color: #bdbdbd; font-weight: 600; width: 160px; font-size: 1.04em; }
    .topic-col { font-size: 1.13em; font-weight: 700; }
    .project-col { color: #bdbdbd; font-size: 0.98em; margin-bottom: 0.2em; }
    .contents-col ul { margin: 0.2em 0 0.7em 0; padding-left: 1.2em; }
    .contents-col li { margin-bottom: 0.18em; }
    .hr { border: 0; border-top: 1.5px solid #444; margin: 24px 0 24px 0; }
    .tag { display: inline-block; background: #333; color: #eee; border-radius: 6px; font-size: 0.95em; padding: 2px 10px; margin: 0 2px 4px 0; }
    a { color: #8ec6ff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    @media (max-width: 950px) {
      .resume-container { max-width: 100vw; padding: 16px 4vw; }
    }
  </style>
</head>
<body>
<div class="resume-container">
  <h1>김재현 (Cyril)</h1>
  <div class="subtitle">Unity Client Developer</div>
  <div style="margin-bottom:1.2em;">
    <b>“견고한 시스템 설계와 집요한 최적화로 가치 있는 플레이 경험을 만듭니다.”</b>
  </div>
  <div style="margin-bottom:1.5em;">
    <b>Email:</b> jay.kim1994@gmail.com<br>
    <b>GitHub:</b> <a href="https://github.com/MikLiryc" style="color:#8ec6ff;">github.com/MikLiryc</a>
  </div>

  <h2>Professional Summary</h2>
  <div class="section">
    4년 차 유니티 클라이언트 개발자로 <b>확장성 있는 아키텍처 설계</b>, <b>개발 프로세스 효율화(툴링)</b>, <b>성능 최적화</b>에 강점이 있습니다.<br>
    대형 모바일 프로젝트에서 전투·LBS·시스템 코어를 개발하며, 이슈를 "수정"으로 끝내지 않고 <b>재현 → 원인 분석 → 구조 개선</b>으로 안정화하는 방향을 선호합니다.<br>
    <span class="tag">Unity</span> <span class="tag">C#</span> <span class="tag">Architecture</span> <span class="tag">Optimization</span> <span class="tag">Tools</span> <span class="tag">LBS</span> <span class="tag">Timeline</span> <span class="tag">Cinemachine</span>
  </div>

  <h2>Work Experience</h2>
  <div class="section">
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2026.01 ~ 2026.02</td>
        <td>
          <div class="topic-col">빌드 안정화 및 공용 툴 개발</div>
          <div class="project-col">Project: Transformers Alliance (Mobile)</div>
          <ul>
            <li>지난 빌드 이후 체크된 각종 버그 수정 및 구조 안정화</li>
            <li>UI팀이 수동으로 폰트 에셋을 교체하지 않아도 되도록 UI 폰트 에셋 교체/관리 자동화 툴 개발</li>
          </ul>
        </td>
      </tr>
    </table>
    <hr class="hr">
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2025.09 ~ 2025.12</td>
        <td>
          <div class="topic-col">다이얼로그 시스템 개발 및 전투 연출 리팩토링</div>
          <div class="project-col">Project: Transformers Alliance (Mobile)</div>
          <ul>
            <li>내용 1</li>
            <li>내용 2</li>
            <li>내용 3</li>
          </ul>
        </td>
      </tr>
    </table>
    <hr class="hr">
    <div style="font-weight:700;">클라이언트 파트장 · 2024.11 – 현재</div>
    <div style="font-weight:700;">클라이언트 팀원 · 2022.12 – 2024.11</div>
    <ul>
      <li>Cinemachine 기반 전투 시스템 및 연출 파이프라인 구조 설계, 개발</li>
      <li>전투 시스템 리팩토링을 통해 유지보수성 및 안정성 개선</li>
      <li>Unity Input System 기반 LBS 맵 테스트 시뮬레이터 개발로 GPS 의존성 제거 및 테스트 효율화</li>
      <li>GOMap API 중, Open Street Map (OSM) 데이터를 기반으로 3D 지도를 생성하는 대신, Static Image API 를 사용하여 위성 지도 이미지를 불러오는 등 Satellite 모드 대응 로직 개발</li>
      <li>FSM 기반 전투 시스템 아키텍처 설계 및 구현</li>
      <li>UI 폰트 일괄 교체 툴 개발로 대량 프리팹 작업 자동화 및 휴먼 에러 최소화</li>
      <li>Object Pooling, Mesh Combine을 통한 렌더링 성능 개선</li>
      <li>신규 멤버 온보딩 및 코드 리뷰 프로세스 정립</li>
    </ul>
    <div style="margin-top:0.7em; color:#bdbdbd; font-size:0.98em;">
      <b>기술 스택:</b> Unity, C#, Cinemachine, GOMap SDK, Input System, FSM, Object Pooling
    </div>
    <h3>피구왕 통키 M (Live Ops)</h3>
    <div style="font-weight:700;">클라이언트 팀원 · 2021.04 – 2022.12</div>
    <ul>
      <li>라이브 운영 콘텐츠 개발 및 안정화</li>
      <li>UI 시스템 최적화 및 성능 개선</li>
    </ul>
  </div>

  <h2>Projects</h2>
  <div class="section">
    <!-- 예시 프로젝트 카드 반복 -->
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2025.11 ~ 2025.12</td>
        <td>
          <div class="topic-col">전투 연출 파이프라인 리팩토링</div>
          <div class="project-col">Timeline/Cinemachine 기반 상태 관리 시스템</div>
          <div style="margin-bottom:0.3em; font-weight:600;">문제</div>
          <ul>
            <li>연출 프리팹과 PlayableDirector 관리가 불명확하여 유지보수 어려움</li>
            <li>상태 전환 시 한 프레임 튐 등 체감 이슈 발생</li>
            <li>강스킬/HealthCheck 구간의 카메라/트랜스포머 위치 예외 케이스 처리 불안정</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">해결</div>
          <ul>
            <li>Intro → Confrontation → Skill Ready/Fail/StrongSkill → HealthCheck 흐름을 상태 기반으로 구조화</li>
            <li>연출 프리팹을 상태 단위로 관리하여 "누가 무엇을 언제 잡는지" 명확화</li>
            <li>전환 타이밍 트랜지션 루틴 정리로 한 프레임 튐 현상 완화</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">성과</div>
          <ul>
            <li>연출 코드 유지보수성 향상</li>
            <li>강스킬/HealthCheck 구간 예외 케이스 안정화</li>
          </ul>
        </td>
      </tr>
    </table>
    <hr class="hr">
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2026.01</td>
        <td>
          <div class="topic-col">LBS 맵 테스트 시뮬레이터</div>
          <div class="project-col">Unity Input System 기반 에디터 테스트 환경</div>
          <div style="margin-bottom:0.3em; font-weight:600;">문제</div>
          <ul>
            <li>GPS 의존으로 인한 에디터 내 재현 불가</li>
            <li>실기기 테스트 필수로 인한 테스트 루프 지연</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">해결</div>
          <ul>
            <li>Input System Action 기반 이동/줌/상태 테스트 환경 구축</li>
            <li>타일 로딩/생성/파괴 진행 상태를 콜백으로 수집해 디버깅 편의 개선</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">성과</div>
          <ul>
            <li>GPS 의존성 제거</li>
            <li>에디터 내 재현 가능한 테스트 환경 확보로 개발 효율화</li>
          </ul>
        </td>
      </tr>
    </table>
    <hr class="hr">
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2026.01</td>
        <td>
          <div class="topic-col">MapBox 외부 API 대응 및 비용 최적화</div>
          <div class="project-col">Static Image API 변경 대응 + Satellite 모드 분기 처리</div>
          <div style="margin-bottom:0.3em; font-weight:600;">문제</div>
          <ul>
            <li>MapBox Static Image API 변경으로 지도 로딩 실패</li>
            <li>Satellite 모드에서 불필요한 도로/물/빌딩 레이어 생성으로 비용 증가</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">해결</div>
          <ul>
            <li>Static Image URL 및 영역 산정 로직 보정</li>
            <li>Satellite 배경 사용 시 도로/물/빌딩 레이어 생성 스킵 분기 추가</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">성과</div>
          <ul>
            <li>외부 API 변경 이슈 해결</li>
            <li>Satellite 모드 비용 절감</li>
          </ul>
        </td>
      </tr>
    </table>
    <hr class="hr">
    <table style="width:100%; border:none; border-collapse:collapse;">
      <tr>
        <td class="date-col">2025.03, 2026.02</td>
        <td>
          <div class="topic-col">UI 폰트 일괄 교체 툴</div>
          <div class="project-col">Prefab 재귀 탐색 자동화 툴 (2026.02 고도화)</div>
          <div style="margin-bottom:0.3em; font-weight:600;">문제</div>
          <ul>
            <li>대량 프리팹 폰트 교체 작업의 휴먼 에러 및 불필요한 변경 발생</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">해결</div>
          <ul>
            <li>프리팹 내 텍스트 컴포넌트 재귀 탐색 및 대상 폰트 일괄 교체</li>
            <li>변경 없는 프리팹 저장 방지로 변경 노이즈 감소</li>
          </ul>
          <div style="margin-bottom:0.3em; font-weight:600;">성과</div>
          <ul>
            <li>반복 작업 자동화</li>
            <li>작업 시간 단축 및 휴먼 에러 최소화</li>
          </ul>
        </td>
      </tr>
    </table>
  </div>

  <h2>Skills</h2>
  <div class="section">
    <b>Languages & Engine</b><br>
    C# (Advanced), HLSL (Basic), Unity 2022/2023, Git
    <br><br>
    <b>Architecture & Design Patterns</b><br>
    FSM, Command, Observer, Memento, Dictionary, Queue/Stack, SortedList, Graph(Node–Edge)
    <br><br>
    <b>Performance Optimization</b><br>
    Object Pooling, Mesh Combine, DrawCall Batching, GC Alloc Reduction, UI Virtualization (EnhancedScroller)
    <br><br>
    <b>Tools & Pipeline</b><br>
    Unity Editor Scripting (GraphView, Custom Inspector), Addressables, GOMap SDK, Unity Input System
  </div>

  <h2>Technical Highlights</h2>
  <div class="section">
    <b>2026</b><br>
    <span class="date-col">02월</span>: 폰트 일괄 교체 툴 고도화 (변경 없는 프리팹 저장 방지 로직 추가)<br>
    <span class="date-col">01월</span>: Input System 기반 맵 테스트 시뮬레이터, Satellite 동적 로딩/타일 로직 보정<br>
    <br>
    <b>2025</b><br>
    <span class="date-col">12월</span>: AR 평면 인식 정밀도 개선, 글리치 쉐이더 구현<br>
    <span class="date-col">11월</span>: 오디오 분석 기반 립싱크, Memento 패턴 상태 저장 시스템<br>
    <span class="date-col">10월</span>: 데미지 폰트 풀링, 난수 시드 동기화<br>
    <span class="date-col">08–09월</span>: Dictionary/SortedList 기반 대용량 데이터 리팩토링<br>
    <span class="date-col">06–07월</span>: GraphView 다이얼로그 에디터, UI 가상화<br>
    <span class="date-col">04–05월</span>: 베지어 투사체, 슬로우 모션 연출<br>
    <span class="date-col">02–03월</span>: ATB 행동바, UI 컴포넌트 일괄 교체 툴<br>
    <br>
    <b>2024</b><br>
    <span class="date-col">10–12월</span>: 전투 FSM 아키텍처 설계, Addressables 최적화<br>
    <span class="date-col">04–09월</span>: Vector2d 좌표계, 메쉬 병합 기반 렌더링 최적화<br>
    <span class="date-col">01–03월</span>: 제네릭 데이터 매니저, 소셜 로그인 모듈 연동<br>
  </div>
</div>
</body>
</html>
