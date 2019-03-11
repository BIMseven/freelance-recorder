from flask import Flask, request
from src import api, models
import pytest


@pytest.fixture()
def make_user():
    """Adds a user to the database to ensure we have something to add"""
    return


@pytest.fixture()
def initdb():
    """Initializes the database to ensure we have a clean working environment"""
    api.init_db
    return 42


def test_initdb(initdb):
    assert initdb == 42


def test_create_job():
    """ tests that creat_job returns a job json object"""
    # api.create_job(user, client, start_date, due_date, rate)
    return
