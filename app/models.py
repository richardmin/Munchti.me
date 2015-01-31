from app import db
from datetime import datetime

class Post(db.Model):
	id 			= db.Column(db.Integer, primary_key=True)
	food 		= db.Column(db.String(255))
	source 		= db.Column(db.String(255))
	destination = db.Column(db.String(255))
	time 		= db.Column(db.DateTime)
	payment 	= db.Column(db.Integer)
	contact 	= db.Column(db.String(255))  
	info 		= db.Column(db.String(255))
	name 		= db.Column(db.String(255))

class Comment(db.Model):
 	id			= db.Column(db.String(255), primary_key=True)
 	post_id		= db.Column(db.Integer)
 	text		= db.Column(db.String(255))
 	