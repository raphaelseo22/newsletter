import smtplib
from email.mime.text import MIMEText
from crawl import crawl
import datetime

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


def main():
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    table = crawl(url, title, time)
    mail(f'{today}', table)
    print('메일이 성공적으로 보내졌습니다.')


url = 'https://www.fmkorea.com/football_news'
title = '#bd_340354_0 > div > table > tbody > tr > td.title.hotdeal_var8 > a:nth-child(1)'
time = '#bd_340354_0 > div > table > tbody > tr > td.time'
# address = '#bd_340354_0 > div > table > tbody > tr > td.title.hotdeal_var8 > a:nth-child(1).hre'


if __name__ == '__main__':
    main()