# WSOP TV OTT Solution PRD

**Version**: 3.0.0
**Date**: 2026-01-21
**Reference**: NBA TV League Pass
**Wireframes**: 13개 B&W 목업 완성
**Design Principle**: NBA TV 1:1 복제 (용어만 변경)

---

## 0. 설계 원칙

### 0.1 핵심 원칙: NBA TV 1:1 대응

> **"주관적 해석 배제, 최대한 동일한 디자인 레이아웃 설계"**

본 PRD는 NBA TV League Pass의 UI/UX를 **1:1 복제**하여 WSOP TV로 변환합니다.
- **변경**: 용어 (Game→Tournament, Score→Chips 등)
- **유지**: 레이아웃, 구조, 인터랙션, 컴포넌트 배치
- **금지**: NBA TV에 없는 기능의 Core 포함

### 0.2 기능 분류

| 분류 | 정의 | 예시 |
|------|------|------|
| **Core** | NBA TV에 존재하는 기능의 1:1 대응 | Ticker, MultiView, Key Plays |
| **Extension** | 포커 도메인 특화 확장 기능 | Equity Meter, Hand Range |

### 0.3 전체 용어 매핑

| NBA TV | WSOP TV | 비고 |
|--------|---------|------|
| Scoreboard Ticker | Tournament Ticker | 동일 구조 |
| Q3 3:05 | L38 LIVE | Quarter→Level |
| Clippers 77 / Bulls 90 | Negreanu 1.3M | 점수→칩 리더 플레이어 |
| League Pass | WSOP+ | 동일 |
| CLIPPERS @ BULLS | [♠] MAIN EVENT 2024 | 팀→이벤트 |
| Bulls (In-Arena) | Main Table Cam | 동일 |
| Streams 9 | Active Tables 45 | 동일 구조 |
| Key Plays | Featured Hands | 동일 구조 |
| Summary | Summary | 동일 |
| Box Score | Player Stats | 동일 |
| Game Charts | Hand Charts | 동일 |
| Play-By-Play | Hand History | 동일 |

### 0.4 Streaming Options 매핑

#### Broadcasts → Camera
| NBA TV | WSOP TV |
|--------|---------|
| Bulls (In-Arena) | Main Table Cam |
| Clippers (In-Arena) | Rail Cam |
| Bulls (Studio Show) | Dealer Cam |
| Clippers (Studio Show) | Player Focus Cam |
| Mobile View | Arena Overview Cam |

#### Audio → Commentary
| NBA TV | WSOP TV |
|--------|---------|
| Bulls Radio | English Commentary |
| Clippers Radio | Spanish Commentary |
| Spanish | Portuguese/Korean 등 |

### 0.5 Box Score → Player Stats 컬럼 매핑

| NBA TV | WSOP TV | 설명 |
|--------|---------|------|
| MIN | HANDS | 플레이 시간/핸드 |
| FGM | WINS | 성공 횟수 |
| FG% | WIN% | 성공률 |
| 3PM | VPIP | 3점슛/팟 참여 |
| 3PA | PFR | 3점슛 시도/프리플랍 레이즈 |
| REB | CHIPS | 리바운드/칩 |
| +/- | +/- | 동일 |

### 0.6 레퍼런스 문서

- **NBA TV 원본 분석**: [`NBATV-SCREENSHOT-ANALYSIS.md`](./NBATV-SCREENSHOT-ANALYSIS.md)
- **스크린샷 26개**: `docs/guides/` (113524~145658)

---

## 1. 개요

### 1.1 프로젝트 배경
WSOP(World Series of Poker) 대회의 라이브 스트리밍 서비스를 위한 OTT 플랫폼 구축. NBA TV League Pass의 검증된 UX 패턴을 기반으로 포커 대회 특화 기능을 추가.

### 1.2 목표
- 전 세계 포커 팬에게 프리미엄 라이브 스트리밍 경험 제공
- 다중 테이블 동시 시청 지원
- 실시간 통계 및 핸드 히스토리 제공
- 30분 딜레이 스트림으로 홀카드 공개

### 1.3 범위
| 포함 | 제외 |
|------|------|
| 라이브 스트리밍 | 온라인 포커 플레이 |
| VOD 다시보기 | 베팅 기능 |
| 통계/분석 | 소셜 기능 (v2) |
| 다국어 해설 | 모바일 앱 (v2) |

---

## 2. 핵심 기능

### 2.1 라이브 스트리밍 `[Core]`

> **NBA TV 대응**: Main Streaming UI (7단 레이아웃)

#### Tournament Ticker (상단 바) `[Core]`

![메인 스트리밍 UI](../images/mockups/wsoptv/01-main-streaming.png)

> **목업 파일**: [`01-main-streaming.html`](../mockups/wsoptv/01-main-streaming.html)

