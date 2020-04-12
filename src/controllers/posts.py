from flask import (Blueprint, flash, request, jsonify)
from flask_restful import Resource, Api
from werkzeug.exceptions import abort
from flask_cors import CORS

from src.models.db import get_db
from src.models.models import BlogModels

bp = Blueprint('blog', __name__)
api_bp = Api(bp)

def get_post(id):
    data_object = BlogModels(db_conn=get_db())
    post = data_object.fetch_post(id)
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))
    return post

class PostCreate(Resource):
    def post(self):
        title = request.form['title']
        body = request.form['body']
        id = request.form['id']
        error = None
        data_object = BlogModels(db_conn=get_db())
        if not title:
            error = "Title is required"

        if error is not None:
            flash(error)
        else:
            data_object.insert_post(title, body, id)
            return jsonify("True")

api_bp.add_resource(PostCreate, '/create')

class PostUpdate(Resource):
    def post(self, id):
        f = open("info_logs.txt", "w")
        f.write(str(request.form))
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
            return jsonify("True")

    def get(self, id):
        post = get_post(id)
        return jsonify(post)

api_bp.add_resource(PostUpdate, '/<int:id>/update')

class PostGeneral(Resource):
    def get(self):
        data_object = BlogModels(db_conn=get_db())
        posts = data_object.fetch_posts()
        return jsonify(posts)

api_bp.add_resource(PostGeneral, '/')

class PostDelete(Resource):
    def post(self, id):
        data_object = BlogModels(db_conn=get_db())
        get_post(id)
        data_object.delete_post(id)
        return jsonify("True", "Deleted successfully")

api_bp.add_resource(PostDelete, '/<int:id>/delete')
