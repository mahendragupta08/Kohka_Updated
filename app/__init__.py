from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config["SECRET_KEY"] = "bc0e24d687e10d57cdc99b02aeccd15d5bdd92e538f898549b99939c629ba7e0"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .payment import payment as payment_blueprint
    app.register_blueprint(payment_blueprint)


    return app