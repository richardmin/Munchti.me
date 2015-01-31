from flask import render_template, redirect, request
from app import app, models, db
from .forms import CreatePostForm, PostCommentForm

@app.route('/home')
def index():
	return render_template('index.html')
@app.route('/create_post', methods=['GET', 'POST'])
def create():
	form = CreatePostForm(request.form)
	if request.method == 'POST':
		post = models.Post(food = form.food.data, source = form.source.data, time = form.time.data, payment = form.payment.data, contact = form.contact.data,
			info = form.info.data, name = form.name.data)
		db.session.add(post)
		db.session.commit()
		return redirect('/home')
	return render_template('create_post.html', form = form)

