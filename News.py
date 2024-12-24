from bs4 import BeautifulSoup
import time, datetime, requests  #yagmail
import pandas as pd

today = time.strftime("%Y%m%d", time.localtime())
time_now = time.strftime('%H%M', time.localtime())
yest = datetime.datetime.now() + datetime.timedelta(days=-1)
yesterday = datetime.datetime.strftime(yest, "%Y%m%d")
day = today

if int(time_now) < 1930:
    today = yesterday

xwlb_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "cna=S3DuFrH93AcCAXj0c2lwtQfH; vjlast=1599648730.1599648730.30; vjuids=-3e1fb7b49.174727e89e0.0.68f7da356d02a; HMF_CI=6b268523bfcfc15a9eaa540a1064dfc4e39734c1c23535dce2072c17b7154535d84f57ae073d77d6bc48622ba036d9c1fd37a2ee6acceecce0e36e5bf19a3f4b81; HMY_JC=2115826dcae16460faa058fca7c9fa3992fcbf0f17e645dd25a15ab9ce3f2076db,; HBB_HC=64a20e4077788f4538777d67241f3c3837e20f2165abb18d4ab0e3c38a71412064; sca=80a3adbc; atpsida=6a8b23f029149068e4137cc6_1705310098_4",
    #"DNT": "1",
    "Host": "tv.cctv.com",
    'Referer':'https://tv.cctv.com/lm/xwlb/index.shtml',
    #"If-Modified-Since": "Sun, 16 Aug 2020 21:50:30 GMT",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

def find_title(day):
    xwlb_url = 'https://tv.cctv.com/lm/xwlb/day/{}.shtml'.format(day)
    r = requests.get(url=xwlb_url, headers=xwlb_headers)
    if r.status_code == 200:
        print("请求成功")
    else:
        print("请求失败，状态码:", r.status_code)
    str1 = r.text
    str1 = str1.encode('raw_unicode_escape').decode()
    soup = BeautifulSoup(str1, 'html.parser')
    news = []
    a_tags = soup.find_all('a')
    for tag in a_tags:
        #print(tag)
        tag_title = tag['title']
        #tag_title.split()
        news.append(tag_title)
        #print(tag_title)
        tag_title = list(tag_title)
    news = pd.DataFrame(news)
    news = news.drop_duplicates()
    #print(news)
    #news = news.replace('[视频]', '')
    return(news)
