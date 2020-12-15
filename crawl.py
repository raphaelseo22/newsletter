import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs


def get_dom(url, encode='utf-8'):
    req = requests.get(url)
    req.encoding = encode
    soup = bs(req.text, 'html.parser')
    return soup


def selector(url, select, length, address=False):
    soup = get_dom(url)
    select_ls = []
    if address == False:
        for tx in soup.select(select):
            select_ls.append(tx.text.strip())
    else:
        for tx in soup.select(select):
            select_ls.append(f"https://www.fmkorea.com/{tx['href']}")
    if len(select_ls) > length:
        while len(select_ls) != length:
            select_ls = select_ls[1:]
    return select_ls



def fmk_crawl(length=20):
    url = 'https://www.fmkorea.com/index.php?mid=football_news&sort_index=pop&order_type=desc'
    title = '#bd_340354_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a'
    time_ = '#bd_340354_0 > div > div.fm_best_widget._bd_pc > ul > li > div > div:nth-child(5) > span.regdate'
    title_ls = selector(url, title, length)
    time_ls = selector(url, time_, length)
    address_ls = selector(url, title, length, address=True)
    table = pd.DataFrame()
    table['Title'] = title_ls
    table['Time'] = time_ls
    table['URL'] = address_ls
    table.insert(0, 'Category', 'News')
    return table



def fashion_crawl(length=20):
    url = 'https://www.fmkorea.com/index.php?mid=fashion&sort_index=pop&order_type=desc'
    title = '#bd_4477817_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a'
    time_ = '#bd_4477817_0 > div > div.fm_best_widget._bd_pc > ul > li > div > div:nth-child(5) > span.regdate'
    title_ls = selector(url, title, length)
    time_ls = selector(url, time_, length)
    address_ls = selector(url, title, length, address=True)
    table = pd.DataFrame()
    table['Title'] = title_ls
    table['Time'] = time_ls
    table['URL'] = address_ls
    table.insert(0, 'Category', 'Fashion')
    return table