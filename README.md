# wheel

## 轮子们

>都是在windows环境下运行的，linux和mac暂无

- file-name.bat可以生成本目录下文件名，生成1.txt,对非utf-8和GBK编码字符支持不好
- file-name.py与file-name.bat功能类似，建议使用py文件
- rename.py可以重命名工作路径文件夹内文件，不给文件夹改名，记得手动设置想要改名的文件格式
- create_and_move.py可以创建与工作路径下所有文件同名的文件夹，并把对应文件放进去。比如这里有个movie.mp4，运行后创建movie文件夹，并把MP4放进去
- ts2mp4.bat可以把ts文件变成mp4到根目录找，利用了ffmpeg。使用前请先行下载ffmpeg
- ffmpeg_combind_videos.py可以生成temp文件，之后运行f.bat，将MP4合成一个，或者任意常见视频格式文件。利用了ffmpeg
- pic_combind.py可以把工作路径下图片按参数合并，使用时记得调参数。
- pic_cut.py可以把工作路径下所有图片按设定参数切割，使用时调参数，通常与pic_combind连用
- vid_separate.bat可以分割视频，使用时要调参数"for %%a in ("*.mp4") do ffmpeg -ss 00:00:00（start_time） -t 01:59:58（Last_time） -i "%%a" -f mp4 -vcodec copy -acodec copy 1%%~na.mp4"持续时间最好使用关键帧确定，potplayer用ctrl+shift+右箭头跳关键帧
- mp42wav.bat可以提取mp4视频音频成wav
- vid_cut2aud.bat可以直接把视频分割定时成音频 参数同vid_separate.bat
- pic_cut_combind.py把切割和合并两步放在一起
- fing_and_draw.py依赖于a.bat生成的1.txt或者直接用os.listdir()获取文件名。然后输入目的序号，会把需要的文件单独复制出来。
