from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from functools import wraps

import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask("__name__")

#checks for UPPERCASE variables
app.config.from_object(__name__)

#function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#login required
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#login page    
@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

#logout page
@app.route('/logout')
def logout():
    """docstring for logout"""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

#main page
@app.route("/main")
@login_required
def main():
    return render_template('main.html')
    
if __name__ == '__main__':
    app.run()