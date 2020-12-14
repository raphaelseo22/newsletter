from apscheduler.schedulers.background import BackgroundScheduler
import time
import crawl
import datetime
import mail


def newsletter():
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    table = crawl.fmk_crawl()
    mail.mail(f'{today}', table)
    print('메일이 성공적으로 보내졌습니다.')


# sched = BackgroundScheduler()
#
#
# sched.start()
# sched.add_job(newsletter, 'cron', hour="12,18")
# while True:
#     # print("Running main process...............")
#     time.sleep(1)


if __name__ == '__main__' :
    newsletter()