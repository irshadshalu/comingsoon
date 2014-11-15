from flask import Flask 
from flask.ext.mongoengine import MongoEngine
from flask_mail import Mail
app=Flask(__name__)
mail=Mail(app)

app.config['MONGODB_SETTINGS']={'db':os.environ['OPENSHIFT_APP_NAME'],'username':os.environ['OPENSHIFT_MONGODB_DB_USERNAME'],'password':os.environ['OPENSHIT_MONGODB_DB_PASSWORD'],'host':os.environ['OPENSHIFT_MONGODB_DB_HOST'],'port':os.environ['OPENSHIFT_MONGODB_DB_PORT']}
db=MongoEngine(app)

def register_mail(app):
	from app.views import email
	app.register_blueprint(email)

register_mail(app)
'''
class Email(db.Document):
	email=db.StringField(min_length=5)
'''


