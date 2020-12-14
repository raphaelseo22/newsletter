import smtplib
from email.mime.text import MIMEText

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
