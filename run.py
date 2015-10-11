from config import Config

from flask import Flask, session, redirect, escape, request
from flask import render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    if 'auth' in session:
        if session['auth'] == True:
            return render_template('index.html')
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
        if request.form["inputEmail"] == Config.auth_mail and request.form["inputPassword"] == Config.auth_password:
            session['auth'] = True
            return redirect(url_for('index'))
        else:
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
