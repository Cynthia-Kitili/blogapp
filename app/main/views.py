from flask import render_template, request, Blueprint,redirect,url_for,flash
from app.models import Post
from flask_login import login_user,logout_user,login_required,current_user
from .forms import SubscriberForm, CommentForm
from ..models import Subscriber,Comment
from ..requests import getQuotes
from .import main
# from .forms import PitchForm,CommentForm,updateProfile
# from ..models import Blog,Comment,User

main = Blueprint('main', __name__)

#Home function
@main.route("/")
@main.route("/home", methods= ['GET'])
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5)
    getquotes = getQuotes()
    return render_template('home.html', posts=posts, getquotes=getquotes)

    
    
@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def newComment(id):
    posts = Post.query.filter_by(id = id).all()
    postComments = Comment.query.filter_by(post_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = comment(post_id=id, comment=comment, user=current_user)
        new_comment.saveComment()
        db.session.commit()
    return render_template('comment.html', posts=posts, post_comments=postComments, comment_form=comment_form)

# @main.route('/home',methods = ['GET'])
# def home():
#     getquotes = getQuotes()
#     return render_template ('home.html',getquotes = getquotes)    

@main.route('/subscribe', methods=['GET','POST'])
def subscriber():
    getquotes = getQuotes()
    subscriber_form=SubscriberForm()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,name = subscriber_form.name.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Welcome to this wonderful application","email/subscriber",subscriber.email,subscriber=subscriber)
        title= "Blog Application"
        return render_template('index.html',title=title, posts=posts, getquotes = getquotes)
    subscriber = Post.query.all()
    post = Post.query.all()
    return render_template('subscribe.html',subscriber=subscriber,subscriber_form=subscriber_form,posts=posts) 



@main.route("/about")
def about():
    return render_template('about.html', title='About')
