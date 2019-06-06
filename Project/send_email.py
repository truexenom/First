#!/usr/bin/python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys,os


#def email(email_recipients, email_subject, email_sender, email_body, email_attachment, email_server, email_port):
def email():
    from config_parser import config
    email_recipients= config.get("EMAIL", "email_recipients")
    email_logfile= config.get("EMAIL", "email_logfile")
    email_subject= config.get("EMAIL", "email_subject")
    email_sender= config.get("EMAIL", "email_sender")
    email_body= config.get("EMAIL", "email_body")
    email_attachment = (os.path.dirname(sys.argv[0])+"/"+email_logfile)
    email_server= config.get("EMAIL", "email_server")
    email_port= int(config.get("EMAIL", "email_port"))
    recipients = [email_recipients]
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = email_subject
    msg['From'] = email_sender
    msg['Reply-to'] = email_sender

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText(email_body)
    msg.attach(part)

    part = MIMEApplication(open(email_attachment).read())
    part.add_header('Content-Disposition', 'attachment', filename=email_attachment)
    msg.attach(part)

    #server  = smtplib.SMTP_SSL("smtp.llnw.com:465")
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP(email_server, email_port)
    #server.connect("mail.llnw.com",587)
    #server.ehlo("llnw.com")
    server.starttls()
    #server.ehlo("llnw.com")
    #server.login("smc-autoreport@llnw.com", "PASS")

    server.sendmail(msg['From'], emaillist , msg.as_string())
    server.quit()