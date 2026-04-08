@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
echo ============================================
echo   급여명세서 PDF 저장 도구
echo ============================================
echo.

REM ── Python 설치 확인 ──
python --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않습니다.
    echo   https://www.python.org/downloads/ 에서 설치하세요.
    echo   설치 시 "Add Python to PATH" 체크 필수!
    echo.
    pause
    exit /b 1
)

REM ── Playwright 설치 확인 ──
python -c "import playwright" >nul 2>&1
if errorlevel 1 (
    echo [설치] Playwright를 설치합니다...
    python -m pip install playwright --quiet
    python -m playwright install chromium
    echo [설치] 완료!
    echo.
)

REM ── 모드 선택 ──
echo [1] 폴더 지정 (폴더 안 모든 HTML을 PDF로 변환)
echo [2] URL 직접 입력 (단일 페이지)
echo.
set /p MODE="모드 선택 (1 또는 2): "

if "!MODE!"=="1" goto FOLDER_MODE
if "!MODE!"=="2" goto URL_MODE
echo [오류] 1 또는 2를 입력하세요.
goto END

:FOLDER_MODE
set /p FOLDER="HTML 폴더 경로: "
set /p PW="비밀번호: "
set /p OUTDIR="PDF 출력 폴더 (Enter=HTML과 같은 폴더): "
if "!OUTDIR!"=="" (
    python save_payslip.py --folder "!FOLDER!" --password "!PW!"
) else (
    python save_payslip.py --folder "!FOLDER!" --password "!PW!" --outdir "!OUTDIR!"
)
goto END

:URL_MODE
set /p URL="URL 입력: "
set /p PW="비밀번호: "
set /p FILENAME="저장 파일명 (Enter=자동): "
if "!FILENAME!"=="" (
    python save_payslip.py --url "!URL!" --password "!PW!"
) else (
    python save_payslip.py --url "!URL!" --password "!PW!" --output "!FILENAME!"
)
goto END

:END
echo.
pause
