echo off
cls
title Caesar - Reconstruct
:1
echo Nachricht:
set /p input=
cls
echo Verschluesselte Nachricht:
set /p output=
cls
echo Passwort:
python reconstruct.py -i "%input%" -o "%output%"
pause > nul
cls
goto 1
