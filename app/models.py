from app import db, api_manager
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


api_manager.create_api(Post, methods=['GET', 'POST', 'DELETE', 'PUT'])