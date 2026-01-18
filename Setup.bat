@echo off
setlocal

echo Checking if python is installed...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Install python from https://python.org .
    pause
    exit /b
)

echo Checking pip...
python -m pip --version>nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pip...
    python -m ensurepip --upgrade
)

echo Installing dependence...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Setup finished.
pause