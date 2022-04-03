from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ User Profile """

    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

