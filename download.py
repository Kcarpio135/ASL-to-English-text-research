import json
import urllib.request
#import youtube_dl
import os
#pip install youtube-dl and the upgragde 

JSON_PATH = '/Real-time-ASL-to-English-text-translation/data/msasl/MSASL_val.json'
Video_path = '/data/videos'

with open('data/msasl/MSASL_val.json') as video_file:
    videos = video_file.read()

parsed_json = json.loads(videos)

count = 0
for i in range(len(parsed_json)):
    url = parsed_json[i]['url']
    name = parsed_json[i]['url'].split("=")[1]
    print(name)
    print(parsed_json[i]['url'])
    # count +=1
    try:
        print("Downloading starts...\n")
        os.system('yt-dlp -P data/videos -o "%(id)s.%(ext)s" URL ' + url + ' --recode-video mp4')
        #os.system('yt-dlp -o %(title)s-%(id)s.%(ext)s -P data/videos URL ' + url)
        print("Download completed..!!\n")
        # if count == 10:
        #     exit()
    except Exception as e:
        print(e)


download_yt_vids("MSASL_val.json")
print("done")