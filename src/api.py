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
# -----------------------------------------------------------------------------CLI-Commands
@app.cli.command("initdb")
def init_db():
    """Initializes database and any model objects necessary for assignment"""
    db.drop_all()
    db.create_all()

    print("Initialized Freelance-Tracker Database.")


@app.cli.command("devinit")
def init_dev_data():
    """Initializes database with data for development and testing"""
    db.drop_all()
    db.create_all()
    print("Initialized Freelance-Tracker Database.")

    db.session.commit()
    print("Added dummy data.")

# -----------------------------------------------------------------------------------/CLI Commands


@app.route('/')
def backend():
    return('hello!')


# Pulls json from a request
def pull_json():
    # TODO: IMPLEMENT
    raise NotImplementedError


# Send the jobs of the passed in author
def get_jobs():
    # TODO: IMPLEMENT
    raise NotImplementedError


# Output billing period to csv
def output_to_csv():
    # TODO: IMPLEMENT
    raise NotImplementedError


# Creates a new job
# args: cuser, author, type, task, company
def create_job():
    # TODO: IMPLEMENT
    raise NotImplementedError
    return


def update_job():
    # TODO: IMPLEMENT
    raise NotImplementedError


def check_auth():
    # TODO: IMPLEMENT
    raise NotImplementedError


def requres_auth():
    # TODO: IMPLEMENT
    raise NotImplementedError


def authenticate():
    # TODO: IMPLEMENT
    raise NotImplementedError


def create_user():
    # TODO: IMPLEMENT
    raise NotImplementedError
