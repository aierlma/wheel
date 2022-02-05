for %%a in ("*.mp4") do ffmpeg -i "%%~sa" -f mp3 "%%~na.mp3"
pause
