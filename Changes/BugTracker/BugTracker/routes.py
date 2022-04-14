from BugTracker import app
from flask import render_template


@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def home_page():
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')
