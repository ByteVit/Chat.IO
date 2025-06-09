from flask import session, render_template, url_for, redirect,Flask,request
import random,time
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import PasswordEncoder as pe

app = Flask(__name__)
app.config["SECRET_KEY"]="3eododlide><"
def database_import():
  from database.models import User,Message,Conversation,db
  return User,Message ,Conversation ,db
  
app.config["ICONS"]= 'static/icons'
app.config["STYLES"]='static/styles'

status = ["active", "not active"]
user_status = ""

@app.route("/")
def landing_page():
  trusted_users=10
  return render_template("landing_page.html", trusted_users=trusted_users)
  
@app.route("/login")
def login():
  return render_template('login.html')
@app.route("/signup")
def signup():
  return render_template("signup.html")
 
@app.route("/verify_login", methods=["POST", "GET"])
def verify_login():
  username = request.form.get("username")
  password = request.form.get("password")
  #checks if user exists
  user = User.query.filter_by(username=username).first()
  if user:
    session["username"]=user.username
    user_status = status[0]
    return redirect(url_for('home'))
  return render_template('login.html', error="That user does not exists!")
@app.route("/create_account", methods=["POST", "GET"])
def create_account():
  fullname = request.form.get("name")
  username = request.form.get("username")
  password = request.form.get("password")
  user = User.query.filter_by(username=username ).first()
  if user:
    return render_template("signup.html", error="That username has been taken!")
  if len(password)<6:
    return render_template("signup.html", error="Password is too short")
  encoded_passkey = pe.encode_str(password)
  new_user = User(fullname=fullname, username=username, password=password)
  db.session.add(new_user)
  time.sleep(5)
  db.session.commit()
  return render_template("signup.html", status="Your account has been created Successfully , you can now proceed to login.")

@app.route("/home")
def home():
  username = session.get("username")
  if not username or username is None:
    return "This not the page, your looking for. Check the link and try again."
  user = User.query.filter_by(username=username).first()
  chats = Conversation.query.filter_by(id=user.id).all()
  return render_template("home.html",chats=chats, user=user)
 
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=2000)