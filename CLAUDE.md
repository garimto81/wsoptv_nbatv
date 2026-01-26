# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

WSOP TV OTT 솔루션 기획 저장소. NBA TV League Pass UI를 1:1 복제하여 WSOP TV로 변환하는 프로젝트의 PRD, 와이어프레임, 분석 문서 모음.

**설계 원칙**: NBA TV 1:1 대응 (용어만 변경, 레이아웃/구조/인터랙션 유지)

## Google Docs Reference

**프로젝트 공식 문서** - 동일 제목 문서 다수 존재 시 반드시 아래 ID 사용:

| 문서 | Google Docs ID | 버전 | 동기화 날짜 |
|------|----------------|------|-------------|
| **WSOPTV : NBATV Analyze** | `1VE0StXfXN5-cUGXSLFTNp280VgTHxEHgRHaDrNUtBBo` | v5.1.0 | 2026-01-26 |

**PRD 동기화 URL** (고정 문서):
```
https://docs.google.com/document/d/1VE0StXfXN5-cUGXSLFTNp280VgTHxEHgRHaDrNUtBBo/edit
```

> 이 문서 ID는 고정되어 있으며, 모든 PRD 수정은 이 문서에서 진행합니다.
> 로컬 파일 (`docs/guides/WSOP-TV-PRD.md`)과 양방향 동기화됩니다.

## Repository Structure

```
docs/
├── guides/
│   ├── WSOP-TV-PRD.md              # 메인 PRD (v5.1.0)
│   ├── NBATV-UI-ANALYSIS.md        # UI 분석
│   └── NBATV-SCREENSHOT-ANALYSIS.md
├── mockups/
│   ├── nbatv/                      # NBA TV B&W 와이어프레임 (01~13)
│   ├── nbatv-analysis/             # 오버레이 분석 목업 (01~12)
│   └── wsoptv/                     # WSOP TV B&W 와이어프레임 (01~16)
└── images/mockups/                 # PNG 스크린샷
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

## Analysis Mockup Style Guide

분석 목업의 오버레이 색상 코드 (`nbatv-analysis/` 참조):

| 색상 | HEX | 용도 |
|------|-----|------|
| 파란색 | `#00f` | 주요 컴포넌트 |
| 초록색 | `#0c0` | 콘텐츠 영역 |
| 주황색 | `#f80` | 선택/활성 상태 |
| 빨간색 | `#c00` | 비디오/미디어 |
| 마젠타 | `#f0f` | 탭/네비게이션 |
| 시안 | `#0ff` | 타임라인/진행 |
| 노란색 | `#ff0` | 컨트롤/버튼 |

## Implementation Phases

- **Phase 1**: Core MVP (Video Player, Ticker, Controls, Tabs, Timeline)
- **Phase 2**: Core 확장 (MultiView, Featured Hands, Streaming Options)
- **Phase 3**: Core 완성 (Info tabs - Summary, Player Stats, Hand Charts, Hand History)
- **Phase 4**: Extension (Hole Cards, POT/BOARD 오버레이, Equity Calculator)
