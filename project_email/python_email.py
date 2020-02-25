# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests
import smtplib


 
# create message object instance
msg = MIMEMultipart()
 
 
message = """Este email é para testar se tudo esta okay,
então se tudo der certo , vc receberá esta mesangem.
ATT,

""" 
# setup the parameters of the message
password = os.environ['MANDRILL_PASSWORD']
msg['From'] = os.environ['MANDRILL_USERNAME']
msg['To'] = "a.pissulin@gmail.com"
msg['Subject'] = "email teste"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email para %s:" % (msg['To']))