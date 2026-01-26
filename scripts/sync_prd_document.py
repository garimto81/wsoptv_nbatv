"""
Google Docs PRD 동기화 스크립트

CLAUDE.md에 등록된 Google Docs와 로컬 Markdown 파일 동기화

사용법:
    python scripts/sync_prd_document.py check   # 차이점 확인
    python scripts/sync_prd_document.py pull    # Google Docs → 로컬
    python scripts/sync_prd_document.py push    # 로컬 → Google Docs
"""

import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Tuple
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# 인증 파일 경로
CREDENTIALS_FILE = r"C:\claude\json\desktop_credentials.json"
TOKEN_FILE = r"C:\claude\json\token.json"

# Google Docs API 범위
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

# 프로젝트 루트
PROJECT_ROOT = Path(__file__).parent.parent


@dataclass
class DocMapping:
    """문서 매핑 정보"""
    doc_id: str
    doc_title: str
    local_path: Path
    version: str
    sync_date: str


def get_credentials() -> Credentials:
    """OAuth 2.0 인증 정보 획득"""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds


def parse_claude_md() -> Optional[DocMapping]:
    """CLAUDE.md에서 Google Docs 매핑 정보 파싱"""
    claude_md_path = PROJECT_ROOT / "CLAUDE.md"

    if not claude_md_path.exists():
        print(f"[ERROR] CLAUDE.md not found: {claude_md_path}")
        return None

    content = claude_md_path.read_text(encoding="utf-8")

    # Google Docs ID 추출 (테이블에서)
    # | **WSOP TV PRD** | `1VE0StXfXN5-cUGXSLFTNp280VgTHxEHgRHaDrNUtBBo` | v5.1.0 | 2026-01-26 |
    doc_pattern = r'\|\s*\*\*(.+?)\*\*\s*\|\s*`([a-zA-Z0-9_-]+)`\s*\|\s*v?([\d.]+)\s*\|\s*([\d-]+)\s*\|'

    match = re.search(doc_pattern, content)
    if not match:
        print("[ERROR] Google Docs mapping not found in CLAUDE.md")
        return None

    doc_title = match.group(1)
    doc_id = match.group(2)
    version = match.group(3)
    sync_date = match.group(4)

    # 로컬 파일 경로 추출
    # 로컬 PRD (`docs/guides/WSOP-TV-PRD.md` v5.1.0)
    local_pattern = r'`(docs/[^`]+\.md)`'
    local_match = re.search(local_pattern, content)

    if local_match:
        local_path = PROJECT_ROOT / local_match.group(1)
    else:
        # 기본 경로
        local_path = PROJECT_ROOT / "docs" / "guides" / "WSOP-TV-PRD.md"

    return DocMapping(
        doc_id=doc_id,
        doc_title=doc_title,
        local_path=local_path,
        version=version,
        sync_date=sync_date
    )


def extract_text_from_doc(doc: dict) -> str:
    """Google Docs 문서에서 텍스트 추출"""
    body = doc.get("body", {})
    content = body.get("content", [])

    text_parts = []

    def process_element(element):
        if "paragraph" in element:
            para = element["paragraph"]
            para_style = para.get("paragraphStyle", {})
            named_style = para_style.get("namedStyleType", "")

            line_parts = []
            for elem in para.get("elements", []):
                if "textRun" in elem:
                    line_parts.append(elem["textRun"].get("content", ""))

            line = "".join(line_parts)

            # 헤딩 처리
            if "HEADING" in named_style:
                level = int(named_style.replace("HEADING_", ""))
                prefix = "#" * level + " "
                line = prefix + line.strip() + "\n"

            text_parts.append(line)

        elif "table" in element:
            table = element["table"]
            rows = table.get("tableRows", [])

            for row_idx, row in enumerate(rows):
                cells = row.get("tableCells", [])
                row_parts = []

                for cell in cells:
                    cell_text = []
                    for cell_content in cell.get("content", []):
                        if "paragraph" in cell_content:
                            for elem in cell_content["paragraph"].get("elements", []):
                                if "textRun" in elem:
                                    cell_text.append(elem["textRun"].get("content", "").strip())
                    row_parts.append(" ".join(cell_text))

                text_parts.append("| " + " | ".join(row_parts) + " |\n")

                # 헤더 구분선
                if row_idx == 0:
                    text_parts.append("|" + "|".join(["---"] * len(cells)) + "|\n")

            text_parts.append("\n")

    for element in content:
        process_element(element)

    return "".join(text_parts)


