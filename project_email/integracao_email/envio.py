
import smtplib
from email.mime.text import MIMEText

servidor = "smtp.gmail.com"
email_de = "a.pissulin@gmail.com"
senha = "ueithi2012"
porta_SMTP1 = 465
porta_SMTP2 = 587

email_para = "a.pissulin@outlook.com"
email_assunto = "Email teste chegou!!!"
email_corpo = """Email teste para ver se tudo esta funcionando corretamente e poder
usar para a nossa aplicação web da OPE"""
 
msg = MIMEText(email_corpo)
msg["Subject"] = email_assunto
msg["From"] = email_de
msg["To"] = email_para


smtp =smtplib.server(servidor)
smtp = smtplib.SMTP_SSL_PORT(porta_SMTP1)
smtp.login(email_de, senha)

smtp.sendmail(msg["From"], msg["To"], msg.as_string())

