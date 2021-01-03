from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import time
import crawl
import datetime
import mail
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')



fmk_news = crawl.crawl(url=cfg["fmk_news"]["url"], title=cfg["fmk_news"]["title"],
                       time_=cfg["fmk_news"]["time_"], site=cfg["fmk_news"]["site"],
                       category="News", sub="\[[0-9]{1,4}\]")
fmk_fashion = crawl.crawl(url=cfg["fmk_fashion"]["url"], title=cfg["fmk_fashion"]["title"],
                          time_=cfg["fmk_fashion"]["time_"], site=cfg["fmk_fashion"]["site"],
                          category="Fashion", sub="\[[0-9]{1,4}\]")
naver_finance_news = crawl.crawl(url=cfg["naver_finance_news"]["url"],
                                 title=cfg["naver_finance_news"]["title"],
                                 time_=cfg["naver_finance_news"]["time_"],
                                 site=cfg["naver_finance_news"]["site"],
                                 address=cfg["naver_finance_news"]["address"],
                                 category="Finance", sub="\n[\s\S]*")

table_ls = [fmk_news, fmk_fashion, naver_finance_news]




def newsletter(table_ls):
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    table = pd.concat(table_ls, ignore_index=True)
    mail.mail(f'{today}', table)
    print('메일이 성공적으로 보내졌습니다.')

#
sched = BackgroundScheduler()


sched.start()
sched.add_job(newsletter(table_ls), 'cron', hour="7,17")
# sched.add_job(newsletter(table_ls), "interval", hours=14, minutes=20)
while True:
    # print("Running main process...............")
    time.sleep(1)


# if __name__ == '__main__':
#     newsletter(table_ls)
