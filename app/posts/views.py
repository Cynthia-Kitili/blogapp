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
        flash('Post Created Successfully!', 'success')
        return redirect(url_for('main.home')) 
    return render_template('create_post.html', title='New Post',form=form, legend='New Post')

# @posts.route('/post/<int:post_id>', methods = ['POST','GET'])
# @login_required
# def comment(post_id):
#     form = CommentForm()
#     post = Post.query.get(post_id)
#     all_comments = Comment.query.filter_by(post_id = post_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data 
#         post_id = post_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(comment = comment,user_id = user_id,post_id = pitch_id)
#         new_comment.save_c()
#         return redirect(url_for('.comment', post_id = post_id))
#     return render_template('comment.html', form =form, post = post,all_comments=all_comments)    

@posts.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def newComment(id):
    post = post.query.filter_by(id = id).all()
    postComments = Comment.query.filter_by(post_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(post_id=id, comment=comment, user=current_user)
        new_comment.saveComment()
    return render_template('comment.html', post=post, post_comments=postComments, comment_form=comment_form)
#creating a post function 
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

#updating a post function
@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':    
        form.title.data = post.title
        form.content.data = post.content 
    return render_template('create_post.html', title='Update Post',form=form, legend='Update Post')   

#Deleting a post function
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted Succesfully!' "success")
    return redirect(url_for('main.home')) 