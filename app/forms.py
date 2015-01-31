from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import DateTimeField
from wtforms import IntegerField
from datetime import datetime


class CreatePostForm(Form):
	food 		= StringField('food')
	source 		= StringField('location')
	destination = StringField('destination')
	time 		= DateTimeField('time')
	payment 	= IntegerField('payment')
	contact 	= StringField('contact info')
	info 		= StringField('additional info')
	name 		= StringField('name')

class PostCommentForm(Form):
	text 		= StringField('comment')