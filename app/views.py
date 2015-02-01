from flask import render_template, redirect, request
from app import app, models, db, s, api_manager
from models import Post
from .forms import CreatePostForm, PostCommentForm
import sched, time, json
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
	posts = models.Post.query.all()
	return render_template('index.html', posts=posts)


#@app.route('/home', methods=['GET', 'POST'])
#def create():
#	form = CreatePostForm(request.form)
#	if request.method == 'POST':
#		post = models.Post(food = form.food.data, source = form.source.data, time = form.time.data, payment = form.payment.data, contact = form.contact.data,
#			info = form.info.data, name = form.name.data)
#		db.session.add(post)
#		db.session.commit()
##		s.enterabs(delete_entry, form.time.data, form.time.data)
#		return redirect('/home')
#	return render_template('home.html', form = form)

@app.route('/static/stylesheets/style.css')
def display():
    return app.send_static_file('style.css')

###########################
####### RESTful API #######
###########################

