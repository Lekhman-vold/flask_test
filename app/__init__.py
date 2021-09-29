from flask import Flask, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_security import Security, SQLAlchemyUserDatastore, auth_required

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    from app.models import register_models
    from app.models.account import User, Role
    from app.models.product import Product
    from app.models.delivery import Delivery
    from app.admin.admin import ProductAdmin, DeliveryAdmin
    from app.admin.admin import MyAdminIndexView, LogoutMenuLink

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://naruto:voloda2000@localhost:54320/flask_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw'
    app.config['SECURITY_PASSWORD_SALT'] = 'MY_SALT'

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    db.init_app(app)

    app.db = db
    migrate.init_app(app, db)

    admin = Admin(app, name='Admin dashboard', template_mode='bootstrap4', index_view=MyAdminIndexView())
    admin.add_view(ProductAdmin(Product, db.session))
    admin.add_view(DeliveryAdmin(Delivery, db.session))

    admin.add_link(LogoutMenuLink(name='Logout', category='', url='/logout'))

    register_models()

    @app.before_first_request
    def create_user():
       db.create_all()
       user_datastore.create_user(email='test_user@mail.com', password='password')
       db.session.commit()

    @app.route('/')
    @auth_required()
    def home():
        return redirect('/admin')

    # db.create_all()
    return app
