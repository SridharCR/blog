import os
from flask import Flask



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='sridhar',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqllite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello World"

    from src.model import db
    from src.controller import auth
    db.init_app(app)
    app.register_blueprint(auth.bp)

    from src.controller import posts
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint="index")

    return app
