
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validations


db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='users', lazy=True)
    followers = db.relationship('Followers', foreign_keys='Followers.follower_id', backref='users')
    following = db.relationship('Followers', foreign_keys='Followers.following_id', backref='users')


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

class Followers(db.Model):
    __tablename__='followers'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    following_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
