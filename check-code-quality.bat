@echo off

echo ###### static code analysis ######
python -m pipenv run pylama python/gilded_rose.py
set quality=%ERRORLEVEL%

echo .
echo ###### unit test ######
python -m pipenv run pytest
set test=%ERRORLEVEL%

echo .
echo ###### results ######
echo static code analysis result is: %ERRORLEVEL% 
echo unit test result is: %ERRORLEVEL% 
