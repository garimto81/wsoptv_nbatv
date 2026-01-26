"""
Google Docs PRD 문서 검증 스크립트

검증 항목:
1. 이미지 분석 (60개 이미지 검증)
2. 문서 구조/텍스트 분석 (헤딩, 섹션, 버전)
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# 인증 파일 경로
CREDENTIALS_FILE = r"C:\claude\json\desktop_credentials.json"
TOKEN_FILE = r"C:\claude\json\token.json"

# Google Docs API 범위 (토큰 파일과 동일하게)
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

# 대상 문서 ID
DOC_ID = "1VE0StXfXN5-cUGXSLFTNp280VgTHxEHgRHaDrNUtBBo"


@dataclass
class ImageInfo:
    """이미지 정보"""
    index: int
    uri: str
    width: Optional[float] = None
    height: Optional[float] = None


@dataclass
class HeadingInfo:
    """헤딩 정보"""
    level: int  # 1=H1, 2=H2, 3=H3
    text: str
    start_index: int


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


def analyze_images(doc: dict) -> list[ImageInfo]:
    """문서 내 이미지 분석"""
    images = []
    body = doc.get("body", {})
    content = body.get("content", [])

    image_count = 0

    def process_element(element, parent_index=0):
        nonlocal image_count

        # InlineObjectElement 확인
        if "inlineObjectElement" in element:
            inline_obj_id = element["inlineObjectElement"].get("inlineObjectId")
            if inline_obj_id:
                inline_objects = doc.get("inlineObjects", {})
                inline_obj = inline_objects.get(inline_obj_id, {})
                embedded_obj = inline_obj.get("inlineObjectProperties", {}).get("embeddedObject", {})

                image_props = embedded_obj.get("imageProperties", {})
                content_uri = image_props.get("contentUri", "")

                # 크기 정보
                size = embedded_obj.get("size", {})
                width = size.get("width", {}).get("magnitude")
                height = size.get("height", {}).get("magnitude")

                image_count += 1
                images.append(ImageInfo(
                    index=image_count,
                    uri=content_uri,
                    width=width,
                    height=height
                ))

        # Paragraph 내 elements 처리
        if "paragraph" in element:
            para_elements = element["paragraph"].get("elements", [])
            for para_elem in para_elements:
                process_element(para_elem, element.get("startIndex", 0))

        # Table 처리
        if "table" in element:
            for row in element["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    for cell_content in cell.get("content", []):
                        process_element(cell_content)

    for element in content:
        process_element(element)

    return images


def analyze_headings(doc: dict) -> list[HeadingInfo]:
    """문서 내 헤딩 분석"""
    headings = []
    body = doc.get("body", {})
    content = body.get("content", [])

    for element in content:
        if "paragraph" not in element:
            continue

        para = element["paragraph"]
        para_style = para.get("paragraphStyle", {})
        named_style = para_style.get("namedStyleType", "")

        if "HEADING" in named_style:
            level = int(named_style.replace("HEADING_", ""))

            # 텍스트 추출
            text_parts = []
            for elem in para.get("elements", []):
                if "textRun" in elem:
                    text_parts.append(elem["textRun"].get("content", ""))

            text = "".join(text_parts).strip()

            if text:
                headings.append(HeadingInfo(
                    level=level,
                    text=text,
                    start_index=element.get("startIndex", 0)
                ))

    return headings


def analyze_text_content(doc: dict) -> dict:
    """문서 전체 텍스트 분석"""
    body = doc.get("body", {})
    content = body.get("content", [])

    all_text = []

    def extract_text(element):
        if "paragraph" in element:
            for elem in element["paragraph"].get("elements", []):
                if "textRun" in elem:
                    all_text.append(elem["textRun"].get("content", ""))

        if "table" in element:
            for row in element["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    for cell_content in cell.get("content", []):
                        extract_text(cell_content)

    for element in content:
        extract_text(element)

    full_text = "".join(all_text)

    # 버전 정보 찾기
    version_match = re.search(r"v?(\d+\.\d+\.\d+)", full_text)
    version = version_match.group(1) if version_match else None

    return {
        "total_chars": len(full_text),
        "total_paragraphs": len(content),
        "version": version,
        "full_text": full_text
    }


def check_required_sections(headings: list[HeadingInfo], full_text: str) -> dict:
    """필수 섹션 존재 확인"""
    required_sections = [
        "설계 원칙",
        "메인 스트리밍",
        "Streaming Options",
        "MultiView",
        "Featured Hands",
        "Info",
        "Player Controls",
        "UX 워크플로우",
    ]

    results = {}
    heading_texts = [h.text.lower() for h in headings]

    for section in required_sections:
        # 헤딩에서 찾기
        found_in_heading = any(section.lower() in h for h in heading_texts)
        # 본문에서 찾기
        found_in_text = section.lower() in full_text.lower()

        results[section] = {
            "in_heading": found_in_heading,
            "in_text": found_in_text,
            "status": "PASS" if (found_in_heading or found_in_text) else "FAIL"
        }

    return results


def validate_image_sizes(images: list[ImageInfo]) -> dict:
    """이미지 크기 검증"""
    MIN_SIZE = 50
    MAX_WIDTH = 800
    MAX_HEIGHT = 600

    issues = []
    valid_count = 0

    for img in images:
        problems = []

        if img.width and img.width < MIN_SIZE:
            problems.append(f"너비 너무 작음: {img.width}px")
        if img.height and img.height < MIN_SIZE:
            problems.append(f"높이 너무 작음: {img.height}px")
        if img.width and img.width > MAX_WIDTH:
            problems.append(f"너비 너무 큼: {img.width}px")
        if img.height and img.height > MAX_HEIGHT:
            problems.append(f"높이 너무 큼: {img.height}px")

        if not img.uri:
            problems.append("URI 없음")

        if problems:
            issues.append({
                "index": img.index,
                "problems": problems
            })
        else:
            valid_count += 1

    return {
        "total": len(images),
        "valid": valid_count,
        "issues": issues
    }


def main():
    print("=" * 60)
    print("Google Docs PRD 문서 검증")
    print("=" * 60)
    print(f"문서 ID: {DOC_ID}")
    print()

    # 인증
    print("[1/4] 인증 중...")
    creds = get_credentials()
    docs_service = build("docs", "v1", credentials=creds)

    # 문서 가져오기
    print("[2/4] 문서 로드 중...")
    doc = docs_service.documents().get(documentId=DOC_ID).execute()
    title = doc.get("title", "Unknown")
    print(f"  제목: {title}")

    # 이미지 분석
    print("\n[3/4] 이미지 분석 중...")
    images = analyze_images(doc)
    print(f"  발견된 이미지: {len(images)}개")

    image_validation = validate_image_sizes(images)
    print(f"  유효한 이미지: {image_validation['valid']}/{image_validation['total']}")

    if image_validation['issues']:
        print(f"  문제 있는 이미지: {len(image_validation['issues'])}개")
        for issue in image_validation['issues'][:5]:  # 처음 5개만 표시
            print(f"    - 이미지 #{issue['index']}: {', '.join(issue['problems'])}")
        if len(image_validation['issues']) > 5:
            print(f"    ... 외 {len(image_validation['issues']) - 5}개")

    # 문서 구조 분석
    print("\n[4/4] 문서 구조 분석 중...")
    headings = analyze_headings(doc)
    text_info = analyze_text_content(doc)

    print(f"  총 문자 수: {text_info['total_chars']:,}")
    print(f"  총 paragraph: {text_info['total_paragraphs']}")
    print(f"  버전: {text_info['version'] or '찾을 수 없음'}")

    # 헤딩 구조 분석
    h1_count = sum(1 for h in headings if h.level == 1)
    h2_count = sum(1 for h in headings if h.level == 2)
    h3_count = sum(1 for h in headings if h.level == 3)
    print(f"  헤딩 구조: H1={h1_count}, H2={h2_count}, H3={h3_count}")

    # 필수 섹션 확인
    section_check = check_required_sections(headings, text_info['full_text'])

    print("\n" + "=" * 60)
    print("검증 결과")
    print("=" * 60)

    # 이미지 결과
    img_status = "PASS" if image_validation['valid'] == image_validation['total'] else "WARN"
    print(f"\n1. 이미지 검증: {img_status}")
    print(f"   - 총 이미지: {image_validation['total']}개")
    print(f"   - 유효: {image_validation['valid']}개")
    print(f"   - 문제: {len(image_validation['issues'])}개")

    # 버전 결과
    version_status = "PASS" if text_info['version'] == "5.1.0" else "WARN"
    print(f"\n2. 버전 정보: {version_status}")
    print(f"   - 발견된 버전: {text_info['version']}")
    print(f"   - 예상 버전: 5.1.0")

    # 섹션 결과
    section_pass_count = sum(1 for s in section_check.values() if s['status'] == 'PASS')
    section_status = "PASS" if section_pass_count == len(section_check) else "WARN"
    print(f"\n3. 필수 섹션: {section_status}")
    print(f"   - 확인됨: {section_pass_count}/{len(section_check)}")

    for section, result in section_check.items():
        status_icon = "[O]" if result['status'] == 'PASS' else "[X]"
        print(f"   {status_icon} {section}")

    # 전체 결과
    print("\n" + "=" * 60)
    all_pass = (
        img_status == "PASS" and
        version_status == "PASS" and
        section_status == "PASS"
    )
    final_status = "ALL PASS" if all_pass else "NEEDS REVIEW"
    print(f"최종 결과: {final_status}")
    print("=" * 60)

    return {
        "images": image_validation,
        "version": text_info['version'],
        "sections": section_check,
        "headings": {
            "h1": h1_count,
            "h2": h2_count,
            "h3": h3_count
        }
    }


if __name__ == "__main__":
    main()
