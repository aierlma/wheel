@echo off

md %~d0\abc

for /f "delims=" %%a in ('dir /b /ad "%~dp0"') do (

for /f "delims=" %%i in ('dir /b "%%a"') do (

move "%%~fa\%%i" "%%~di\abc"

))

pause