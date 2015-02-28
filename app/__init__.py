# coding: utf-8

from flask                  import Flask
from flask                  import render_template

from flask.ext.sqlalchemy   import SQLAlchemy
from flask.ext.login        import LoginManager

from config                 import config

db                                  = SQLAlchemy()
login_manager                       = LoginManager()

login_manager.session_protection    = "strong"
login_manager.login_view            = "auth.Login"

def create_app( config_name ):
    app = Flask( __name__ )
    app.config.from_object( config[ config_name ] )
    config[ config_name ].init_app( app )

    db.init_app( app )
    login_manager.init_app( app )

    from .main import main as main_blueprint
    from .auth import auth as auth_plueprint
    app.register_blueprint( main_blueprint )
    app.register_blueprint( auth_plueprint, url_prefix="/auth" )

    return app