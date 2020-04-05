from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from src.model.db import get_db
from src.model.models import BlogModels
from src.views.auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    data_object = BlogModels(db_conn=get_db())
    posts = data_object.fetch_posts()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        data_object = BlogModels(db_conn=get_db())
        if not title:
            error = "Title is required"

        if error is not None:
            flash(error)
        else:
            data_object.insert_post(title, body)
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


def get_post(id, check_author=True):
    data_object = BlogModels(db_conn=get_db())
    post = data_object.fetch_post(id)
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)
    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        data_object = BlogModels(db_conn=get_db())
        if not title:
            error = "Title is required"

        if error is not None:
            flash(error)
        else:
            data_object.update_post(title, body, id)
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    data_object = BlogModels(db_conn=get_db())
    get_post(id)
    data_object.delete_post(id)
    return redirect(url_for('blog.index'))
