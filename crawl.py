import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup as bs


def get_dom(url, encode='utf-8'):
    req = requests.get(url)
    req.encoding = encode
    soup = bs(req.text, 'html.parser')
    return soup


def selector(url, select, length):
    soup = get_dom(url)
    select_ls = []
    for tx in soup.select(select):
        select_ls.append(tx.text.strip())
    if len(select_ls) > length:
        while len(select_ls) != length:
            select_ls = select_ls[1:]
    return select_ls


def crawl(url, title, time, length=20):
    title_ls = selector(url, title, length)
    time_ls = selector(url, time, length)
    # address_talbe = selector(url, address)
    table = pd.DataFrame()
    table['Title'] = title_ls
    table['Time'] = time_ls
    return table