| 요소 | 설명 |
|------|------|
| Day/Flight | DAY 2A, DAY 3, FINAL 등 |
| Level | 현재 블라인드 레벨 (Level 15) |
| Blinds | 1K/2K/200 (SB/BB/Ante) |
| Table | Table 42 (8 Players) |
| Avg Stack | 평균 스택 (Avg: 125K) |
| Tag | [Featured], [Final Table], [Bubble], BREAK |

### 2.2 MultiView (다중 테이블) `[Core]`

![MultiView Selector](../images/mockups/wsoptv/04-multiview-selector.png)

> **목업 파일**: [`04-multiview-selector.html`](../mockups/wsoptv/04-multiview-selector.html)
>
> **NBA TV 대응**: MultiView Selector (1x1, 1:2, 2x2)

| 레이아웃 | 설명 | NBA TV |
|----------|------|--------|
| 1x1 | 단일 테이블 풀스크린 | ✅ 동일 |
| 1:2 | 메인+사이드 분할 | ✅ 동일 |
| 2x2 | 4개 테이블 | ✅ 동일 |

**Core 기능 (NBA TV 동일):**
- "Add a Table from Tournament Ticker" - 스코어 스트립에서 테이블 추가
- "Catch up with Featured Hands" - 주요 핸드로 이동

**Extension 기능 (포커 전용):**
- 3x3 레이아웃 (9개 테이블 동시 - 파이널 데이용)

### 2.3 Featured Hands (Key Plays) `[Core]`

![Featured Hands Modal](../images/mockups/wsoptv/10-modal-featuredhands.png)

> **목업 파일**: [`10-modal-featuredhands.html`](../mockups/wsoptv/10-modal-featuredhands.html)
>
> **NBA TV 대응**: Key Plays (모달 + 플레이어)

| 요소 | 설명 | NBA TV |
|------|------|--------|
| 썸네일 | 핸드 하이라이트 이미지 | ✅ 동일 |
| 설명 | "AA vs KK All-in on the Bubble" | ✅ 동일 |
| 시간 | Level 38 • Hand #245 | Q1 • 00:49.5 대응 |
| 네비게이션 | Next, Previous, Jump to Live | ✅ 동일 |

### 2.4 Player Stats & Analytics `[Core]`

![Player Stats](../images/mockups/wsoptv/07-info-playerstats.png)

> **목업 파일**: [`07-info-playerstats.html`](../mockups/wsoptv/07-info-playerstats.html)
>
> **NBA TV 대응**: Info - Box Score, Game Charts

#### Box Score 대응 (포커 통계) `[Core]`
| NBA TV | WSOP TV | 설명 |
|--------|---------|------|
| MIN | Hands | 플레이한 핸드 수 |
| PTS | Chips Won | 획득 칩 |
| FG% | VPIP | Voluntarily Put In Pot % |
| 3P% | PFR | Pre-Flop Raise % |
| AST | 3Bet | 3벳 빈도 |
| REB | WTSD | Went To Showdown % |
| STL | W$SD | Won $ at Showdown % |

#### 시각화 차트
| NBA TV | WSOP TV |
|--------|---------|
| Shot Chart | Position Map (포지션별 승률) |
| Lead Tracker | Stack Tracker (스택 변화 그래프) |
| Team Comparison | Player Comparison |

### 2.5 Hand History (Play-By-Play) `[Core]`

![Hand History](../images/mockups/wsoptv/09-info-handhistory.png)

> **목업 파일**: [`09-info-handhistory.html`](../mockups/wsoptv/09-info-handhistory.html)
>
> **NBA TV 대응**: Info - Play-By-Play

| 요소 | 설명 | NBA TV |
|------|------|--------|
| Level 필터 | Level 1, 2, 3... ALL | Q1~Q4, ALL 대응 |
| 타임라인 | 양 팀 대신 양 플레이어 액션 | ✅ 동일 구조 |
| 액션 타입 | RAISE, CALL, FOLD, ALL-IN, CHECK | 득점/파울 등 대응 |
| 점수 | Pot Size, Stack 변화 | Score 대응 |

---

## 3. UI 컴포넌트 상세

### 3.1 메인 플레이어 `[Core]`

![메인 스트리밍 UI](../images/mockups/wsoptv/01-main-streaming.png)

> **목업 파일**: [`01-main-streaming.html`](../mockups/wsoptv/01-main-streaming.html)

**7단 레이아웃:**
| 레이어 | 컴포넌트 | 설명 |
|:------:|----------|------|
| ① | Tournament Ticker | 날짜, Level, Table 정보, WSOP+ 태그 |
| ② | Ad Banner | 스폰서 광고 |
| ③ | Tournament Header | 이벤트명, 플레이어 수, Prize Pool |
| ④ | Video Player | POT/BOARD 오버레이, 플레이어 HUD |
| ⑤ | Stream Tabs | Active Tables, MultiView, Featured Hands |
| ⑥ | Timeline | Level 시간, 프로그레스 바, LIVE 라벨 |
| ⑦ | Controls | 재생, 볼륨, 자막, 설정, PiP, 전체화면 |

