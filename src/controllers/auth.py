import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify)
from flask_restful import Resource, Api
from werkzeug.security import check_password_hash

from src.models.db import get_db
from src.models.models import BlogModels

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
auth_api_bp = Api(auth_blueprint)


class Register(Resource):
    def get(self):
        return render_template('auth/register.html')

    def post(self):
        username = request.form['username']
        password = request.form['password']
        error = None
        data_object = BlogModels(db_conn=get_db())
        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        elif data_object.get_user_id(username) is not None:
            error = 'User {} is already registered.'.format(username)
        if error is None:
            data_object.insert_new_user(username, password)
            return redirect(url_for('auth.login'))

        flash(error)


auth_api_bp.add_resource(Register, '/register')


class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        error = None
        data_object = BlogModels(get_db())
        user = data_object.get_username(username)
        if user is None:
            error = "Incorrect Username"
        elif not check_password_hash(user['password'], password):
            error = "Incorrect Password"

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return jsonify("true")
        flash(error)


auth_api_bp.add_resource(Login, '/login')


@auth_blueprint.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    data_object = BlogModels(db_conn=get_db())
    if user_id is None:
        g.user = None
    else:
        g.user = data_object.get_logged_user(user_id)


class Logout(Resource):
    def get(self):
        session.clear()
        return jsonify("true")


auth_api_bp.add_resource(Logout, '/logout')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
