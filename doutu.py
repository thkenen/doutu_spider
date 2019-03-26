#coding=utf-8
'''
[小试牛刀]爬取斗图网的图片
'''
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import time
def get_page(url):
    '''获取页面soup'''
    request_heads={
    'authority': 'www.doutula.com',
    'method': 'GET',
    'path':'/',
    'scheme': 'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d87014a95c888749a0e7e3558aa029e391542875442; UM_distinctid=1673a8af4ec947-0fe5c7933d2931-4313362-144000-1673a8af4ed561; _ga=GA1.2.997708735.1542875444; _gid=GA1.2.289917732.1542875445; yjs_id=c5141fe916285e06748acc082e344c44; ctrl_time=1; CNZZDATA1256911977=719530834-1542871248-null%7C1542882055; XSRF-TOKEN=eyJpdiI6Ilc3N1wvUGdhXC8rcWZVdXY4R1U1UUxIQT09IiwidmFsdWUiOiI3SGNZbk1Ic3ZYWVNHY045ZFNYakxiM21KMnU2bHdmN2ZkQVl0MFwvejJyalpkSnI1dG9XNzlldVN1aHFtTlA4dSIsIm1hYyI6IjQzMmY0NGI2Y2QxNjFmYWRkYWNkYjM3ODc4ZmYyNzJlNTcyY2U4MzgzYWMxMzUwNTExMDA4MzVmYTQxMDE4MzAifQ%3D%3D; doutula_session=eyJpdiI6IklJWldMQ2d3Q2s5cm9hdXlOcWJhZWc9PSIsInZhbHVlIjoiS1B3OHNNXC9XQmRCeVpJcDZqc1puU3pjbXZyaEVhUFBsOVdlN0o2aGo5MEk5Q3ZUNlRLVUltQk54OE9Malg5aU8iLCJtYWMiOiJmNDE4NDVlNjVkNzkwMmE0NGIzM2E0NTU1NmExYTdhMTY0YjJmNTFiNDM3Mzg5ZTc3ZmExMTczMDBlNmI5MzQ2In0%3D',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    response=requests.get(url,headers=request_heads)#伪造请求头信息
    print(response.status_code)
    html = BeautifulSoup(response.text,'html.parser')
    return html
#print html.prettify().encode('GBK','ignore')
'''爬去网站表情包'''
def get_pic_url(html):
    '''获取页面中图片地址'''
    #第一栏部分div标签下
    pic_divs=html.select('div[class="col-xs-6 col-sm-3"]')
    picUrl=[]
    for pic_div in pic_divs:
        pic_url=pic_div.select('img[class="lazy image_dtb img-responsive"]')[0]["data-original"]
        if pic_url[-1]=="g":
            picUrl.append((pic_url,'jpg'))
        elif pic_url[-1]=="f":
            picUrl.append((pic_url,'gif'))
    #第二栏部分a标签下
    pic_as=html.select('a[class="col-xs-6 col-sm-3"]')
    for pic_a in pic_as:
        pic_url=pic_a.select('img[class="img-responsive lazy image_dta"]')[0]["data-original"]
        if pic_url[-1]=="g":
            picUrl.append((pic_url,'jpg'))
        elif pic_url[-1]=="f":
            picUrl.append((pic_url,'gif'))
    return picUrl
def get_pic(picUrl,i):
    '''下载图片'''
    j=0
    for picUrlx in picUrl:
        if picUrlx[1] == 'jpg':
            urlretrieve(picUrlx[0],filename="C:\\Users\\kennethwei\\Desktop\\image\\%s%s.jpg"%(str(i),str(j)))
            #使用urllib的方法来保存图片
            print("downloding...%s"%picUrlx[0])
        elif picUrlx[1] == 'gif':
            urlretrieve(picUrlx[0],filename="C:\\Users\\kennethwei\\Desktop\\image\\%s%s.gif"%(str(i),str(j)))
            print("downloding...%s"%picUrlx[0])
        j+=1
        time.sleep(5)
    return 0
def turn_page(url,i):
    '''翻页爬取'''
    url2=''.join([url,"/article/list/?page=%s"%str(i)])
    return url2

    
def main():
    '''main就是main啊'''
    i=1#页数
    url2='http://www.doutula.com/'
    while i <= 3:
        html=get_page(url2)
        url2=turn_page(url2,i)
        picUrl=get_pic_url(html)
        get_pic(picUrl,i)
        i+=1
        

        
main()