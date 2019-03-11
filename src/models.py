from flask_sqlalchemy import SQLAlchemy
# import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Job(db.Model):
    """ USER, CLIENT, DATE ASSIGNED, DATE DUE, HOURS-WORKED, JOB-TYPE, COMPANY, RATE, AMOUNT DUE, COMPLETED?"""
    # Properties
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    date_assigned = db.Column(db.Date, nullable=False)
    date_due = db.Column(db.Date, nullable=False)
    hours_worked = db.Column(db.Float, nullable=False, default=0)
    rate = db.Column(db.Float, nullable=False, default=14.5)
    # company = db.Column(db.String(20))
    # job_type = db.Column(db.Enum, )

    # Relationships
    # one to many
    user = db.relationship('User', foreign_keys=[user_id], backref='jobs')
    author = db.relationship('Client', foreign_keys=[
                             client_id], backref='jobs')
