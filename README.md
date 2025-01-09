# wheel

## 轮子们

> 都是在windows环境下运行的，linux和mac暂无

- file-name.bat可以生成本目录下文件名，生成1.txt,对非utf-8和GBK编码字符支持不好
- file-name.py与file-name.bat功能类似，建议使用py文件
- rename.py可以重命名工作路径文件夹内文件，不给文件夹改名，记得手动设置想要改名的文件格式
- create_and_move.py可以创建与工作路径下所有文件同名的文件夹，并把对应文件放进去。比如这里有个movie.mp4，运行后创建movie文件夹，并把MP4放进去
- ts2mp4.bat可以把ts文件变成mp4到根目录找，利用了ffmpeg。使用前请先行下载ffmpeg
- ffmpeg_combind_videos.py可以生成temp文件，之后运行f.bat，将MP4合成一个，或者任意常见视频格式文件。利用了ffmpeg
- pic_combind.py可以把工作路径下图片按参数合并，使用时记得调参数。
- pic_cut.py可以把工作路径下所有图片按设定参数切割，使用时调参数，通常与pic_combind连用
- vid_separate.bat可以分割视频，使用时要调参数"for %%a in ("*.mp4") do ffmpeg -ss 00:00:00（start_time） -t 01:59:58（Last_time） -i "%%a" -f mp4 -vcodec copy -acodec copy 1%%~na.mp4"持续时间最好使用关键帧确定，potplayer用ctrl+shift+右箭头跳关键帧
- mp42mp3.bat可以提取mp4视频音频成mp3
- vid_cut2aud.bat可以直接把视频分割定时成音频 参数同vid_separate.bat
- pic_cut_combind.py把切割和合并两步放在一起
- fing_and_draw.py依赖于a.bat生成的1.txt或者直接用os.listdir()获取文件名。然后输入目的序号，会把需要的文件单独复制出来。会生成两个txt，not_finished.txt记录了未成功复制的，original.txt记录了复制文件的原路径
- gbk2utf8.py是把编码为非utf-8的转变为utf8编码
- my_function.py记录我所用的函数，可以用来查表
- combind_srt.py合并该文件夹srt文件
- delay_sub.py延后该文件夹所有字幕的时间
- subfinder.py可以根据已有的字幕文件找工作文件夹下的影片是否具有外挂字幕，有则把已有字幕文件复制到相应影片文件夹里
- fanhao_get.py可以从javbus获取页面里的番号保存到工作路径下的result.txt
- 搜索字幕.py从javbus获取影片是否有字幕
- danmu_optimise.py可以把低于1/4屏幕的弹幕清除掉。也可以把它们改成高于1/4屏幕的
- split_big_audio_into_small.py可以把长视频或音频变成顺序的短视频或音频，通过导出一个bat利用ffmpeg完成
- picspider.py是我的第一个爬虫脚本，可以爬取网页图片并保存
- mp42mp3(keep_file_name).bat提取当前目录下所有mp4的音频成mp3，保留原文件名
- file_rename.py可以按照特定目的对文件重命名
- spider2.py是加强版爬虫脚本
- txtcombind.py用来合并txt
- autocombind.py可以自动合成多个文件夹下的视频
- graphing.py可以读取excel表格，并根据列做图及给出回归方程
- argparse.py给出argparse module的使用方法，用来获取用户输入，与CLI有关
- beautifulsoup_method.py给出bs4 module 的使用方法
- delete_repeat.py 可以将来自faster-whisper-webui large-v3的转录字幕srt中的重复片段去掉，只需要将它们呢放在哦同一个目录下。注意，该脚本着重于对日语转录本进行预处理。处理后的结果会在同一个目录下生成，后缀加merged。就可以直接放在翻译机里翻译了。
- export-emby-fav.py 作用是在当前目录输出emby中的"最爱"的所有项目和指定的合集的项目
- autossl.sh 用于在Linux上自动配置nginx反代和证书申请，配合cloudflare体验更佳
