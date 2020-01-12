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
echo Entschluesselte Nachricht:
python caesar.py --password "%password%" decrypt "%text%"
pause > nul
cls
goto 1
