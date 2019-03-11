from flask import Flask
from src.models import db
import os
import string

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "connect4.db"
)
# Suppress deprecation warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/')
def backend():
    return('hello!')


# Pulls json from a request
def pull_json():
    # TODO: IMPLEMENT
    return


# Send the jobs of the passed in author
def get_jobs():
    # TODO: IMPLEMENT
    return


# Output billing period to csv
def output_to_csv():
    # TODO: IMPLEMENT
    return


# Creates a new job
# args: cuser, author, type, task, company
def create_job():
    # TODO: IMPLEMENT
    return


def update_job():
    # TODO: IMPLEMENT
    return


def check_auth():
    # TODO: IMPLEMENT
    return


def requres_auth():
    # TODO: IMPLEMENT
    return


def authenticate():
    # TODO: IMPLEMENT
    return


def create_user():
    # TODO: IMPLEMENT
    return