### 3.2 컨트롤 바 `[Core]`

![Player Controls](../images/mockups/wsoptv/13-player-controls.png)

> **목업 파일**: [`13-player-controls.html`](../mockups/wsoptv/13-player-controls.html)
>
> **NBA TV 대응**: Player Controls (툴팁 + 단축키)

#### Core 컨트롤 (NBA TV 동일)
| 컨트롤 | 아이콘 | 기능 | 단축키 |
|--------|--------|------|--------|
| Play/Pause | `\|\|` / `▶` | 재생/일시정지 | Space |
| Rewind | `<<` | 10초 되감기 | ← |
| Forward | `>>` | 10초 앞으로 | → |
| Volume | `[)]` | 볼륨 조절 | - |
| CC | `CC` | 자막 | c |
| MultiView | `⊞` | 멀티뷰 | Shift+m |
| PIP | `[P]` | Picture-in-Picture | p |
| Fullscreen | `[F]` | 전체화면 | f |
| Live | `LIVE` | 라이브로 이동 | Shift+→ |

#### Extension 컨트롤 (포커 전용)
| 컨트롤 | 아이콘 | 기능 | 비고 |
|--------|--------|------|------|
| **[CARDS]** | 🂠 | 홀카드 표시 토글 | NBA TV 없음 |
| **[STACK]** | 💰 | 스택 오버레이 토글 | NBA TV 없음 |
| **[EQUITY]** | 📊 | 에퀴티 미터 토글 | NBA TV 없음 |
| **[CAM]** | 📷 | 카메라 전환 | Settings 확장 |

### 3.3 스트리밍 옵션 `[Core]`

![Streaming Options - Camera](../images/mockups/wsoptv/02-streaming-options-camera.png)

> **목업 파일**: [`02-streaming-options-camera.html`](../mockups/wsoptv/02-streaming-options-camera.html)
>
> **NBA TV 대응**: Streaming Options (2탭 모달)

#### Camera 탭 (Broadcasts 대응) `[Core]`
| 옵션 | 설명 |
|------|------|
| Main Table | 메인 테이블 뷰 |
| Rail Cam | 레일(관중석) 카메라 |
| Hole Cards Cam | 홀카드 전용 카메라 |
| Dealer Cam | 딜러 시점 |
| Player Cam | 특정 플레이어 포커스 |

#### Commentary 탭 (Audio 대응) `[Core]`

![Streaming Options - Commentary](../images/mockups/wsoptv/03-streaming-options-commentary.png)

> **목업 파일**: [`03-streaming-options-commentary.html`](../mockups/wsoptv/03-streaming-options-commentary.html)

| 옵션 | 설명 | NBA TV |
|------|------|--------|
| English | 영어 해설 | Bulls Radio 대응 |
| Spanish | 스페인어 해설 | Spanish 대응 |
| Portuguese | 포르투갈어 해설 | - |
| No Commentary | 테이블 사운드만 | - |

### 3.4 오버레이 시스템 `[Extension]`

> **주의**: 포커 오버레이는 NBA TV의 단순 Score 표시와 다름. Extension으로 분류.

| 오버레이 | 설명 |
|----------|------|
| POT Display | `[POT: $X,XXX,XXX]` |
| Community Cards | `[BOARD: A♠ K♥ 7♦ 2♣ __]` |
| Player HUD | 이름, 스택, 홀카드 표시 |
| Hole Cards | 30분 딜레이 후 공개 |

---

## 4. 확장 기능 (Extension)

> **주의**: 이 섹션의 기능들은 NBA TV에 없는 **포커 도메인 특화 기능**입니다.
> Core 기능 구현 완료 후 Phase 2 이상에서 추가합니다.

### 4.1 Hole Cards Display `[Extension]`
- **30분 딜레이**: 보안을 위해 홀카드는 30분 지연 표시
- **토글**: [CARDS] 버튼으로 ON/OFF
- **RFID 연동**: 테이블 RFID 리더 데이터 실시간 수신

> NBA TV에는 없는 기능. 포커 방송의 핵심 차별점으로 Phase 2에서 추가.

### 4.2 POT/BOARD 오버레이 `[Extension]`
| 요소 | 표시 형식 |
|------|----------|
| POT | `[POT: $2,450,000]` |
| Side Pots | `[MAIN: $1M] [SIDE: $500K]` |
| BOARD | `[BOARD: A♠ K♥ 7♦ __ __]` |
| Action | `[RAISE $150,000]` |

> NBA TV의 Score 오버레이에 대응하나, 포커 특화 형식.

### 4.3 Equity Calculator `[Extension]`

