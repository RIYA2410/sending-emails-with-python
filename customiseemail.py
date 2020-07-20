import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('.\html\index.html').read_text())
email=EmailMessage()
email['from']='Riya Jain'
email['to']='riyajainangel675@gmail.com'
email['subject']='Python Programming'

email.set_content(html.substitute(name = 'tintin'))

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('riyajainangel675@gmail.com','jainriya2557')
	smtp.send_message(email)
	print('email sent')
