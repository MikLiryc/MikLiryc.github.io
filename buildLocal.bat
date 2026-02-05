@echo off
REM Build and serve Jekyll site

echo Building site...
bundle exec jekyll build

echo Starting local server...
bundle exec jekyll serve

pause
