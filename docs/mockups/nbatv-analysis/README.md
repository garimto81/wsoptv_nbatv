# NBA TV → WSOP TV Analysis Mockups

**Version**: 2.0.0
**Date**: 2026-01-22

기존 B&W 와이어프레임 목업 위에 **오버레이 분석**을 적용한 목업입니다.
각 파일은 원본 UI를 완전히 포함하며, 그 위에 색상 하이라이트와 주석이 배치됩니다.

---

## 목업 인덱스 (13개)

| # | 파일명 | 원본 목업 | 분석 포인트 | WSOP 힌트 |
|---|--------|----------|------------|----------|
| 01 | `01-main-streaming-analysis.html` | `nbatv/01-main-streaming.html` | 7단 레이어 구조 | Tournament Streaming |
| 02 | `02-streaming-options-broadcasts-analysis.html` | `nbatv/02-streaming-options-broadcasts.html` | 모달/탭/옵션 | Table Selection Modal |
| 03 | `03-streaming-options-audio-analysis.html` | `nbatv/03-streaming-options-audio.html` | 라디오 옵션 | Commentary Language |
| 04 | `04-multiview-selector-analysis.html` | `nbatv/04-multiview-selector.html` | 레이아웃 버튼 | Multi-Table Selector |
| 05 | `05-multiview-layout-analysis.html` | `nbatv/05-multiview-1x2.html` | Cell 구조 | Multi-Table Layout |
| 06 | `06-info-summary-analysis.html` | `nbatv/08-info-summary.html` | 7:3 레이아웃 | Tournament Summary |
| 07 | `07-info-boxscore-analysis.html` | `nbatv/09-info-boxscore.html` | 통계 테이블 | Player Statistics |
| 08 | `08-info-gamecharts-analysis.html` | `nbatv/10-info-gamecharts.html` | 차트 영역 | Hand History Charts |
| 09 | `09-info-playbyplay-analysis.html` | `nbatv/11-info-playbyplay.html` | 타임라인 구조 | Hand-by-Hand Timeline |
| 10 | `10-modal-keyplays-analysis.html` | `nbatv/12-modal-keyplays.html` | 카드 구조 | Featured Hands Modal |
| 11 | `11-keyplays-player-analysis.html` | `nbatv/13-keyplays-player.html` | 플레이어 오버레이 | Featured Hand Player |
| 12 | `12-player-controls-analysis.html` | `nbatv/07-player-controls.html` | 컨트롤 그룹 | Poker Control Extensions |
| -- | `sample-overlay-analysis.html` | (템플릿) | 오버레이 스타일 참조 | - |

---

## 분석 스타일 가이드

모든 목업은 `sample-overlay-analysis.html` 스타일을 따릅니다:

### 시각적 요소

| 요소 | 용도 | 색상 |
|------|------|------|
| **Section Overlay** | UI 레이어 구분 | 각 레이어별 고유 색상 |
| **Annotation Box** | 분석 설명 | 노란색 (#ff0) |
| **Number Badge** | 순서 표시 | 빨간색 (#c00) |
| **Legend Panel** | 범례 | 검정 배경 + 노란 테두리 |
| **WSOP TV Hint** | 변환 매핑 | 회색 이탤릭 |

### 하이라이트 색상 코드

| 색상 | HEX | 용도 |
|------|-----|------|
| 파란색 | `#00f` | 주요 컴포넌트 |
| 초록색 | `#0c0` | 콘텐츠 영역 |
| 주황색 | `#f80` | 선택/활성 상태 |
| 빨간색 | `#c00` | 비디오/미디어 |
| 마젠타 | `#f0f` | 탭/네비게이션 |
| 시안 | `#0ff` | 타임라인/진행 |
| 노란색 | `#ff0` | 컨트롤/버튼 |

---

## 사용 방법

```bash
# 브라우저에서 직접 열기
start docs/mockups/nbatv-analysis/01-main-streaming-analysis.html

# 모든 분석 목업 순차 확인 (오버레이 버전만)
for %%f in (docs\mockups\nbatv-analysis\*-analysis.html) do start %%f
```

## 분석 목업 구조

```
┌─────────────────────────────────────────────────────────────┐
│ [기존 NBA TV B&W 목업] ← 와이어프레임 UI 전체 포함         │
│   ┌───────────────────────────────────────────────────────┐ │
│   │ [Section Overlay] ← 반투명 색상 하이라이트            │ │
│   │   ┌─────────────────────────────────────────────────┐ │ │
│   │   │ [Annotation Box] ← 노란색 설명 박스             │ │ │
│   │   │   ① 번호 배지 + 설명 + WSOP TV 힌트            │ │ │
│   │   └─────────────────────────────────────────────────┘ │ │
│   └───────────────────────────────────────────────────────┘ │
│ [Legend Panel] ← 좌측 하단 범례                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 관련 문서

- **PRD**: `docs/guides/WSOP-TV-PRD.md`
- **Google Slides 원본 이미지**: `docs/images/slides-analysis/`
- **승인된 샘플**: `sample-overlay-analysis.html`
