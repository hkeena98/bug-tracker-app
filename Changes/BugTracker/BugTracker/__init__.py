from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'cd02f1d63e0086b5eecb4e1d'
db = SQLAlchemy(app)

from BugTracker import routes
