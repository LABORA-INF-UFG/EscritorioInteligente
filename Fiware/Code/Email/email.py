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

        self.__rasp01 = False
        self.__rasp02 = False
        self.__rasp03 = False

    def get_rasp01(self):
        return self.__rasp01

    def get_rasp02(self):
        return self.__rasp02
    
    def get_rasp03(self):
        return self.__rasp03

    def get_allRasp(self):
        if(self.__rasp01 == True and self.__rasp02 == True and self.__rasp03 == True):
            return 1
        else: 
            return 0

    def get_oneRasp(self):
        if(self.__rasp01 == True or self.__rasp02 == True or self.__rasp03 == True):
            return 1
        else: 
            return 0

    def set_rasp01(self, status):
        self.__rasp01 = status

    def set_rasp02(self, status):
        self.__rasp02 = status

    def set_rasp03(self, status):
        self.__rasp03 = status

    def set_allRasp(self):
        self.__rasp01 = False
        self.__rasp02 = False
        self.__rasp03 = False

    def send_email(self, mail_from, mail_to, mail_subject, mail_message):
        self.__server.login(self.__username, self.__password)
        self.__server.sendmail(mail_from, mail_to, mail_subject, mail_message)
        self.__server.quit()

    