from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PostForm

posts = Blueprint('posts', __name__)

#creating new post route
@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post(): 
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post have been created!', 'success')
        return redirect(url_for('main.home')) 
    return render_template('create_post.html', title='New Post',form=form, legend='New Post')