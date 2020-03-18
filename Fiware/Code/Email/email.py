import smtplib, yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        self.__nodes = []
        print(self.__config['Nodes'])
        for x in self.__config['Nodes']:
            node = {'ID': x['ID'], 'Status': False}
            self.__nodes.append(node)

    def get_nodes(self):
        return self.__nodes

    def get_allNodes(self):
        for node in self.__nodes:
            if not node['Status']:
                return 0
        print(self.__nodes)
        return 1

    def get_oneNode(self):
        for node in self.__nodes:
            if node['Status']:
                return 1
        return 0

    def set_node(self, status, index):
        self.__nodes[index]['Status'] = status

    def set_allNodes(self):
        for x in range(len(self.__nodes)):
            self.__nodes[x]['Status'] = False
        #print(self.__nodes)

    def send_email(self):
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.__config['Email']['Subject']
        msg.attach( MIMEText(self.__config['Email']['Message'], "plain", "utf-8" ) )
        msg = msg.as_string().encode('ascii')

        self.__server.login(self.__username, self.__password)
        self.__server.sendmail(self.__username, self.__username_recipient,msg)
        self.__server.quit()
    