import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as bs


def get_dom(url, encode):
    req = requests.get(url)
    if encode != None:
        req.encoding = encode
    soup = bs(req.text, 'html.parser')
    return soup


def selector(url, select, length=20, address=False, sub=None, site=None, encode=None):
    soup = get_dom(url, encode)
    select_ls = []
    if address == False:
        for tx in soup.select(select):
            if sub != True:
                t = tx.text.strip()
                t = re.sub(f"{sub}","",t)
                select_ls.append(t)
            else:
                t = tx.text.strip()
                select_ls.append(t)
    else:
        for tx in soup.select(select):
            select_ls.append(f"{site}/{tx['href']}")
    if len(select_ls) > length:
        while len(select_ls) != length:
            select_ls = select_ls[1:]
    return select_ls



def crawl(url, title=None, time_=None, address="title",site=None, category=None, encode=None, sub=None):
    if title != None:
        title_ls = selector(url, title, encode=encode, sub=sub)
    if time_ != None:
        time_ls = selector(url, time_, encode=encode)
    if address != None:
        if address == "title":
            address = title
        address_ls = selector(url, address, address=address, site=site, encode=encode)
    table = pd.DataFrame()
    table['Title'] = title_ls
    table['Time'] = time_ls
    table['URL'] = address_ls
    table.insert(0, 'Category', category)
    return table
