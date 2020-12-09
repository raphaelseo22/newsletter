from apscheduler.schedulers.background import BackgroundScheduler
import time
import pandas as pd
import numpy as np
import re
import datetime
import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.text import MIMEText


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


def mail(subject, text, f_mail='raphaelseo22@gmail.com', t_mail='seodh02@gmail.com',f_pw='seraewgfcyoptwyc'):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    text = text.to_html(index=False, justify='center')
    s.login(f_mail,f_pw)
    msg = MIMEText(text, 'html', _charset="utf8")
    msg['Subject'] = subject
    #메일보내기
    s.sendmail(f_mail, t_mail, msg.as_string())
    # 세션 종료
    s.quit()


def newsletter():
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    table = crawl(url, title, time_)
    mail(f'{today}', table)
    print('메일이 성공적으로 보내졌습니다.')


url = 'https://www.fmkorea.com/index.php?mid=football_news&sort_index=pop&order_type=desc'
title = '#bd_340354_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a'
time_ = '#bd_340354_0 > div > div.fm_best_widget._bd_pc > ul > li > div > div:nth-child(5) > span.regdate'
# address = '#bd_340354_0 > div > table > tbody > tr > td.title.hotdeal_var8 > a:nth-child(1).hre'


sched = BackgroundScheduler()


sched.start()
sched.add_job(newsletter, 'interval', minutes=1)
while True:
    print("Running main process...............")
    time.sleep(60)