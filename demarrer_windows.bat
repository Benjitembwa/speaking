@echo off
chcp 65001 > nul
cd /d "%~dp0"
where python > nul 2> nul
if errorlevel 1 (
  echo Python est introuvable. Installe Python 3, ou ouvre directement index.html.
  pause
  exit /b 1
)
echo Site disponible sur http://localhost:8000/
start "" "http://localhost:8000/"
python -m http.server 8000
pause
