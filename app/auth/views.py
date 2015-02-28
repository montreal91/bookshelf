# coding: utf-8

from flask import render_template, redirect, request, url_for, flash

from flask.ext.login import login_user
from flask.ext.login import logout_user, login_required

from . import auth
from ..models import AnUser
from .forms import LoginForm

@auth.route("/login", methods=["GET", "POST"])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = AnUser.query.filter_by(username=form.username.data).first()
        print(user)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.Index"))
        else:
            flash("Invalid username or password.")
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
@login_required
def Logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.Index"))
