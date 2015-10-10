import config

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
        if request.form["inputEmail"] == config.auth_mail and request.form["inputPassword"] == config.auth_password:
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
    app.debug = config.debug
    app.secret_key = "8897879668D998AD5E9C4200E90E6056BBEB2FA38745ECA4D6710BC535ACDA02"
    app.run()
