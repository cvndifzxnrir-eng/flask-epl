# from epl import models , routes

from flask import Flask
from epl.extensions import db , migrate
from epl.core.routes import core_bp
from epl.clubs.routes import club_bp

def create_app():
    app = Flask(_name_)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/epl_s02_db'
    app.secret_key = b'klklklk'

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(core_bp , url_prefix='/')
    app.register_blueprint(club_bp , url_prefix='/clubs')

    return app