def get_doc_content(doc_id: str) -> Tuple[str, dict]:
    """Google Docs 문서 내용 조회"""
    creds = get_credentials()
    docs_service = build("docs", "v1", credentials=creds)

    doc = docs_service.documents().get(documentId=doc_id).execute()
    text = extract_text_from_doc(doc)

    return text, doc


def get_local_content(local_path: Path) -> str:
    """로컬 Markdown 파일 내용 조회"""
    if not local_path.exists():
        return ""
    return local_path.read_text(encoding="utf-8")


def compare_documents(gdocs_text: str, local_text: str) -> dict:
    """문서 비교"""
    gdocs_lines = gdocs_text.strip().split("\n")
    local_lines = local_text.strip().split("\n")

    # 간단한 비교 (줄 수, 문자 수)
    return {
        "gdocs_lines": len(gdocs_lines),
        "local_lines": len(local_lines),
        "gdocs_chars": len(gdocs_text),
        "local_chars": len(local_text),
        "line_diff": len(gdocs_lines) - len(local_lines),
        "char_diff": len(gdocs_text) - len(local_text),
        "identical": gdocs_text.strip() == local_text.strip()
    }


def update_claude_md_sync_date(sync_date: str):
    """CLAUDE.md의 동기화 날짜 업데이트"""
    claude_md_path = PROJECT_ROOT / "CLAUDE.md"
    content = claude_md_path.read_text(encoding="utf-8")

    # 날짜 패턴 교체
    updated = re.sub(
        r'(\|\s*\*\*WSOP TV PRD\*\*\s*\|\s*`[^`]+`\s*\|\s*v?[\d.]+\s*\|\s*)[\d-]+(\s*\|)',
        rf'\g<1>{sync_date}\2',
        content
    )

    claude_md_path.write_text(updated, encoding="utf-8")


def cmd_check(mapping: DocMapping):
    """차이점 확인"""
    print("=" * 60)
    print("Google Docs PRD 동기화 상태 확인")
    print("=" * 60)
    print(f"문서: {mapping.doc_title}")
    print(f"Doc ID: {mapping.doc_id}")
    print(f"로컬 파일: {mapping.local_path}")
    print(f"버전: v{mapping.version}")
    print(f"마지막 동기화: {mapping.sync_date}")
    print()

    print("[1/2] Google Docs 조회 중...")
    gdocs_text, doc = get_doc_content(mapping.doc_id)

    print("[2/2] 로컬 파일 조회 중...")
    local_text = get_local_content(mapping.local_path)

    print()
    comparison = compare_documents(gdocs_text, local_text)

    print("=" * 60)
    print("비교 결과")
    print("=" * 60)
    print(f"Google Docs: {comparison['gdocs_lines']:,} lines, {comparison['gdocs_chars']:,} chars")
    print(f"로컬 파일:   {comparison['local_lines']:,} lines, {comparison['local_chars']:,} chars")
    print()

    if comparison['identical']:
        print("상태: [SYNC] 동기화됨")
    else:
        print("상태: [DIFF] 차이 있음")
        print(f"  줄 차이: {comparison['line_diff']:+d}")
        print(f"  문자 차이: {comparison['char_diff']:+d}")

        if comparison['gdocs_chars'] > comparison['local_chars']:
            print("  -> Google Docs가 더 최신 (pull 권장)")
        else:
            print("  -> 로컬이 더 최신 (push 권장)")

    return comparison


