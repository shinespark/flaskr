# coding: utf-8
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# configration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'developemnt key'
USERNAME = 'admin'
PASSWORD = 'default'


# create out little appplication :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run()
