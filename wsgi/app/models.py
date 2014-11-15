from app import db


class mail_message(db.Document):
	email_id=db.StringField(max_length=30,required=True)
