from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from werkzeug.security import generate_password_hash,check_password_hash
from app import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])  
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)     

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id',ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    def saveComment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def getComment(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments
    def deleteComment(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f'Comments: {self.comment}'   

class Subscriber(UserMixin, db.Model):
   __tablename__="subscribers"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   email = db.Column(db.String(255),unique = True,index = True)
   def save_subscriber(self):
       db.session.add(self)
       db.session.commit()
   @classmethod
   def get_subscribers(cls,id):
       return Subscriber.query.all()
   def __repr__(self):
       return f'User {self.email}'                   