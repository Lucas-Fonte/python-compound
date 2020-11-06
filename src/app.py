from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from .api import compound
        app.register_blueprint(compound.compound_bp)

    return app

