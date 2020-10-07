for %%a in ("*.mp4") do ffmpeg -ss 00:00:00 -t 01:59:58 -i "%%a" -f mp4 -vcodec copy -acodec copy output.mp4
pause
