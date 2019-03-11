from flask import Flask, render_template, jsonify, Response, request

app = Flask(__name__)

app.route('/')
def backend():
    return('hello!')