@echo off
title Potato Disease Classifier Launcher
color 0A

echo =====================================================
echo           Potato Disease Classification App
echo =====================================================
echo.

echo Launching Application...

:: Step 1: Start the FastAPI backend
echo [1/2] Starting FastAPI backend...
cd api
start cmd /k "title FastAPI Server & color 0B & python main.py"
cd ..
timeout /t 3 >nul

:: Step 2: Start Streamlit frontend
echo [2/2] Starting Streamlit frontend...
cd website
start cmd /k "title Streamlit App & color 0E & streamlit run app.py --server.headless true --server.port 8501"
cd ..
timeout /t 3 >nul

:: Step 3: Open frontend automatically in default browser
set "frontend_url=http://localhost:8501"
echo Opening frontend in your default browser...
start "" "%frontend_url%"

echo.
echo =====================================================
echo Application Started Successfully!
echo -----------------------------------------------------
echo API Server      : http://localhost:8000
echo Frontend URL    : %frontend_url%
echo =====================================================
echo.
echo Press any key to exit launcher...
pause >nul
exit /b
