from flask import Flask, request
from src import api
import pytest


def test_json_from_req():
    req = request()
    req.method = 'POST'
    pass
