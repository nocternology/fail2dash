from config import Config
from core.flaskutils import *
from core.utils import gatherHostInfo

from flask import Flask, session, redirect, escape, request
from flask import render_template, url_for

import hashlib

app = Flask(__name__)


@app.route('/')
def index():
    if isAuth(session):
        return render_template('index.html', data=gatherHostInfo())
    else:
        return redirect(url_for('auth'))


@app.route('/raw')
def raw_logs():
    if isAuth(session):
        return render_template('raw.html')
    else:
        return redirect(url_for('auth'))


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if 'auth' in session:
        if session['auth'] == True:
            return redirect(url_for('index'))

    if request.method == "GET":
        return render_template('auth.html', error=False)
    else:
        if request.form["inputEmail"] == Config.auth_mail:
            if hashlib.sha512(request.form["inputPassword"]).hexdigest() == Config.auth_password:
                session['auth'] = True
                return redirect(url_for('index'))

        return render_template('auth.html', error=True)


@app.route('/logout')
def logout():
    if 'auth' in session:
        if session['auth'] == True:
            session.pop('auth', False)
    return redirect(url_for('auth'))


if __name__ == '__main__':
    app.debug = Config.debug
    app.secret_key = Config.secret
    app.run()