| 요소 | 표시 형식 |
|------|----------|
| Player 1 | `Daniel Negreanu [A♠K♥]: 78.5%` |
| Player 2 | `Phil Ivey [Q♣Q♦]: 21.5%` |
| OUTS | `Q (2장) = 4.5%` |

> NBA TV에 없는 기능. 실시간 승률 계산은 포커 방송 특화 기능.

### 4.4 Hand Range Display `[Extension]`
- 플레이어의 예상 핸드 범위 시각화
- 프리플랍/포스트플랍 레인지 표시

> NBA TV에 없는 기능. 고급 분석 기능으로 Phase 3에서 추가.

### 4.5 Street Timeline `[Extension]`

| Street | 설명 |
|--------|------|
| PREFLOP | 프리플랍 베팅 라운드 |
| FLOP | 플랍 (커뮤니티 카드 3장) |
| TURN | 턴 (커뮤니티 카드 4장) |
| RIVER | 리버 (커뮤니티 카드 5장) |
| SHOWDOWN | 쇼다운 |

> NBA TV의 Quarter 기반 타임라인과 다른 구조.
> Core에서는 Level 기반 타임라인 사용, Street 타임라인은 Extension.

---

## 5. 기술 요구사항

### 5.1 스트리밍 프로토콜
| 항목 | 스펙 |
|------|------|
| 프로토콜 | HLS, DASH |
| 화질 | 1080p (기본), 4K (프리미엄) |
| 비트레이트 | 3-15 Mbps 어댑티브 |
| 지연 | 30초 (라이브), 30분 (홀카드) |

### 5.2 지연 시간 관리

| 소스 | 지연 | 출력 |
|------|------|------|
| 실시간 테이블 영상 | 30초 | Main Stream |
| RFID 홀카드 데이터 | 30분 | Hole Cards Overlay |

### 5.3 다국어 지원
| 언어 | 해설 | UI |
|------|------|-----|
| English | ✅ | ✅ |
| Spanish | ✅ | ✅ |
| Portuguese | ✅ | ✅ |
| Korean | ✅ | ✅ |
| Japanese | ✅ | ✅ |
| Chinese | ✅ | ✅ |

---

## 6. 와이어프레임

> **전체 목업 파일**: `docs/mockups/wsoptv/` (13개 HTML)
> **스크린샷**: `docs/images/mockups/wsoptv/` (13개 PNG)

### 6.1 메인 스트리밍 UI
Tournament Ticker, Ad Banner, Header, Video Player, Stream Tabs, Timeline, Controls 7단 레이아웃

![Main Streaming UI](../images/mockups/wsoptv/01-main-streaming.png)

- **HTML**: [`01-main-streaming.html`](../mockups/wsoptv/01-main-streaming.html)
- **특징**: POT/BOARD 오버레이, 9인 플레이어 HUD, 홀카드 표시

### 6.2 스트리밍 옵션 - Camera
카메라 앵글 선택 모달 (Main Table, Rail Cam, Hole Cards Cam 등)

![Streaming Options - Camera](../images/mockups/wsoptv/02-streaming-options-camera.png)

- **HTML**: [`02-streaming-options-camera.html`](../mockups/wsoptv/02-streaming-options-camera.html)
- **특징**: Hole Cards Cam에 30분 딜레이 배지

### 6.3 스트리밍 옵션 - Commentary
다국어 해설 선택 모달 (English, Spanish, Portuguese, Korean, German)

![Streaming Options - Commentary](../images/mockups/wsoptv/03-streaming-options-commentary.png)

- **HTML**: [`03-streaming-options-commentary.html`](../mockups/wsoptv/03-streaming-options-commentary.html)
- **특징**: Table Sound Only, Background Music Mix 옵션

### 6.4 MultiView Selector
레이아웃 선택 컴포넌트 (1x1, 1:2, 2x2, 3x3)

![MultiView Selector](../images/mockups/wsoptv/04-multiview-selector.png)

- **HTML**: [`04-multiview-selector.html`](../mockups/wsoptv/04-multiview-selector.html)
- **특징**: WSOP 전용 3x3 레이아웃 추가

### 6.5 MultiView 2x2
4개 테이블 동시 시청 레이아웃

![MultiView 2x2](../images/mockups/wsoptv/05-multiview-2x2.png)

- **HTML**: [`05-multiview-2x2.html`](../mockups/wsoptv/05-multiview-2x2.html)
- **특징**: 미니 POT/Blinds 오버레이, "Catch up with Featured Hands" 버튼

### 6.6 MultiView 1:2
메인 + 사이드 2개 테이블 분할 레이아웃

![MultiView 1:2](../images/mockups/wsoptv/12-multiview-1x2.png)

- **HTML**: [`12-multiview-1x2.html`](../mockups/wsoptv/12-multiview-1x2.html)
- **특징**: 메인 테이블 강조, 사이드 테이블 축소

