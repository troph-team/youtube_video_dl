from googleapiclient.discovery import build
from pytube import YouTube
import os
 # 替换为你的API密钥
APIKEY = 'your-api-key'
# APIKEY = 'AIzaSyDkaF-eRtplLTokhwiZj_TcRPX_n1sSuTI'

# 使用YouTube Data API获取视频信息
def get_video_info(api_key, video_url):
    api_key = APIKEY
    video_id = video_url.split('v=')[1]  # 从视频URL中提取视频ID
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    video_info = video_response['items'][0]['snippet']
    return video_info

# 下载单个视频
def YoutubeDL(video_name, index, video_url, download_directory):
    api_key = APIKEY
    try:
        # 使用YouTube Data API获取视频信息
        video_info = get_video_info(api_key, video_url)
        title = video_info['title']

        # 使用pytube下载视频
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_filename = f"{video_name}.mp4"
        video_stream.download(output_path=download_directory, filename=video_filename)
        print(f"{title} 下载成功！ key: {video_name}")
    except Exception as e:
        print(f"下载失败: {video_url}")
        with open(f'fails_{index}.txt', 'a') as fail_file:
            fail_file.write(video_url + '\n')

