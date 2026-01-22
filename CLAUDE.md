# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WSOP TV OTT 솔루션 기획 저장소. NBA TV League Pass UI를 1:1 복제하여 WSOP TV로 변환하는 프로젝트의 PRD, 와이어프레임, 분석 문서 모음.

**설계 원칙**: NBA TV 1:1 대응 (용어만 변경, 레이아웃/구조/인터랙션 유지)

## Repository Structure

```
docs/
├── guides/
│   └── WSOP-TV-PRD.md          # 메인 PRD (v5.1.0) - 17개 섹션, 4단계 변환 프로세스
├── mockups/
│   ├── nbatv/                  # NBA TV B&W 와이어프레임 (13개)
│   ├── nbatv-analysis/         # 오버레이 분석 목업 (13개)
│   └── wsoptv/                 # WSOP TV B&W 와이어프레임 (16개)
└── images/mockups/             # PNG 스크린샷
```

## Key Terminology Mapping

| NBA TV | WSOP TV |
|--------|---------|
| Scoreboard Ticker | Tournament Ticker |
| Key Plays | Featured Hands |
| Box Score | Player Stats |
| Game Charts | Hand Charts |
| Play-By-Play | Hand History |
| Q3 3:05 | L38 LIVE (Level) |

## Mockup Workflow

목업 확인 시 브라우저에서 HTML 직접 열기:
```powershell
start docs/mockups/wsoptv/01-main-streaming.html
```

Playwright로 스크린샷 캡처:
```powershell
npx playwright screenshot docs/mockups/wsoptv/01-main-streaming.html docs/images/mockups/wsoptv/01-main-streaming.png
```

## 4-Stage Conversion Process

각 기능별 변환 단계:
1. **NBA TV 스크린샷** - 실제 서비스 캡처 (`docs/guides/스크린샷 *.png`)
2. **NBA TV B&W 목업** - 흑백 와이어프레임 (`docs/mockups/nbatv/`)
3. **분석 다이어그램** - 레이어별 UI 패턴 분석 (`docs/mockups/nbatv-analysis/`)
4. **WSOP TV B&W 목업** - 최종 적용 목업 (`docs/mockups/wsoptv/`)

## Implementation Phases

- **Phase 1**: Core MVP (Video Player, Ticker, Controls, Tabs, Timeline)
- **Phase 2**: Core 확장 (MultiView, Featured Hands, Streaming Options)
- **Phase 3**: Core 완성 (Info tabs - Summary, Player Stats, Hand Charts, Hand History)
- **Phase 4**: Extension (Hole Cards, POT/BOARD 오버레이, Equity Calculator)
