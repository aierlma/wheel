for %%a in ("*.mp4") do ffmpeg -ss 00:00:00 -t 01:59:58 -i "%%a" -f mp4 -vn -codec copy out.aac
pause
