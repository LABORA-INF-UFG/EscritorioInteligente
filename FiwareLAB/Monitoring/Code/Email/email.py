import smtplib, yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Office import logs

class Email(object):
    def __init__(self):
        self.__config = yaml.load(open('../Scripts/config.yaml', 'r'))
        self.__msg = None
        self.__smtp_ssl_host = 'smtp.gmail.com'
        self.__smtp_ssl_port = 465
        self.__server = smtplib.SMTP_SSL(self.__smtp_ssl_host, self.__smtp_ssl_port)
        self.__username = self.__config['email']['email_sender']
        self.__password = self.__config['email']['password_sender']
        self.__username_recipient = self.__config['email']['email_receiver']

    def send_email(self, subject, message):
        
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg.attach( MIMEText(message, "plain", "utf-8" ) )
            msg = msg.as_string().encode('ascii')

            self.__server.login(self.__username, self.__password)
            self.__server.sendmail(self.__username, self.__username_recipient,msg)
            self.__server.quit()
            logs.log("INFO - E-mail enviado!")
        except Exception as e:
            logs.log("ERROR - E-mail não enviado! {}".format(e))

    