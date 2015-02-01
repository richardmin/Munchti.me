import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from apscheduler.scheduler import Scheduler

def delete_entry(t):
	post = models.Post.query(datetime).filter(t).delete(synchronize_session='fetch')
	db.session.commit()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

s = Scheduler()
s.start()

from app import views, models

