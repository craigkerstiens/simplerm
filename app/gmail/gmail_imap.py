import imaplib, sys
from smtplib import  SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)        
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


import gmail_mailboxes, gmail_messages, gmail_message

class gmail_imap:

    def __init__ (self, host, key):
        self.imap_server = imaplib.IMAP4_SSL(host)
        self.key = key
        self.username = "craig.kerstiens@gmail.com"
        self.loggedIn = False
        
        self.mailboxes = gmail_mailboxes.gmail_mailboxes(self)
        self.messages = gmail_messages.gmail_messages(self)
        
    def login (self):
        self.imap_server.authenticate('XOAUTH', lambda x: self.key)
        #self.imap_server.login(self.username,self.password)
        self.loggedIn = True
    
    def logout (self):
        self.imap_server.close()
        #self.imap_server.logout()
        self.loggedIn = False
                                

    def sendmail(self, destination, subject, message, attach = None):        
        try:
            msg = MIMEMultipart()

            msg['From'] = self.username
            msg['Reply-to'] = self.username
            msg['To'] = destination
            msg['Subject'] = subject

            msg.attach(MIMEText(message))

            if attach:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(attach, 'rb').read())
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                'attachment; filename="%s"' % os.path.basename(attach))
                msg.attach(part)

            mailServer = SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            try:
                mailServer.login(self.username, self.password)
                mailServer.sendmail(self.username, destination, msg.as_string())
            finally:
                mailServer.close()
        except Exception, exc:
            sys.exit("Failed to send mail; %s" % str(exc))
            
def get_messages(host, key):
    import getpass

    gmail = gmail_imap(host, key)
    
    gmail.mailboxes.load()
    print gmail.mailboxes
    
    gmail.messages.process("INBOX")
    print gmail.messages
  
    for msg in gmail.messages[0:2]:
      message = gmail.messages.getMessage(msg.uid)
      print message.uid
      print message.From
    
    gmail.logout()
