import smtplib
from email.mime.text import MIMEText

class Email():
    def __init__(self):
        #self.__mail_from = 'franciellysouza020@gmail.com'
        self.__msg = None
        self.__smtp_ssl_host = 'smtp.gmail.com'
        self.__smtp_ssl_port = 465
        self.__server = smtplib.SMTP_SSL(self.__smtp_ssl_host, self.__smtp_ssl_port)
        self.__username = 'franciellysouza020@gmail.com'
        self.__password =  'f91348509.'

    def send_email(self, mail_from, mail_to, mail_subject, mail_message):
        self.__server.login(self.__username, self.__password)
        self.__server.sendmail(mail_from, mail_to, mail_subject, mail_message)
        self.__server.quit()

if __name__ == "__main__":
    mail = Email()
    print("oi")
    mail.send_email('franciellysouza020@gmail.com', 'franciellysouza552@gmail.com', 'teste ', 'oi')
