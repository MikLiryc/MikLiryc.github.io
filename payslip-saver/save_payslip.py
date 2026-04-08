"""
급여명세서 HTML → PDF 저장 도구
================================
비밀번호로 보호된 HTML 페이지에 접속하여 PDF로 저장합니다.

사용법:
  # 단일 URL
  python save_payslip.py --url "https://example.com/payslip" --password "1234"

  # 로컬 폴더 내 모든 HTML 일괄 변환
  python save_payslip.py --folder "C:/급여명세서" --password "1234"
  python save_payslip.py --folder "C:/급여명세서" --password "1234" --outdir "C:/PDF출력"

옵션:
  --url       접속할 URL (--folder와 택1)
  --folder    HTML 파일이 있는 폴더 경로 (--url과 택1)
  --password  비밀번호 (생략 시 프롬프트 입력)
  --output    저장할 PDF 파일명 (단일 URL 모드용)
  --outdir    PDF 출력 폴더 (폴더 모드용, 기본: HTML과 같은 폴더)
  --selector  비밀번호 입력 필드 CSS 셀렉터 (기본: input[type="password"])
  --submit    제출 버튼 CSS 셀렉터 (기본: 자동 감지)
  --wait      페이지 로드 후 추가 대기 시간(초) (기본: 2)
  --no-headless  브라우저 창을 표시 (디버깅용)
"""

import argparse
import getpass
import glob
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("❌ Playwright가 설치되어 있지 않습니다.")
    print("   다음 명령으로 설치하세요:")
    print("   pip install playwright")
    print("   playwright install chromium")
    sys.exit(1)


def save_payslip_to_pdf(
    url: str,
    password: str,
    output_path: str,
    password_selector: str = 'input[type="password"]',
    submit_selector: str | None = None,
    wait_seconds: float = 2,
    headless: bool = True,
):
    """비밀번호 보호된 HTML 페이지를 PDF로 저장합니다."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        print(f"🌐 페이지 접속 중... {url}")
        
        # --- 1) JavaScript prompt/confirm 가로채기 ---
        # 일부 사이트는 prompt()로 비밀번호를 받음
        page.on("dialog", lambda dialog: dialog.accept(password))
        
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
        except PlaywrightTimeout:
            print("❌ 페이지 로딩 시간 초과 (30초)")
            browser.close()
            return False

        # --- 2) 비밀번호 입력 폼 처리 ---
        try:
            pw_input = page.wait_for_selector(password_selector, timeout=5000)
            if pw_input:
                print("🔑 비밀번호 입력 중...")
                pw_input.fill(password)
                
                # 제출 버튼 찾기
                if submit_selector:
                    page.click(submit_selector)
                else:
                    # 자동 감지: submit 버튼 또는 Enter 키
                    submit_btn = page.query_selector(
                        'button[type="submit"], input[type="submit"], '
                        'button:has-text("확인"), button:has-text("로그인"), '
                        'button:has-text("열기"), button:has-text("OK")'
                    )
                    if submit_btn:
                        submit_btn.click()
                    else:
                        pw_input.press("Enter")
                
                print("⏳ 페이지 로드 대기 중...")
                page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeout:
            # 비밀번호 폼이 없음 → dialog로 이미 처리됐거나 비밀번호 불필요
            print("ℹ️  비밀번호 입력 폼 없음 (dialog 방식이거나 이미 인증됨)")

        # --- 3) 추가 대기 (동적 렌더링 등) ---
        if wait_seconds > 0:
            print(f"⏳ {wait_seconds}초 추가 대기...")
            page.wait_for_timeout(int(wait_seconds * 1000))

        # --- 4) PDF 저장 ---
        print(f"📄 PDF 저장 중... → {output_path}")
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={
                "top": "10mm",
                "bottom": "10mm",
                "left": "10mm",
                "right": "10mm",
            },
        )

        browser.close()
        print(f"✅ 저장 완료: {output_path}")
        return True


def process_folder(
    folder_path: str,
    password: str,
    outdir: str | None = None,
    password_selector: str = 'input[type="password"]',
    submit_selector: str | None = None,
    wait_seconds: float = 2,
    headless: bool = True,
):
    """폴더 내 모든 HTML 파일을 찾아 PDF로 변환합니다."""

    folder = Path(folder_path).resolve()
    if not folder.is_dir():
        print(f"[오류] 폴더를 찾을 수 없습니다: {folder}")
        sys.exit(1)

    # HTML 파일 수집
    html_files = sorted(folder.glob("*.html")) + sorted(folder.glob("*.htm"))
    if not html_files:
        print(f"[오류] HTML 파일이 없습니다: {folder}")
        sys.exit(1)

    # 출력 폴더
    out = Path(outdir).resolve() if outdir else folder
    out.mkdir(parents=True, exist_ok=True)

    print(f"========================================")
    print(f"  폴더: {folder}")
    print(f"  HTML 파일: {len(html_files)}개")
    print(f"  출력 폴더: {out}")
    print(f"========================================")

    success = 0
    fail = 0
    for i, html_file in enumerate(html_files, 1):
        print(f"\n[{i}/{len(html_files)}] {html_file.name}")
        pdf_name = html_file.stem + ".pdf"
        pdf_path = str(out / pdf_name)
        file_url = html_file.as_uri()

        ok = save_payslip_to_pdf(
            url=file_url,
            password=password,
            output_path=pdf_path,
            password_selector=password_selector,
            submit_selector=submit_selector,
            wait_seconds=wait_seconds,
            headless=headless,
        )
        if ok:
            success += 1
        else:
            fail += 1

    print(f"\n========================================")
    print(f"  완료: {success}개 성공, {fail}개 실패")
    print(f"========================================")


def main():
    parser = argparse.ArgumentParser(
        description="비밀번호 보호된 HTML 페이지를 PDF로 저장",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="접속할 URL (단일)")
    group.add_argument("--folder", help="HTML 파일이 있는 폴더 경로 (일괄 변환)")

    parser.add_argument("--password", default=None, help="비밀번호 (생략 시 프롬프트)")
    parser.add_argument("--output", default=None, help="출력 PDF 파일명 (단일 URL 모드)")
    parser.add_argument("--outdir", default=None, help="PDF 출력 폴더 (폴더 모드)")
    parser.add_argument(
        "--selector",
        default='input[type="password"]',
        help='비밀번호 입력 필드 CSS 셀렉터',
    )
    parser.add_argument("--submit", default=None, help="제출 버튼 CSS 셀렉터")
    parser.add_argument("--wait", type=float, default=2, help="추가 대기 시간(초)")
    parser.add_argument(
        "--no-headless", action="store_true", help="브라우저 창 표시 (디버깅)"
    )

    args = parser.parse_args()

    # 비밀번호
    password = args.password
    if password is None:
        password = getpass.getpass("비밀번호 입력: ")

    if args.folder:
        # ── 폴더 모드 ──
        process_folder(
            folder_path=args.folder,
            password=password,
            outdir=args.outdir,
            password_selector=args.selector,
            submit_selector=args.submit,
            wait_seconds=args.wait,
            headless=not args.no_headless,
        )
    else:
        # ── 단일 URL 모드 ──
        output = args.output
        if output is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output = f"payslip_{timestamp}.pdf"

        output_path = str(Path(output).resolve())

        save_payslip_to_pdf(
            url=args.url,
            password=password,
            output_path=output_path,
            password_selector=args.selector,
            submit_selector=args.submit,
            wait_seconds=args.wait,
            headless=not args.no_headless,
        )


if __name__ == "__main__":
    main()
