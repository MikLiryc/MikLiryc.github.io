# 급여명세서 HTML → PDF 저장 도구

비밀번호로 보호된 HTML 페이지에 접속하여 PDF로 저장하는 도구입니다.

## 설치

```bash
cd payslip-saver
pip install -r requirements.txt
playwright install chromium
```

## 사용법

### 기본 사용
```bash
python save_payslip.py --url "https://example.com/payslip.html"
# → 비밀번호를 프롬프트로 입력받음
# → payslip_20260408_153000.pdf 로 저장
```

### 비밀번호 직접 전달
```bash
python save_payslip.py --url "https://example.com/payslip.html" --password "1234"
```

### 파일명 지정
```bash
python save_payslip.py --url "https://example.com/payslip.html" --output "2026년3월_급여명세서.pdf"
```

### 디버깅 (브라우저 창 표시)
```bash
python save_payslip.py --url "https://example.com/payslip.html" --no-headless
```

## 옵션

| 옵션 | 설명 | 기본값 |
|---|---|---|
| `--url` | 접속할 URL (필수) | - |
| `--password` | 비밀번호 | 프롬프트 입력 |
| `--output` | 저장 파일명 | `payslip_날짜_시간.pdf` |
| `--selector` | 비밀번호 입력 필드 CSS 셀렉터 | `input[type="password"]` |
| `--submit` | 제출 버튼 CSS 셀렉터 | 자동 감지 |
| `--wait` | 로드 후 추가 대기(초) | 2 |
| `--no-headless` | 브라우저 창 표시 | false |

## 지원하는 비밀번호 방식

1. **HTML form** — `<input type="password">` 필드에 자동 입력 후 제출
2. **JavaScript prompt()** — `prompt()` 다이얼로그 자동 응답
3. **커스텀 셀렉터** — `--selector` 옵션으로 특정 입력 필드 지정 가능

## 참고

- 로컬 HTML 파일도 `file:///C:/path/to/file.html` 형식으로 접속 가능합니다.

