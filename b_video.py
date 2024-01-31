#https://www.bilibili.com/video/BV14Y4y1j7s4?t=6.2&p=14

import requests
import re
import json
import subprocess

headers = {
    'Cookie':'buvid3=FD1B8E93-B27B-5D5D-5A03-7557B50601BB81101infoc; b_nut=1706348781; CURRENT_FNVAL=16; _uuid=8108DD352-7C9C-1045E-1887-C8B1D5672A7885803infoc; buvid4=06942070-77AF-5EEA-3ED6-74A09D5CCC6963844-023112111-; buvid_fp=9d5170f234cccf2f9c4ecf6525d559ee; rpdid=0zbfAHTjDJ|Fz1zbc3L|M9K|3w1RtFgG; PVID=1; sid=6pnte25u; b_lsid=79E8C272_18D5D279D39; bsource=search_baidu; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDY5MjQxNDIsImlhdCI6MTcwNjY2NDg4MiwicGx0IjotMX0.ST08aN1XhD0CEWr1mfX_bl01qSSSJjWnz4zh2gUll1g; bili_ticket_expires=1706924082',
    'Referer':'https://www.bilibili.com/',
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url = 'https://www.bilibili.com/video/BV14Y4y1j7s4?t=6.2&p=14'
response = requests.get(url=url,headers=headers)
html = response.text
title = re.findall('<h1 title="(.*?)" class="video-title"',html)[0]
info = re.findall('<script>window.__playinfo__=(.*?)</script>',html)[0]
json_data = json.loads(info)
video_url = json_data['data']['dash']['video'][0]['baseUrl']
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_content = requests.get(url=video_url,headers=headers).content
audio_content = requests.get(url=audio_url,headers=headers).content
with open(title + '.mp4',mode='wb') as video:
    video.write(video_content)
with open(title + '.mp3',mode='wb') as audio:
    audio.write(audio_content)
cmd = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {title}output.mp4"
subprocess.run(cmd)