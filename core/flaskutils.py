from flask import Flask, session, redirect, escape, request
from flask import render_template, url_for


def isAuth(session):
    """
    Verify if a user is authenticated
    """

    if 'auth' in session:
        if session['auth'] == True:
            return True
    return False
