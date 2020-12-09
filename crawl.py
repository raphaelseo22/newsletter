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


def selector(url, select):
    soup = get_dom(url)
    select_ls = []
    for ti in soup.select(select):
        select_ls.append(ti.text.strip())
    if len(select_ls) > 20:
        while len(select_ls) != 20:
            select_ls = select_ls[1:]
    return select_ls


def crawl(url, title, time):
    title_ls = selector(url, title)
    time_ls = selector(url, time)
    # address_talbe = selector(url, address)
    table = pd.DataFrame()
    table['Title'] = title_ls
    table['Time'] = time_ls
    return table