
from flask import render_template,request,redirect,url_for

from flask import Blueprint
from models import mail_message
from flask.ext.mail import Message
from app import mail
from config import ADMINS

email=Blueprint('mail',__name__,url_prefix='/')

@email.route('/')
@email.route('/index')
def index():
	return render_template('base.html')

'''
def sent_email(subject,sender,recipients,text_body,html_body):
        msg=Message(subject,sender=sender,recipients=recipients)
        msg.body=text_body
        msg.html=html_body
        msg.send(msg)
'''
@email.route('/',methods=['POST'])
def get_data():
	t=request.form['email']
	if t.find('@') !=-1:
		p=mail_message()
		p.email_id=t
		p.save()
	#	sent_email("Welcome To HoistMe",ADMINS[0],t,render_template("sent_main.txt"),render_template("sent_mail.html") )
		return "Thank You. We will keep in touch"
	return "Sorry you have typed an invalid Email Address"

@email.route('mail')
def get_mail():
	y=mail_message.objects.all()
	return render_template('mail.html',y=y)


'''
def sent_email(subject,sender,recepients,text_body,html_body):
	msg=Message(subject,sender=sender,recipients=recipients)
	msg.body=text_body
	msg.html=html_body
	msg.send(msg)
		
'''
