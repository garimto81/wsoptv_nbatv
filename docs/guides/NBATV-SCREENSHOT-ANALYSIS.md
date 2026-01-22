# NBA TV 스크린샷 기능 분석

**Version**: 2.0.0
**Date**: 2026-01-21
**Purpose**: WSOP TV 1:1 복제를 위한 NBA TV UI 정밀 분석

---

## 개요

| 항목 | 값 |
|------|-----|
| 총 스크린샷 | 26개 |
| 유효 스크린샷 | 25개 |
| 무관 스크린샷 | 1개 (#26) |
| 분석 대상 | NBA TV League Pass 웹 UI |
| HTML 목업 | 13개 |
| PNG 스크린샷 | 13개 |

---

## 목업 인덱스

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

---

## 스크린샷 인덱스

| # | 파일명 | 기능 | 상세 |
|---|--------|------|------|
| 1 | 113524 | 메인 스트리밍 | 전체 UI: Ticker, Ad, Header, Video, Tabs, Timeline, Controls |
| 2 | 113700 | Streaming Options - Broadcasts | 5개 방송 소스 선택 (In-Arena, Studio, Mobile) |
| 3 | 113717 | Streaming Options - Audio | 4개 오디오 선택 (Radio, Spanish) |
| 4 | 113734 | MultiView Selector | 3개 레이아웃 버튼 (1x1, 1:2, 2x2) |
| 5 | 113750 | MultiView 1:2 | 메인+사이드, "Catch up with Key Plays" |
| 6 | 113755 | MultiView - Add to | Ticker의 "Add to Multiview" 버튼 |
| 7 | 113825 | MultiView 2x2 | 4분할, "Add a Game from Score Strip" |
| 8 | 113835 | MultiView 2x2 추가 | Ticker 인터랙션 |
| 9 | 113855 | 툴팁 - Stream Selector | Streams 버튼 툴팁 |
| 10 | 113907 | 툴팁 - MultiView | "multiview (Shift+m)" |
| 11 | 113916 | 툴팁 - CC | "Subtitles/closed captions (c)" |
| 12 | 113926 | 툴팁 - Settings | 설정 버튼 |
| 13 | 113935 | 툴팁 - PiP | "Picture in Picture (p)" |
| 14 | 113949 | 툴팁 - Live | "Live (SHIFT+→)" |
| 15 | 114101 | Stream Tabs 확장 | Streams, MultiView, Key Plays 탭 |
| 16 | 114114 | 레이아웃 선택기 | 컨트롤 바 내 레이아웃 버튼 |
| 17 | 114505 | Info - Summary | 기사(70%) + Game Info(30%) + Line Scores |
| 18 | 114529 | Info - Box Score | 선수별 20컬럼 통계 테이블 |
| 19 | 114548 | Info - Shot Charts | 양 팀 코트 다이어그램, 플레이어 필터 |
| 20 | 114600 | Info - Lead Tracker | 점수 차이 추이 그래프 (Q1~Q4) |
| 21 | 114611 | Info - Leading Players | 방사형 차트 + Team Comparison 바 차트 |
| 22 | 114928 | Info - Play-By-Play | Quarter 탭, 양 팀 이벤트 타임라인 |
| 23 | 114955 | Key Plays 모달 | 썸네일 + 설명 + "Q1 • 00:49.5" |
| 24 | 115018 | Key Plays 툴팁 | "key highlights" |
| 25 | 115031 | Key Plays 플레이어 | Next, Jump to Live 버튼 |
| 26 | 145658 | (관련 없음) | 주문 완료 메시지 |

---

## 1. 메인 스트리밍 화면 (#1)

### 1.1 7단 레이아웃 구조

![메인 스트리밍 UI](../images/mockups/nbatv/01-main-streaming.png)

> **목업 파일**: [`01-main-streaming.html`](../mockups/nbatv/01-main-streaming.html)

| 레이어 | 컴포넌트 | 설명 |
|:------:|----------|------|
| ① | Scoreboard Ticker | 날짜, 경기 상태, 팀 정보, 구독 태그 |
| ② | Ad Banner | 상품 이미지, 광고 텍스트, CTA 버튼 |
| ③ | Game Header | 경기명 (AWAY @ HOME), 방송 타입 |
| ④ | Video Player | 16:9 비율 라이브 스트리밍 |
| ⑤ | Stream Tabs | Streams, MultiView, Key Plays |
| ⑥ | Timeline | 현재 시간, 프로그레스 바, LIVE 라벨 |
| ⑦ | Controls | 재생, 볼륨, 자막, 설정, PiP, 전체화면 |

### 1.2 컴포넌트 상세

#### ① Scoreboard Ticker
| 요소 | 내용 | 예시 |
|------|------|------|
| 날짜 | 요일 + 월/일 | TUE JAN 20 |
| 경기 상태 | Quarter + 시간 또는 상태 | Q3 3:05, HALF, PREGAME, FINAL |
| 팀 정보 | 로고 + 팀명 + 점수 | Clippers 77 / Bulls 90 |
| 구독 태그 | 시청 가능 서비스 | League Pass, Coupang Play |
| 스크롤 | 좌우 화살표 | → |

#### ② Ad Banner
| 요소 | 위치 | 크기 |
|------|------|------|
| 상품 이미지 | 좌측 | ~150px |
| 광고 텍스트 | 중앙 | flex |
| CTA 버튼 | 중앙-우측 | ~100px, 빨간 배경 |
| 프로모션 배너 | 우측 | ~150px |

#### ③ Game Header
| 요소 | 내용 |
|------|------|
| 경기명 | "CLIPPERS @ BULLS" (AWAY @ HOME 형식) |
| 방송 타입 | "Bulls (In-Arena)" + 정보 아이콘 ⓘ |

#### ④ Video Player
- 비율: 16:9
- 라이브 스트리밍 영상

#### ⑤ Stream Tabs
| 탭 | 아이콘 | 내용 |
|-----|--------|------|
| Streams | 📡 | 숫자 배지 (예: 9) |
| MultiView | ⊞ | 멀티뷰 모드 |
| Key Plays | 🔥 | 하이라이트 |

#### ⑥ Timeline
| 요소 | 내용 |
|------|------|
| 현재 시간 | 01:35:55 형식 |
| 프로그레스 바 | 빨간색 진행 바 |
| LIVE 라벨 | 우측 끝 |

#### ⑦ Controls
| 위치 | 버튼 |
|------|------|
| 좌측 | ⏸ 일시정지, ⏪10 10초 뒤로, ⏮ 처음으로, ⏭ 끝으로, ⏩10 10초 앞으로, 🔊 볼륨 슬라이더 |
| 우측 | ⊞ MultiView, CC 자막, ⚙ 설정, ⧉ PiP, 🖵 전체화면 |

---

## 2. Streaming Options 모달 (#2-3)

### 2.1 Broadcasts 탭 (#2)

![Streaming Options - Broadcasts](../images/mockups/nbatv/02-streaming-options-broadcasts.png)

> **목업 파일**: [`02-streaming-options-broadcasts.html`](../mockups/nbatv/02-streaming-options-broadcasts.html)

| 옵션 | 설명 |
|------|------|
| Bulls (In-Arena) | 홈팀 경기장 방송 |
| Clippers (In-Arena) | 원정팀 경기장 방송 |
| Bulls (Studio Show) | 홈팀 스튜디오 방송 |
| Clippers (Studio Show) | 원정팀 스튜디오 방송 |
| Mobile View | 모바일 최적화 뷰 |

### 2.2 Audio 탭 (#3)

![Streaming Options - Audio](../images/mockups/nbatv/03-streaming-options-audio.png)

> **목업 파일**: [`03-streaming-options-audio.html`](../mockups/nbatv/03-streaming-options-audio.html)

| 옵션 | 설명 |
|------|------|
| Bulls Radio | 홈팀 라디오 방송 (영어) |
| Clippers Radio | 원정팀 라디오 방송 (영어) |
| Bulls Radio - Spanish | 홈팀 라디오 (스페인어) |
| Clippers Radio - Spanish | 원정팀 라디오 (스페인어) |

---

## 3. MultiView (#4-8)

### 3.1 레이아웃 선택기 (#4)

![MultiView Selector](../images/mockups/nbatv/04-multiview-selector.png)

> **목업 파일**: [`04-multiview-selector.html`](../mockups/nbatv/04-multiview-selector.html)

| 레이아웃 | 아이콘 | 설명 |
|----------|--------|------|
| 1x1 | [■] | 단일 화면 |
| 1:2 | [■│□] | 메인(큼) + 사이드(작음) |
| 2x2 | [■■/■■] | 4분할 균등 |

### 3.2 MultiView 1:2 레이아웃 (#5)

![MultiView 1:2](../images/mockups/nbatv/05-multiview-1x2.png)

> **목업 파일**: [`05-multiview-1x2.html`](../mockups/nbatv/05-multiview-1x2.html)

| 요소 | 위치 | 기능 |
|------|------|------|
| 메인 영역 | 좌측 (2/3) | 현재 시청 중인 경기 |
| 사이드 영역 | 우측 (1/3) | 빈 슬롯 또는 추가 경기 |
| "Catch up with Key Plays" | 메인 영역 하단 | 놓친 하이라이트 보기 버튼 |
| "Add a Game from Score Strip" | 빈 슬롯 | 경기 추가 안내 |

### 3.3 Add to Multiview 기능 (#6)

- Scoreboard Ticker의 경기 카드에 "Add to Multiview" 버튼 표시
- 클릭 시 해당 경기를 빈 슬롯에 추가

### 3.4 MultiView 2x2 레이아웃 (#7-8)

![MultiView 2x2](../images/mockups/nbatv/06-multiview-2x2.png)

> **목업 파일**: [`06-multiview-2x2.html`](../mockups/nbatv/06-multiview-2x2.html)

| 영역 | 내용 |
|------|------|
| 좌상단 | 현재 경기 |
| 나머지 3개 | 빈 슬롯 ("Add a Game from Score Strip") |

---

## 4. 컨트롤 바 (#9-16)

![Player Controls](../images/mockups/nbatv/07-player-controls.png)

> **목업 파일**: [`07-player-controls.html`](../mockups/nbatv/07-player-controls.html)

### 4.1 툴팁 목록

| # | 버튼 | 툴팁 텍스트 | 단축키 |
|---|------|-------------|--------|
| 9 | Streams | "Stream Selector" | - |
| 10 | MultiView | "multiview" | Shift+m |
| 11 | CC | "Subtitles/closed captions" | c |
| 12 | Settings | "Settings" | - |
| 13 | PiP | "Picture in Picture" | p |
| 14 | Live | "Live" | SHIFT+→ |

### 4.2 Stream Tabs 구성 (#15)

| 탭 | 아이콘 | 기능 |
|-----|--------|------|
| Streams | 📡 | 방송 소스 선택 (숫자 배지) |
| MultiView | ⊞ | 멀티뷰 모드 전환 |
| Key Plays | 🔥 | 하이라이트 재생 |

### 4.3 레이아웃 선택기 위치 (#16)

- Stream Tabs 우측 또는 컨트롤 바 우측에 배치
- 1x1, 1:2, 2x2 레이아웃 버튼 + LIVE 라벨

---

## 5. Info 탭 (#17-22)

### 5.0 탭 구조

| 탭 | 기능 |
|-----|------|
| Summary | 기사 + Game Info + Line Scores |
| Box Score | 선수별 통계 테이블 |
| Game Charts | Shot Charts, Lead Tracker, Team Comparison |
| Play-By-Play | 양 팀 이벤트 타임라인 |

### 5.1 Summary 탭 (#17)

![Info - Summary](../images/mockups/nbatv/08-info-summary.png)

> **목업 파일**: [`08-info-summary.html`](../mockups/nbatv/08-info-summary.html)

#### 레이아웃 (7:3)

| 영역 | 비율 | 내용 |
|------|:----:|------|
| 좌측 | 70% | 기사 본문 |
| 우측 | 30% | Game Info + Line Scores |

#### Game Info 항목
| 아이콘 | 항목 | 내용 |
|--------|------|------|
| 📅 | 날짜/시간 | Wednesday, 21 January, 2026 10:00 AM |
| 📍 | 장소 | United Center, Chicago, IL |
| 👔 | Officials | Marc Davis, Brent Barnaky, Robert Hussey |
| 📺 | Broadcast | League Pass |
| 🎧 | Radio | - |
| 📄 | Game Book | Gamebook, PDF (다운로드 링크) |

#### Line Scores 테이블
| TEAM | Q1 | Q2 | Q3 | Q4 | Total |
|------|----|----|----|----|-------|
| LAC | 30 | 19 | 30 | 0 | 79 |
| CHI | 25 | 45 | 27 | 0 | 97 |

#### 추가 통계
| 통계 | LAC | CHI |
|------|-----|-----|
| PITP (Points in the Paint) | 42 | 44 |
| FB PTS (Fastbreak Points) | 10 | 27 |
| BIG LD (Biggest Lead) | 8 | 21 |
| BPTS (Bench Points) | 12 | 40 |
| TREB (Total Rebounds) | 5 | 6 |
| TOV (Turnovers) | 12 | 9 |
| TTOV (Team Turnovers) | 0 | 0 |
| POT (Points off Turnovers) | 13 | 10 |

### 5.2 Box Score 탭 (#18)

![Info - Box Score](../images/mockups/nbatv/09-info-boxscore.png)

> **목업 파일**: [`09-info-boxscore.html`](../mockups/nbatv/09-info-boxscore.html)

#### 20개 컬럼 설명
| 컬럼 | 설명 |
|------|------|
| PLAYER | 선수명 + 포지션 (SF, PF, C, SG, PG) |
| MIN | 출전 시간 (mm:ss) |
| FGM | Field Goals Made |
| FGA | Field Goals Attempted |
| FG% | Field Goal Percentage |
| 3PM | 3-Point Field Goals Made |
| 3PA | 3-Point Field Goals Attempted |
| 3P% | 3-Point Percentage |
| FTM | Free Throws Made |
| FTA | Free Throws Attempted |
| FT% | Free Throw Percentage |
| OREB | Offensive Rebounds |
| DREB | Defensive Rebounds |
| REB | Total Rebounds |
| AST | Assists |
| STL | Steals |
| BLK | Blocks |
| TO | Turnovers |
| PF | Personal Fouls |
| PTS | Points |
| +/- | Plus/Minus |

#### 특수 행
- **DNP**: Did Not Play - Coach's Decision
- **TOTALS**: 팀 합계

### 5.3 Game Charts 탭 (#19-21)

![Info - Game Charts](../images/mockups/nbatv/10-info-gamecharts.png)

> **목업 파일**: [`10-info-gamecharts.html`](../mockups/nbatv/10-info-gamecharts.html)

#### Shot Charts (#19)

| 요소 | 기능 |
|------|------|
| Shot Plot 드롭다운 | 차트 유형 선택 |
| Quarter 드롭다운 | Q1, Q2, Q3, Q4, ALL |
| Range Filter | 거리별 필터 |
| 플레이어 체크박스 | 개별 선수 필터 |
| 코트 다이어그램 | ○ Made, × Miss 표시 |
| FG% | 필드골 성공률 (성공/시도) |
| DOWNLOAD | 이미지 다운로드 |

#### Lead Tracker (#20)

| 요소 | 설명 |
|------|------|
| X축 | Q1, Q2, Q3, Q4 |
| Y축 | -25 ~ +25 (LAC 위, CHI 아래) |
| 영역 차트 | 빨간색으로 점수 차이 시각화 |
| Biggest Lead | 양 팀 최대 리드 |
| Times Tied | 동점 횟수 |
| Longest Run | 최장 연속 득점 |
| Lead Changes | 리드 교체 횟수 |

#### Leading Players & Team Comparison (#21)

| 차트 | 설명 |
|------|------|
| Leading Players | 방사형 차트, 4축 (BLK, PTS, REB, AST) |
| Team Comparison | 가로 바 차트, 9개 통계 비교 |
| 추가 통계 | 도넛 차트 (PTS IN PAINT, 2ND CHANCE, FASTBREAK) |

### 5.4 Play-By-Play 탭 (#22)

![Info - Play-By-Play](../images/mockups/nbatv/11-info-playbyplay.png)

> **목업 파일**: [`11-info-playbyplay.html`](../mockups/nbatv/11-info-playbyplay.html)

| 요소 | 설명 |
|------|------|
| Quarter 탭 | Q1, Q2, Q3, Q4, ALL |
| LIVE 배지 | 라이브 경기 표시 |
| Auto Switch Quarter | 자동 쿼터 전환 토글 |
| Latest First | 최신 이벤트 먼저 표시 토글 |
| 좌측 열 | LA Clippers 이벤트 |
| 중앙 열 | 시간 + 점수 |
| 우측 열 | Chicago Bulls 이벤트 |

#### 이벤트 유형
| 유형 | 설명 |
|------|------|
| FOUL | 파울 |
| STEAL | 스틸 |
| TURNOVER | 턴오버 |
| Layup, 3PT, Jump Shot | 득점 |
| REBOUND | 리바운드 |
| SUB In/Out | 선수 교체 |

---

## 6. Key Plays (#23-25)

### 6.1 Key Plays 모달 (#23)

![Key Plays Modal](../images/mockups/nbatv/12-modal-keyplays.png)

> **목업 파일**: [`12-modal-keyplays.html`](../mockups/nbatv/12-modal-keyplays.html)

| 요소 | 설명 |
|------|------|
| 썸네일 | 플레이 미리보기 이미지 |
| 제목 | 플레이 설명 (예: "Huerter running jump shot") |
| 시간 | Quarter • 시간 (예: "Q1 • 00:49.5") |

### 6.2 Key Plays 툴팁 (#24)

| 버튼 | 툴팁 |
|------|------|
| Key Plays (🔥) | "key highlights" |

### 6.3 Key Plays 플레이어 (#25)

![Key Plays Player](../images/mockups/nbatv/13-keyplays-player.png)

> **목업 파일**: [`13-keyplays-player.html`](../mockups/nbatv/13-keyplays-player.html)

| 요소 | 기능 |
|------|------|
| Key Plays 탭 | 활성 상태 표시 |
| 비디오 영역 | 하이라이트 재생 |
| 점수판 오버레이 | 현재 점수 + 쿼터 + 파울 |
| 타임라인 | 00:00:04 / 00:00:08 형식 |
| Next 버튼 | 다음 하이라이트로 이동 |
| Jump to Live 버튼 | 라이브로 즉시 이동 |
| 컨트롤 바 | 기본 비디오 컨트롤 |

---

## WSOP TV 매핑 참조

NBA TV → WSOP TV 1:1 매핑은 `WSOP-TV-PRD.md` 섹션 0을 참조하세요.

### 핵심 매핑 요약

| NBA TV | WSOP TV |
|--------|---------|
| Scoreboard Ticker | Tournament Ticker |
| Q3 3:05 | L38 LIVE |
| Clippers 77 / Bulls 90 | Table 1: 5 Players |
| League Pass | WSOP+ |
| Streams 9 | Active Tables 45 |
| Key Plays | Featured Hands |
| Box Score | Player Stats |
| Game Charts | Hand Charts |
| Play-By-Play | Hand History |
| Q1, Q2, Q3, Q4 | Level 34, 35, 36, 37 |
