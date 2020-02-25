 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

try:
		msgFrom = 'a.pissulin@gmail.com'
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		msgTo = os.environ['MANDRILL_USERNAME']
		toPass = os.environ['MANDRILL_PASSWORD']
		smtpObj.login(msgTo, toPass)
		msg = '''
		Mensagem do E-mail
		'''
		smtpObj.sendmail(msgTo,msgFrom,'Subject: Titulo do email\n{}'.format(msg))
		smtpObj.quit()
		print("Email enviado com sucesso!")
except:
		print("Erro ao enviar e-mail")