# Portfolio Site 개선 계획 (Commit Log 기반)

## 분석 결과
- 800+ 커밋 분석 (2023.01 ~ 2026.02)
- 주요 시스템: 전투(FSM), 다이얼로그(Memento), AR 소환게임, LBS, 도감, 미션, 에디터 툴

## 실행 완료 항목

### ✅ 1. _config.yml - temp 파일 빌드 제외
- `temp_*.txt` 패턴 추가

### ✅ 2. Sticky TOC 네비게이션 추가
- 왼쪽 사이드바 고정 위치
- IntersectionObserver 기반 현재 섹션 하이라이트
- 1350px 이하 화면에서 자동 숨김
- smooth scroll 적용

### ✅ 3. 섹션 ID 부여
- about, summary, experience, projects, skills, highlights
- detail-gomap (기존), detail-battle (신규), detail-dialogue (신규)

### ✅ 4. Work Details: 전투 시스템 파이프라인 추가
- 발단 → 현상 파악 → 접근 방법 → 결과 구조
- FSM 아키텍처 의사코드 포함
- BattleStandalone 독립 테스트 씬, ATB 행동바 언급
- 개선 효과 정량적 기술

### ✅ 5. Work Details: 다이얼로그 시스템 추가
- DialogSequencer (DeltaTime 보정 텍스트 엔진) 코드 포함
- 인라인 커맨드 파서 (BGM/SFX/CameraShake/Animation/Wait)
- Stack 기반 Memento 패턴 상태 관리 코드 포함
- GraphView 에디터 설명
- Work Experience에서 상세 링크 연결

### ✅ 6. Footer 추가
- 저작권, GitHub 링크, 이메일

### ✅ 7. Work Experience 내 상세 링크 추가
- 전투 시스템 → #detail-battle
- 다이얼로그 시스템 → #detail-dialogue

## 향후 고려사항
- ~~FSM 상태 흐름도 이미지/다이어그램 추가~~ ✅ CSS 기반 다이어그램으로 구현
- GraphView 에디터 스크린샷 추가 (이미지 파일 필요)
- ~~AR 소환게임 상세 섹션 추가 가능~~ ✅ 구현 완료

## 추가 완료 항목

### ✅ 8. FSM 상태 흐름도 다이어그램 (CSS 기반)
- Intro → Confrontation → SkillReady → StrongSkill/SkillFail → HealthCheck → Result
- 분기(Success/Fail, HP잔여/HP=0) 시각화
- 전투 상세 섹션(#detail-battle)에 삽입

### ✅ 9. AR 소환게임 상세 섹션 추가 (#detail-ar)
- 발단 → 현상 파악 → 접근 방법 → 결과 구조
- 전체 연출 플로우 다이어그램 (CSS 기반)
- 스파크 물리 발사 메커닉 의사코드
- 카메라 각도 기반 포탈 위치 동적 보간 코드
- 에디터 테스트 환경 설명
- Work Experience에서 상세 링크(→) 연결
- TOC에 "Detail: AR 소환" 항목 추가

# 📋 Step 2: Git Log 심층 분석 기반 이력서 보강 계획

## 🔍 Git Log 분석 결과 요약

- **전체 기간**: 2022.12 ~ 2026.02 (약 3년 2개월)
- **유의미한 커밋**: 약 800+ 건 (merge/빈 커밋 제외)
- **주요 작업 카테고리**: 전투, LBS, 소환게임, 다이얼로그, 도감, 미션, 지휘통제실, 도구함, 파워칩, 에디터 툴, 사운드, 햅틱, 에셋번들, 카메라, 최적화 등 **20+ 영역**

---

## ✅ 실행 완료 항목

### ✅ 1. PROFESSIONAL SUMMARY 보강
- ~~"3년 이상" → "3년 이상, 800+ 커밋"~~ → 사용자 요청으로 제외
- ✅ 에셋번들, 테이블 파이프라인 등 **인프라 역량** 언급 추가
- ✅ 태그에 Asset Bundle, SQLite 추가

### ✅ 2. WORK EXPERIENCE 파트장 기간 항목 추가
- ✅ 전투력 변화 연출 시스템
- ~~평판(Reputation) 시스템~~ → 사용자 요청으로 제외
- ✅ 전용재화 시스템
- ✅ Unity 6 엔진 업그레이드
- ✅ 수량 체크 시스템 (CapacityRestriction)

### ✅ 3. WORK EXPERIENCE 팀원 기간 항목 추가/보강
- ✅ 권능의사당 (Temple of Power)
- ✅ 에셋번들 관리 시스템
- ✅ 테이블 데이터 파이프라인
- ✅ 보상 팝업 시스템
- ✅ 계정/로그인 시스템 (공용 시스템에 보강)
- ✅ 상점/가챠 시스템
- ✅ 인앱 결제 (공용 시스템에 보강)

### ✅ 4. PROJECTS 섹션 누락 프로젝트 추가
- ✅ 전투력 변화 연출 (2025.04~05 섹션에 추가)
- ✅ 권능의사당 개발 (2025.01~02 신규 섹션)
- ✅ 에셋번들 시스템 안정화 (2024~2025 신규 섹션)
- ✅ SQLite 테이블 파이프라인 (전 기간 신규 섹션)

### ✅ 5. TECHNICAL HIGHLIGHTS 보강
- ✅ 2025.01 → 권능의사당(TempleOfPower) 개발, ATB 버그 수정 추가
- ✅ 2025.05 → 전투력 변화 연출 시스템 추가
- ✅ 2025.10 → Unity 6 엔진 업그레이드 추가
- ✅ 2025.12 → 전용재화 테이블 전환 추가
- ✅ 2023 → 보상 팝업, 상점, IAP 하이라이트 추가
- ✅ "전 기간" 에셋번들/테이블 파이프라인 하이라이트 추가

### ✅ 6. SKILLS 섹션 보강
- ✅ Asset Bundle Management 추가
- ✅ SQLite → "SQLite 데이터 파이프라인" 강화
- ✅ IAP (In-App Purchase) 추가
- ✅ Unity 6 엔진 버전 명시 (기존 유지)
- ✅ 엑셀→SQLite 변환 파이프라인 (Tools & Pipeline에 추가)

---

## 📝 작업 순서 (전체 완료)

1. ✅ **PROFESSIONAL SUMMARY** 보강 (인프라 역량)
2. ✅ **WORK EXPERIENCE 파트장 기간** 항목 추가
3. ✅ **WORK EXPERIENCE 팀원 기간** 항목 추가/보강
4. ✅ **PROJECTS 섹션** 누락 프로젝트 추가
5. ✅ **TECHNICAL HIGHLIGHTS** 월별 누락 내용 보강
6. ✅ **SKILLS** 섹션 보강
