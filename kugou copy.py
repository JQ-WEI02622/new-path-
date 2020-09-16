import requests
from bs4 import BeautifulSoup
import time


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"}
##加入请求头， 模拟浏览器获取页面信息


def get_info(url):
    wb_data = requests.get(url, headers =headers) #获取信息
    soup = BeautifulSoup(wb_data.text, 'lxml') #解析/结构化信息，使其日后方便过滤/提取
    ranks = soup.select('span.pc_temp_num') #锁定歌曲排名在网页中的具体位置
    titles = soup.select('div.pc_temp_songlist > ul > li > a') #锁定歌曲名字在网页中对应的位置
    times = soup.select('span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            "rank": rank.get_text().strip(),
            "singer":title.get_text().split('-')[0],
            "song": title.get_text().split('-')[1],

            "time": time.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
    time.sleep(1)  #time's sleep library can help to halt the programme one second each time the programme runs, this can prevent request rate going too quick and fails to scrap.














