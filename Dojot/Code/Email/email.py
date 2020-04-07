import smtplib, yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Office import logs

class Email():
    def __init__(self):
        self.__config = yaml.load(open('./Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__smtp_ssl_host = 'smtp.gmail.com'
        self.__smtp_ssl_port = 465
        self.__server = smtplib.SMTP_SSL(self.__smtp_ssl_host, self.__smtp_ssl_port)
        self.__username = self.__config['Email']['Username_sender']
        self.__password = self.__config['Email']['Password_sender']
        self.__username_recipient = self.__config['Email']['Username_recipient']

    def send_email(self):
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.__config['Email']['Subject']
        msg.attach( MIMEText(self.__config['Email']['Message'], "plain", "utf-8" ) )
        msg = msg.as_string().encode('ascii')

        self.__server.login(self.__username, self.__password)
        self.__server.sendmail(self.__username, self.__username_recipient,msg)
        self.__server.quit()

        logs.log("INFO - E-mail enviado!")
    