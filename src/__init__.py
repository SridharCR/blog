from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='sridhar')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return "Hello World"

    from src.models import db
    from src.controllers import auth
    db.init_app(app)
    app.register_blueprint(auth.auth_blueprint)

    from src.controllers import posts
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint="index")
    CORS(app)
    return app
