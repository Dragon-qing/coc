import os
import requests
import random
import ddddocr
from datetime import datetime


def spider():
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Host': 'www.aiwancoc.com',
        'Referer': 'http://www.aiwancoc.com/'
    }

    url = "http://www.aiwancoc.com/php/yzmjpeg55659.php"
    for i in range(10):
        session.params = {
            "t": random.random()
        }
        response = session.get(url)
        with open("./yzm_{}.png".format(i), "wb") as p:
            p.write(response.content)
    res1 = session.get("http://www.aiwancoc.com/php/qdmtime.php")
    return res1.text


deadTime = datetime.strptime(spider(), " %Y/%m/%d %H:%M:%S")

ocr = ddddocr.DdddOcr(use_gpu=True)
re_list = []
for i in range(10):
    with open("./yzm_{}.png".format(i), "rb") as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    re_list.append(res)

dic = {}
for i in re_list:
    dic[i] = dic.get(i, 0)+1

print(f"验证码为{max(dic, key=dic.get)}")
nowTime = datetime.today()
dec = deadTime - nowTime
seconds = dec.seconds
h = seconds//3600
m = (seconds - h*3600)//60
s = seconds % 60
print(f"有效时间剩余：{h}小时,{m}分钟,{s}秒")
os.system("pause")
