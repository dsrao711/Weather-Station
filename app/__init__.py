from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='static')

    # Registering blueprints
    from app.main.routes import bp as main_blueprint
    from app.prediction.routes import bp as predict_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(predict_blueprint)

    return app
