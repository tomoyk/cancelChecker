#!/usr/bin/env python

import sys
import re
import urllib.request as web
import json
from datetime import datetime as dt
from bs4 import BeautifulSoup

# Get web-page from DEST_URL
# Return canceled-lecture-data by dict in list
def fetch_page(DEST_URL):
    try:
        html = web.urlopen(DEST_URL).read()
    except Exception as e:
        print(e)
        sys.exit(1)

    # Analysis HTML
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('tbody', class_='search_result')

    def delSymbol(str):
        return re.sub(r'(\t|\n)', '', str)

    # Modify data & Store dict
    tmp = []
    for tbl in tables:
        # print(tbl)
        td = tbl.select("td")

        lec_date = delSymbol(td[0].string).split()
        lec_day  = dt.strptime(lec_date[0], '%Y年%m月%d日')
        lec_day_iso = lec_day.strftime('%Y-%m-%d'),
        lec_time = lec_date[1][0]
        
        update_date = dt.strptime(td[7].string, '%Y年%m月%d日%H時%M分')
        update_date_iso = update_date.strftime('%Y-%m-%dT%H:%M:00')

        tmp.append({
            'day':     lec_day_iso[0],
            'time':    lec_time,
            'course':  td[1].string,
            'teacher': td[2].string,
            'dept':    delSymbol(td[3].string).split(', '),
            'grade':   td[4].string,
            'class':   td[5].string,
            'misc':    td[6].string,
            'update':  update_date_iso
        })
    
    if( len(tmp) > 0 ):
        return tmp
    else:
        return False

# Get web-page loop
# Return concatenated cancel-updates by dict in list
def get_updates(BASE_URL):
    cancelled_lecture = []
    label = 1

    while(True):
        stream = fetch_page(DEST_URL= BASE_URL + str(label))
        if(False == stream):
            break
        else:
            cancelled_lecture.extend(stream)
            label+=1

    return cancelled_lecture


if __name__ == '__main__':
    
    posts = get_updates(BASE_URL='https://inside.teu.ac.jp/hachiouji/hachioji_common/cancel/page/')

    # Debug
    for i in posts:
        print(i)
    
'''
SampleData
----------
2018年04月25日
1時限
キャリアデザインI
稲葉　竹俊

応用生物学部
2年次
BS1
7月25日（水）実施予定
2018年03月14日11時50分
None
----------
'''
