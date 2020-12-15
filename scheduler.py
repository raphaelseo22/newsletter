from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import time
import crawl
import datetime
import mail


def newsletter():
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    table = crawl.fmk_crawl()
    table2 = crawl.fashion_crawl()
    table = pd.concat([table, table2], ignore_index=True)
    mail.mail(f'{today}', table)
    print('메일이 성공적으로 보내졌습니다.')


sched = BackgroundScheduler()


sched.start()
sched.add_job(newsletter, 'cron', hour="6,14")
while True:
    # print("Running main process...............")
    time.sleep(1)


# if __name__ == '__main__':
#     newsletter()