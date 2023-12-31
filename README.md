# youtube_video_dl

* 提供`pytube`&`yt-dlp`的youtube单一视频文件下载

* 大多数情况下，YouTube不要求用户登录才能下载公共视频。通常，你可以直接使用`pytube`或类似的库来下载这些视频，而无需登录
* 若需要登录，可以使用YouTube Data API

## YouTube Data API获取方式

1. **创建Google Cloud项目**：

   首先，你需要创建一个Google Cloud项目，因为YouTube Data API是Google Cloud服务的一部分。前往[Google Cloud Console](https://console.cloud.google.com/)，登录你的Google帐号，并创建一个新的项目。

2. **启用YouTube Data API**：

   在你的Google Cloud项目中，转到API和服务 > 仪表板，然后点击 "启用API和服务"。在搜索框中输入 "YouTube Data API v3" 并选择它。点击 "启用" 按钮。

3. **创建API密钥**：

   在你的Google Cloud项目中，点击 "凭据" 选项卡，然后点击 "创建凭据" 按钮。选择 "API 密钥" 选项，Google将为你生成一个API密钥。

4. **安装Google API客户端库**：

   在你的Python环境中安装Google API客户端库，这将帮助你与YouTube Data API进行通信。你可以使用以下命令来安装：

   ```bash
   pip install --upgrade google-api-python-client
   ```

5. **编写Python代码**：

   接下来，你可以编写Python代码来使用YouTube Data API。以下是一个简单示例，演示如何使用API获取视频信息：

   ```python
   from googleapiclient.discovery import build
   
   # 替换为你的API密钥
   api_key = 'your_api_key_here'
   
   # 创建YouTube Data API客户端
   youtube = build('youtube', 'v3', developerKey=api_key)
   
   # 使用API获取视频信息
   video_id = 'your_video_id_here'
   video_response = youtube.videos().list(
       part='snippet',
       id=video_id
   ).execute()
   
   video_info = video_response['items'][0]['snippet']
   print(f'Title: {video_info["title"]}')
   print(f'Published At: {video_info["publishedAt"]}')
   print(f'Channel Title: {video_info["channelTitle"]}')
   ```

   

请将 `'your_api_key_here'` 替换为你在步骤3中创建的API密钥，并将 `'your_video_id_here'` 替换为你想要获取信息的视频的ID。
