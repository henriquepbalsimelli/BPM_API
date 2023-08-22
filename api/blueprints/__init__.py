from blueprints.Auth.routes.auth import bp_auth

def init_app(app):
    app.register_blueprint(bp_auth)