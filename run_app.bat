@echo off
echo Starting News Impact Analyzer...
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Starting Streamlit application...
streamlit run app.py
pause 