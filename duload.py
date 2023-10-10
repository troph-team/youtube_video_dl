import json
import os
import shutil
from s3 import S3Client
import pandas as pd
import pyarrow.parquet as pq
from ytbdl import YoutubeDL

def load_json(path='hdvg_0.json'):
    # 读取JSON文件
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def load_parquet(path='hdvg_0.parquet'):
    table = pq.read_table(path)
    # 将表格转换为Pandas DataFrame
    df = table.to_pandas()
    return df

# 批量下载
def Duload(upload_s3_dir, index = 0, path='hdvg_0.parquet', batch_size = 200, download_directory="./ytbvideos", fails_upload_dir = "s3://dataset-hd-vg-130m/failedURLs/"):
    # judging variables
    batch_count = 0
    data = load_parquet(path)
    print(f"共有{len(data)}条数据待处理...")
    s3_client = S3Client()
    # 遍历DataFrame并按行读取key和url
    for _index, row in data.iterrows():# Read each line
        key = row['key']
        url = row['url']
        YoutubeDL(key, index, url, download_directory)
        batch_count += 1
        if(batch_count % batch_size == 0):
            # 到batch了，上传视频
            partition_files = [os.path.join(download_directory, filename) for filename in os.listdir(download_directory)]
            failed_uploads = s3_client.upload_parallel(partition_files, upload_s3_dir)
            if(len(failed_uploads)!=0):
                print("Failed uploads: ", failed_uploads)
            else:
                print("batch upload Successfully!")
            print(f"已处理{batch_count}条数据...")
            shutil.rmtree(download_directory)
            print("Cache Removed.")
    print("Uploading failed record...")
    s3_client.upload(f"./fails_{index}.txt", fails_upload_dir)

# UPLOAD_BASE_URL = "s3://dataset-hd-vg-130m/videos/" 
# Duload(UPLOAD_BASE_URL, path='hdvg_test.parquet')
# YoutubeDL("test","https://www.youtube.com/watch?v=----meyKR48", download_directory="./ytbvideos")    

        