### 6.7 Info - Summary Tab
토너먼트 요약 페이지 (기사 + Chip Counts + Stats)

![Info Summary](../images/mockups/wsoptv/06-info-summary.png)

- **HTML**: [`06-info-summary.html`](../mockups/wsoptv/06-info-summary.html)
- **특징**: 7:3 레이아웃, Chip Counts 테이블, BB 표시

### 6.8 Info - Player Stats Tab
플레이어별 상세 통계 (VPIP, PFR, 3BET, AF 등)

![Info Player Stats](../images/mockups/wsoptv/07-info-playerstats.png)

- **HTML**: [`07-info-playerstats.html`](../mockups/wsoptv/07-info-playerstats.html)
- **특징**: 15개 통계 컬럼, All Stats/Preflop/Postflop/All-ins 필터

### 6.9 Info - Hand Charts Tab
Stack Tracker, Position Win Rate Map, Equity Graph, Player Comparison

![Info Hand Charts](../images/mockups/wsoptv/08-info-handcharts.png)

- **HTML**: [`08-info-handcharts.html`](../mockups/wsoptv/08-info-handcharts.html)
- **특징**: 4개 차트 그리드 레이아웃

### 6.10 Info - Hand History Tab
레벨별 핸드 타임라인 (Street별 액션, Equity, Showdown)

![Info Hand History](../images/mockups/wsoptv/09-info-handhistory.png)

- **HTML**: [`09-info-handhistory.html`](../mockups/wsoptv/09-info-handhistory.html)
- **특징**: 핸드 목록 사이드바 + 상세 액션 타임라인

### 6.11 Featured Hands Modal
주요 핸드 목록 모달 (All-In, Big Pots, Bluffs, Eliminations 필터)

![Featured Hands Modal](../images/mockups/wsoptv/10-modal-featuredhands.png)

- **HTML**: [`10-modal-featuredhands.html`](../mockups/wsoptv/10-modal-featuredhands.html)
- **특징**: 썸네일 + 핸드 설명, Jump to Live 버튼

### 6.12 Featured Hands Player
핸드 재생 전용 플레이어 (Street별 이동, Equity 표시)

![Featured Hands Player](../images/mockups/wsoptv/11-featuredhands-player.png)

- **HTML**: [`11-featuredhands-player.html`](../mockups/wsoptv/11-featuredhands-player.html)
- **특징**: Street 마커 타임라인, Prev/Next/Jump to Live 네비게이션

### 6.13 Player Controls
컨트롤 바 컴포넌트 상세 (Stream Tabs, Tooltips, WSOP 전용 오버레이)

![Player Controls](../images/mockups/wsoptv/13-player-controls.png)

- **HTML**: [`13-player-controls.html`](../mockups/wsoptv/13-player-controls.html)
- **특징**: WSOP 전용 컨트롤 (Hole Cards, Stack Display, Equity Meter, Hand Range, Switch Cam)

---

## 7. 용어 매핑 (NBA → WSOP)

| NBA TV | WSOP TV | 설명 |
|--------|---------|------|
| Game | Tournament/Table | 경기 단위 |
| Team | Player/Table | 참가 주체 |
| Score | Stack/Chips | 점수 체계 |
| Quarter | Level | 시간 구분 |
| Game Clock | Blinds Timer | 타이머 |
| League Pass | Featured Table | 프리미엄 콘텐츠 |
| Key Plays | Featured Hands | 하이라이트 |
| Box Score | Player Stats | 통계 |
| Play-By-Play | Hand History | 상세 기록 |
| Shot Chart | Position Map | 시각화 |
| Lead Tracker | Stack Tracker | 추이 그래프 |

---

## 8. 구현 우선순위

> **원칙**: Core 기능 완료 후 Extension 기능 추가

### Phase 1: Core MVP (NBA TV 1:1)
| 기능 | NBA TV 대응 | 상태 |
|------|-------------|------|
| 라이브 스트리밍 플레이어 | Video Player | [ ] |
| Tournament Ticker | Scoreboard Ticker | [ ] |
| 기본 컨트롤 바 | Player Controls | [ ] |
| Stream Tabs (Active Tables) | Stream Tabs (Streams) | [ ] |
| Timeline (Level 기반) | Timeline (Quarter 기반) | [ ] |

### Phase 2: Core 확장 (NBA TV 1:1)
| 기능 | NBA TV 대응 | 상태 |
|------|-------------|------|
| MultiView (1x1, 1:2, 2x2) | MultiView (3종) | [ ] |
| Featured Hands 모달 | Key Plays 모달 | [ ] |
| Featured Hands 플레이어 | Key Plays 플레이어 | [ ] |
| Streaming Options (Camera) | Streaming Options (Broadcasts) | [ ] |
| Streaming Options (Commentary) | Streaming Options (Audio) | [ ] |

