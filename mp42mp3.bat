for %%a in ("*.mp4") do ffmpeg -i "%%a" -f mp3 out.mp3
pause
