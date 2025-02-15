@echo off
echo Installing required Python packages...
pip install -r requirements.txt
echo.
:: Set the color to red (Code 0C for red text)
color 0C
echo !!!!! Installation finie !!!!!
:: Reset the color to the default (Code 07 for default)
color 07
pause