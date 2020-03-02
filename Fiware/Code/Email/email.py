import smtplib
from email.mime.text import MIMEText

class Email():
    def __init__(self):
        self.__msg = None
        self.__smtp_ssl_host = 'smtp.gmail.com'
        self.__smtp_ssl_port = 465
        self.__server = smtplib.SMTP_SSL(self.__smtp_ssl_host, self.__smtp_ssl_port)
        self.__username = 'escritoriointeligente123@gmail.com'
        self.__password =  'fran123.'

    def send_email(self, mail_from, mail_to, mail_subject, mail_message):
        self.__server.login(self.__username, self.__password)
        self.__server.sendmail(mail_from, mail_to, mail_subject, mail_message)
        self.__server.quit()

