import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendEmail(Qemail,subject,query):
    sender_email_address = 'patelg.hima@gmail.com'
    sender_email_password = 'Hima2020!'
    receiver_email_address = Qemail

    email_subject_line = subject

    msg = MIMEMultipart()
    msg['From'] = sender_email_address
    msg['To'] = receiver_email_address
    msg['Subject'] = email_subject_line
    email_body =  query + '\n'
    msg.attach(MIMEText(email_body, 'plain'))

    email_content = msg.as_string()
    server = smtplib.SMTP()
    #server.connect('smtp.gmail.com', '587')
    server._host = 'smtp.gmail.com'
    server.connect('smtp.gmail.com', '587')
    server.starttls()
    server.login(sender_email_address, sender_email_password)
    server.sendmail('Raj', receiver_email_address, email_content)
    server.quit()