# we're basically saying that from this package, import db. it works because we have the init file
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    todos = db.relationship('Todo')
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    title = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # we are referencing the user class but in sql its all lowercase



 
    # we've set up the database,but now we have to create it -> init file

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean, default =False)
