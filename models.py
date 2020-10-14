import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()


class Registers(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    project_name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
