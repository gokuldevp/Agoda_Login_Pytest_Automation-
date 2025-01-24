@echo off
REM Activate the virtual environment
call .\.venv\Scripts\activate

REM Run pytest
pytest -s -v ./test_cases/test_login.py

REM Deactivate the virtual environment
deactivate
