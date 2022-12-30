from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY']='this is secret key which is not secret at all'
    app.config['SQLALCHEMY_DATABASE_URI']= f"sqlite:///{DB_NAME}"
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Recom

    
    with app.app_context():
        db.create_all()

    login_manager=LoginManager()
    login_manager.login_view='views.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app


