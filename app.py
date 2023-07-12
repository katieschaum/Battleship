from flask import Flask, request, render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    row = db.Column(db.Integer, nullable=False)
    column = db.Column(db.Integer, nullable=False)
    is_hit = db.Column(db.Integer, default=0)

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    is_player = db.Column(db.Integer, default=0)
    size = db.Column(db.Integer, default=0)
    placement = db.Column(db.String)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.Integer, default=-1)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/startgame", methods=["POST"])
def start_game():
    return "Hello World"

@app.route("/api/makemove", methods=["POST"])
def make_move():
    return "Hello World"

@app.route("/api/login", methods=["POST"])
def login():
    return "Hello World"

@app.route("/api/createuser", methods=["POST"])
def create_user():
    username = request.json["username"]
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return user