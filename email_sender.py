import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Riya Jain'
email['to']='riya.tca1809040@tmu.ac.in'
email['subject']='Python Programming'

email.set_content('I am learning Python')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('riyajainangel675@gmail.com','jainriya2557')
	smtp.send_message(email)
	print('email sent')
