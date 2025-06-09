from main import app
from datetime import datetime
from flask_SQLAlchemy import SQLAlchemy

db = SQLAlchemy()

#databbase models
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(120), unique=True)
  username = db.Column(db.String(60), unique=True)
  email = db.Column(db.String(120), unique=True)
  phone_no = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(120))
  status = db.Column(db.Integer,default=0)
  chats = db.relationship("Chat", backref="user", lazy=True)
  
class Message(db.Model):
  __tablename__ = "messages"
  id = db.Column(db.Integer, primary_key=True)
  conversation_id = db.Column(db.ForeignKey("conversation.id"))
  sender_id = db.Column(db.ForeignKey('users.id'))
  content = db.Column(db.Text)
  unique_id = db.Column(db.ForeignKey('users.id'))
  
class Conversation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  message = db.relationship("Message", backref="conversation", lazy=True