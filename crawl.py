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


def selector(url, category, select):
    soup = get_dom(url)
    select_ls = []
    for ti in soup.select(select):
        select_ls.append(ti.text.strip())
    table = pd.DataFrame()
    if len(select_ls) > 20:
        select_ls = select_ls[3:]
    table[f'{category}'] = select_ls
    return table


def crawl(url, title, time):
    title_table = selector(url, 'title',title)
    time_talbe = selector(url, 'time',time)
    # address_talbe = selector(url, address)
    total = pd.concat([title_table, time_talbe], ignore_index=True)
    return total