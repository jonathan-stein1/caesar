echo off
cls
title Caesar
:1
echo Text:
set /p text=
cls
echo Passwort:
set /p password=
cls
echo Verschluesselte Nachricht:
python caesar.py --password "%password%" encrypt "%text%" 
pause > nul
cls
goto 1
