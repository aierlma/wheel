# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:36:59 2021

@author: AierlmaQuang
"""
import datetime
#for %%a in ("*.wav") do ffmpeg -ss 00:00:00 -t 01:59:58 -i "%%a" -f mp4 -vcodec copy -acodec copy output.wav
with open('temp.bat','w') as f:
    for i in range(50):
        f.write('for %%a in ("*.wav") do ffmpeg -ss '+str(datetime.timedelta(seconds=178*i))+\
                ' -t 00:02:58 -i "%%a" -f mp4 -vcodec copy -acodec copy '+\
                    str(i)+'.m4a'+'\n')