import pytest
from flask import Flask, request


def test_json_from_req():
    req = request()
    req.method = 'POST'
    pass
