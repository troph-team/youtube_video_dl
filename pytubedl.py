from pytube import YouTube
import os

# 下载单个视频
def YoutubeDL(video_name, index, video_url, download_directory):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()  # 获取最高分辨率的视频流
        video_filename = f"{video_name}.mp4"  # 构建视频文件名
        video_stream.download(output_path=download_directory, filename=video_filename)
        print(f"{video_name} 下载成功！")
    except Exception as e:
        print(f"下载失败: {video_url}")
        with open(f'fails_{index}.txt', 'a') as fail_file:
            fail_file.write(video_url + '\n')

