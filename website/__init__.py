from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager




db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mr. worldwide'
    ENV ='prod'
    
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/sra'
        
    else:
        app.debug = False
        app.config['SQLACHEMY_DATABASE_URI'] = 'postgres://mhgqtisxrnhajo:47830ca44a024943e000deda5eb86a37b84fb1e4dd79bec1cc233702ce32a99e@ec2-3-225-132-26.compute-1.amazonaws.com:5432/d3m22ojr7fksk2'

    
    db.init_app(app)


    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    
    return app

def create_database(app):
    if not path.exists('website/' + 'sra'):
        db.create_all(app=app)
        print('Created Database!')