### Phase 3: Core 완성 (NBA TV 1:1)
| 기능 | NBA TV 대응 | 상태 |
|------|-------------|------|
| Info - Summary | Info - Summary | [ ] |
| Info - Player Stats | Info - Box Score | [ ] |
| Info - Hand Charts | Info - Game Charts | [ ] |
| Info - Hand History | Info - Play-By-Play | [ ] |

### Phase 4: Extension (포커 특화)
| 기능 | NBA TV 대응 | 상태 |
|------|-------------|------|
| Hole Cards Display (30분 딜레이) | ❌ 없음 | [ ] |
| POT/BOARD 오버레이 | Score 오버레이 확장 | [ ] |
| 3x3 MultiView | ❌ 없음 | [ ] |

### Phase 5: Extension 고급 (포커 특화)
| 기능 | NBA TV 대응 | 상태 |
|------|-------------|------|
| Equity Calculator | ❌ 없음 | [ ] |
| Hand Range Display | ❌ 없음 | [ ] |
| Street Timeline | ❌ 없음 | [ ] |

---

## 부록 A: 와이어프레임 인덱스

| # | 화면 | HTML | PNG | NBA TV 대응 |
|---|------|------|-----|------------|
| 01 | 메인 스트리밍 | [HTML](../mockups/wsoptv/01-main-streaming.html) | [PNG](../images/mockups/wsoptv/01-main-streaming.png) | Main Streaming |
| 02 | 카메라 선택 | [HTML](../mockups/wsoptv/02-streaming-options-camera.html) | [PNG](../images/mockups/wsoptv/02-streaming-options-camera.png) | Broadcasts |
| 03 | 해설 선택 | [HTML](../mockups/wsoptv/03-streaming-options-commentary.html) | [PNG](../images/mockups/wsoptv/03-streaming-options-commentary.png) | Audio |
| 04 | 레이아웃 선택 | [HTML](../mockups/wsoptv/04-multiview-selector.html) | [PNG](../images/mockups/wsoptv/04-multiview-selector.png) | MultiView Selector |
| 05 | 멀티뷰 2x2 | [HTML](../mockups/wsoptv/05-multiview-2x2.html) | [PNG](../images/mockups/wsoptv/05-multiview-2x2.png) | MultiView 2x2 |
| 06 | 토너먼트 요약 | [HTML](../mockups/wsoptv/06-info-summary.html) | [PNG](../images/mockups/wsoptv/06-info-summary.png) | Summary |
| 07 | 플레이어 통계 | [HTML](../mockups/wsoptv/07-info-playerstats.html) | [PNG](../images/mockups/wsoptv/07-info-playerstats.png) | Box Score |
| 08 | 핸드 차트 | [HTML](../mockups/wsoptv/08-info-handcharts.html) | [PNG](../images/mockups/wsoptv/08-info-handcharts.png) | Game Charts |
| 09 | 핸드 히스토리 | [HTML](../mockups/wsoptv/09-info-handhistory.html) | [PNG](../images/mockups/wsoptv/09-info-handhistory.png) | Play-By-Play |
| 10 | Featured Hands 목록 | [HTML](../mockups/wsoptv/10-modal-featuredhands.html) | [PNG](../images/mockups/wsoptv/10-modal-featuredhands.png) | Key Plays |
| 11 | Featured Hands 플레이어 | [HTML](../mockups/wsoptv/11-featuredhands-player.html) | [PNG](../images/mockups/wsoptv/11-featuredhands-player.png) | Key Plays Player |
| 12 | 멀티뷰 1:2 | [HTML](../mockups/wsoptv/12-multiview-1x2.html) | [PNG](../images/mockups/wsoptv/12-multiview-1x2.png) | MultiView 1:2 |
| 13 | 컨트롤 바 | [HTML](../mockups/wsoptv/13-player-controls.html) | [PNG](../images/mockups/wsoptv/13-player-controls.png) | Player Controls |

---

## 부록 B: NBA TV 레퍼런스

### B.1 원본 스크린샷 및 기능 분석 (26개)

> NBA TV League Pass의 실제 스크린샷과 각 기능 분석

#### B.1.1 메인 스트리밍 UI (#1)

![메인 스트리밍](스크린샷%202026-01-21%20113524.png)

| 구성 요소 | 기능 | WSOP TV 대응 |
|----------|------|-------------|
| Scoreboard Ticker | 실시간 경기 현황 (팀, 점수, 상태) | Tournament Ticker |
| Ad Banner | 스폰서 광고 | 동일 |
| Game Header | AWAY @ HOME, 방송 타입 | Tournament Header |
| Video Player | 16:9 라이브 스트리밍 | 동일 |
| Stream Tabs | Streams, MultiView, Key Plays | Active Tables, MultiView, Featured Hands |
| Timeline | 경과 시간 + LIVE 라벨 | Level 시간 + LIVE |
| Controls | 재생, 볼륨, CC, PiP, 전체화면 | 동일 |

