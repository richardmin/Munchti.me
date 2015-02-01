import os
from flask import Flask
from flask.ext.restful import Api
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
#import models
from apscheduler.scheduler import Scheduler

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)






db.create_all()
api_manager = APIManager(app, flask_sqlalchemy_db=db)
#def delete_entry(t):
#	post = models.Post.query(datetime).filter(t).delete(synchronize_session='fetch')
#	db.session.commit()

s = Scheduler()
s.start()

from app import views, models

