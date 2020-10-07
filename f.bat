for %%a in ("*.mp4") do ffmpeg -i "%%a" -f mp4 -vn -codec copy out.wav
pause