#### B.1.2 Streaming Options - Broadcasts (#2)

![Broadcasts 옵션](스크린샷%202026-01-21%20113700.png)

| 기능 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| Bulls (In-Arena) | 홈팀 경기장 방송 | Main Table Cam |
| Clippers (In-Arena) | 원정팀 경기장 방송 | Rail Cam |
| Bulls (Studio Show) | 홈팀 스튜디오 방송 | Dealer Cam |
| Clippers (Studio Show) | 원정팀 스튜디오 방송 | Player Focus Cam |
| Mobile View | 모바일 최적화 뷰 | Arena Overview Cam |

#### B.1.3 Streaming Options - Audio (#3)

![Audio 옵션](스크린샷%202026-01-21%20113717.png)

| 기능 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| Bulls Radio | 홈팀 라디오 (영어) | English Commentary |
| Clippers Radio | 원정팀 라디오 (영어) | Spanish Commentary |
| Spanish | 스페인어 버전 | Portuguese/Korean |

#### B.1.4 MultiView Selector (#4)

![MultiView 선택기](스크린샷%202026-01-21%20113734.png)

| 레이아웃 | 설명 | WSOP TV 대응 |
|----------|------|-------------|
| 1x1 | 단일 화면 | ✅ 동일 |
| 1:2 | 메인+사이드 | ✅ 동일 |
| 2x2 | 4분할 | ✅ 동일 |

#### B.1.5 MultiView 1:2 (#5)

![MultiView 1:2](스크린샷%202026-01-21%20113750.png)

| 요소 | 기능 | WSOP TV 대응 |
|------|------|-------------|
| 메인 영역 (2/3) | 현재 시청 경기 | 메인 테이블 |
| 사이드 영역 (1/3) | 빈 슬롯/추가 경기 | 추가 테이블 |
| "Catch up with Key Plays" | 놓친 하이라이트 | "Catch up with Featured Hands" |

#### B.1.6 Add to MultiView (#6)

![Add to MultiView](스크린샷%202026-01-21%20113755.png)

- Ticker에서 경기 카드에 "Add to Multiview" 버튼 표시
- 클릭 시 빈 슬롯에 경기 추가

#### B.1.7 MultiView 2x2 (#7)

![MultiView 2x2](스크린샷%202026-01-21%20113825.png)

| 슬롯 | 내용 |
|------|------|
| 좌상단 | 현재 경기 |
| 나머지 3개 | "Add a Game from Score Strip" |

#### B.1.8 MultiView 2x2 Ticker 인터랙션 (#8)

![MultiView Ticker](스크린샷%202026-01-21%20113835.png)

- Ticker 호버 시 "Add to Multiview" 버튼 표시
- 클릭으로 빈 슬롯에 추가

#### B.1.9-14 컨트롤 바 툴팁 (#9-14)

![Streams 툴팁](스크린샷%202026-01-21%20113855.png)
![MultiView 툴팁](스크린샷%202026-01-21%20113907.png)
![CC 툴팁](스크린샷%202026-01-21%20113916.png)
![Settings 툴팁](스크린샷%202026-01-21%20113926.png)
![PiP 툴팁](스크린샷%202026-01-21%20113935.png)
![Live 툴팁](스크린샷%202026-01-21%20113949.png)

| 버튼 | 툴팁 | 단축키 |
|------|------|--------|
| Streams | "Stream Selector" | - |
| MultiView | "multiview" | Shift+m |
| CC | "Subtitles/closed captions" | c |
| Settings | "Settings" | - |
| PiP | "Picture in Picture" | p |
| Live | "Live" | SHIFT+→ |

#### B.1.15-16 Stream Tabs & Layout (#15-16)

![Stream Tabs](스크린샷%202026-01-21%20114101.png)
![Layout Selector](스크린샷%202026-01-21%20114114.png)

- Stream Tabs: Streams (숫자 배지), MultiView, Key Plays
- Layout Selector: 1x1, 1:2, 2x2 + LIVE 라벨

#### B.1.17 Info - Summary (#17)

![Info Summary](스크린샷%202026-01-21%20114505.png)

| 영역 | 비율 | 내용 | WSOP TV 대응 |
|------|------|------|-------------|
| 좌측 | 70% | 기사 본문 | 토너먼트 기사 |
| 우측 | 30% | Game Info + Line Scores | Tournament Info + Chip Counts |

#### B.1.18 Info - Box Score (#18)

![Info Box Score](스크린샷%202026-01-21%20114529.png)

| 컬럼 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| MIN | 출전 시간 | HANDS |
| PTS | 득점 | CHIPS WON |
| FG% | 필드골 % | WIN% |
| +/- | Plus/Minus | +/- |

#### B.1.19 Info - Shot Charts (#19)

![Shot Charts](스크린샷%202026-01-21%20114548.png)

