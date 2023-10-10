import yt_dlp
import os

# 下载单个, name就是key
def YoutubeDL(video_name, index, video_url, download_directory):
    # 创建 yt_dlp 下载器对象
    ydl_opts = {
        'format': 'best',  # 选择最佳质量
        'outtmpl': os.path.join(download_directory, f'{video_name}.%(ext)s'),  # 指定保存的文件名格式
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"{video_name} Downloading...", end=' ')
            ydl.download([video_url])
            print(f"Successfully!")
        except Exception as e:
            print(f"下载失败: {video_url}")
            with open(f'fails_{index}.txt', 'a') as fail_file:
                fail_file.write(video_url + '\n')