def cmd_pull(mapping: DocMapping, force: bool = False):
    """Google Docs → 로컬 동기화"""
    print("=" * 60)
    print("Google Docs -> 로컬 동기화 (pull)")
    print("=" * 60)

    # 먼저 체크
    comparison = cmd_check(mapping)

    if comparison['identical'] and not force:
        print("\n이미 동기화되어 있습니다.")
        return

    print()
    if not force:
        confirm = input("로컬 파일을 덮어쓰시겠습니까? [y/N]: ")
        if confirm.lower() != 'y':
            print("취소됨")
            return

    print("\n동기화 중...")
    gdocs_text, _ = get_doc_content(mapping.doc_id)

    # 백업 생성
    backup_path = mapping.local_path.with_suffix(".md.bak")
    if mapping.local_path.exists():
        import shutil
        shutil.copy(mapping.local_path, backup_path)
        print(f"백업 생성: {backup_path}")

    # 파일 저장
    mapping.local_path.write_text(gdocs_text, encoding="utf-8")
    print(f"저장 완료: {mapping.local_path}")

    # 동기화 날짜 업데이트
    today = datetime.now().strftime("%Y-%m-%d")
    update_claude_md_sync_date(today)
    print(f"CLAUDE.md 동기화 날짜 업데이트: {today}")

    print("\n[DONE] 동기화 완료!")


def cmd_push(mapping: DocMapping, force: bool = False):
    """로컬 → Google Docs 동기화"""
    print("=" * 60)
    print("로컬 -> Google Docs 동기화 (push)")
    print("=" * 60)

    # 먼저 체크
    comparison = cmd_check(mapping)

    if comparison['identical'] and not force:
        print("\n이미 동기화되어 있습니다.")
        return

    print()
    if not force:
        confirm = input("Google Docs를 덮어쓰시겠습니까? [y/N]: ")
        if confirm.lower() != 'y':
            print("취소됨")
            return

    print("\n동기화 중...")

    # 로컬 콘텐츠 읽기
    local_text = get_local_content(mapping.local_path)

    # Google Docs 업데이트 (lib.google_docs 모듈 사용)
    print("Google Docs 업데이트 실행...")
    print("  cd C:\\claude && python -m lib.google_docs convert ...")

    import subprocess
    result = subprocess.run(
        [
            "python", "-m", "lib.google_docs", "update",
            mapping.doc_id,
            str(mapping.local_path)
        ],
        cwd=r"C:\claude",
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)

        # 동기화 날짜 업데이트
        today = datetime.now().strftime("%Y-%m-%d")
        update_claude_md_sync_date(today)
        print(f"CLAUDE.md 동기화 날짜 업데이트: {today}")

        print("\n[DONE] 동기화 완료!")
    else:
        print(f"[ERROR] 업데이트 실패:")
        print(result.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Google Docs PRD 동기화",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python scripts/sync_prd_document.py check   # 차이점 확인
  python scripts/sync_prd_document.py pull    # Google Docs -> 로컬
  python scripts/sync_prd_document.py push    # 로컬 -> Google Docs
  python scripts/sync_prd_document.py pull --force  # 확인 없이 실행
"""
    )

    parser.add_argument(
        "action",
        choices=["check", "pull", "push"],
        help="동기화 작업: check (확인), pull (GDocs->로컬), push (로컬->GDocs)"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="확인 없이 강제 실행"
    )

    args = parser.parse_args()

    # CLAUDE.md에서 매핑 정보 파싱
    mapping = parse_claude_md()
    if not mapping:
        sys.exit(1)

    # 작업 실행
    if args.action == "check":
        cmd_check(mapping)
    elif args.action == "pull":
        cmd_pull(mapping, force=args.force)
    elif args.action == "push":
        cmd_push(mapping, force=args.force)


if __name__ == "__main__":
    main()