| 요소 | 기능 | WSOP TV 대응 |
|------|------|-------------|
| 코트 다이어그램 | ○ Made, × Miss | Position Win Rate Map |
| 플레이어 필터 | 개별 선수 선택 | 플레이어 필터 |
| FG% 표시 | 성공률 통계 | WIN% |

#### B.1.20 Info - Lead Tracker (#20)

![Lead Tracker](스크린샷%202026-01-21%20114600.png)

| 요소 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| X축 | Q1~Q4 | Level 구간 |
| Y축 | 점수 차이 | 칩 변동 |
| 영역 차트 | 리드 시각화 | Stack Tracker |

#### B.1.21 Info - Leading Players (#21)

![Leading Players](스크린샷%202026-01-21%20114611.png)

| 차트 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| 방사형 차트 | 4축 (BLK, PTS, REB, AST) | 4축 (VPIP, PFR, 3BET, AF) |
| Team Comparison | 바 차트 9개 통계 | Player Comparison |

#### B.1.22 Info - Play-By-Play (#22)

![Play-By-Play](스크린샷%202026-01-21%20114928.png)

| 요소 | 설명 | WSOP TV 대응 |
|------|------|-------------|
| Quarter 탭 | Q1~Q4, ALL | Level 탭 |
| 양 팀 열 | 이벤트 타임라인 | 플레이어 액션 |
| 이벤트 타입 | FOUL, STEAL, 득점 등 | RAISE, CALL, FOLD 등 |

#### B.1.23-25 Key Plays (#23-25)

![Key Plays 모달](스크린샷%202026-01-21%20114955.png)
![Key Plays 툴팁](스크린샷%202026-01-21%20115018.png)
![Key Plays 플레이어](스크린샷%202026-01-21%20115031.png)

| 요소 | 기능 | WSOP TV 대응 |
|------|------|-------------|
| 썸네일 | 플레이 미리보기 | 핸드 썸네일 |
| 시간 표시 | "Q1 • 00:49.5" | "Level 38 • Hand #245" |
| Next 버튼 | 다음 하이라이트 | 다음 Featured Hand |
| Jump to Live | 라이브로 이동 | ✅ 동일 |

### B.2 NBA TV B&W 목업 (13개)

| # | 화면 | HTML | PNG |
|---|------|------|-----|
| 01 | 메인 스트리밍 | [HTML](../mockups/nbatv/01-main-streaming.html) | [PNG](../images/mockups/nbatv/01-main-streaming.png) |
| 02 | Broadcasts 옵션 | [HTML](../mockups/nbatv/02-streaming-options-broadcasts.html) | [PNG](../images/mockups/nbatv/02-streaming-options-broadcasts.png) |
| 03 | Audio 옵션 | [HTML](../mockups/nbatv/03-streaming-options-audio.html) | [PNG](../images/mockups/nbatv/03-streaming-options-audio.png) |
| 04 | MultiView 선택 | [HTML](../mockups/nbatv/04-multiview-selector.html) | [PNG](../images/mockups/nbatv/04-multiview-selector.png) |
| 05 | MultiView 1:2 | [HTML](../mockups/nbatv/05-multiview-1x2.html) | [PNG](../images/mockups/nbatv/05-multiview-1x2.png) |
| 06 | MultiView 2x2 | [HTML](../mockups/nbatv/06-multiview-2x2.html) | [PNG](../images/mockups/nbatv/06-multiview-2x2.png) |
| 07 | 컨트롤 바 | [HTML](../mockups/nbatv/07-player-controls.html) | [PNG](../images/mockups/nbatv/07-player-controls.png) |
| 08 | Summary | [HTML](../mockups/nbatv/08-info-summary.html) | [PNG](../images/mockups/nbatv/08-info-summary.png) |
| 09 | Box Score | [HTML](../mockups/nbatv/09-info-boxscore.html) | [PNG](../images/mockups/nbatv/09-info-boxscore.png) |
| 10 | Game Charts | [HTML](../mockups/nbatv/10-info-gamecharts.html) | [PNG](../images/mockups/nbatv/10-info-gamecharts.png) |
| 11 | Play-By-Play | [HTML](../mockups/nbatv/11-info-playbyplay.html) | [PNG](../images/mockups/nbatv/11-info-playbyplay.png) |
| 12 | Key Plays 목록 | [HTML](../mockups/nbatv/12-modal-keyplays.html) | [PNG](../images/mockups/nbatv/12-modal-keyplays.png) |
| 13 | Key Plays 플레이어 | [HTML](../mockups/nbatv/13-keyplays-player.html) | [PNG](../images/mockups/nbatv/13-keyplays-player.png) |

### B.3 정밀 분석 문서
- [`NBATV-SCREENSHOT-ANALYSIS.md`](./NBATV-SCREENSHOT-ANALYSIS.md) - NBA TV 26개 스크린샷 상세 분석
