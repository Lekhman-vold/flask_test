from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_admin.menu import MenuLink
from flask_security import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class ProductAdmin(ModelView):
    form_columns = ('name', 'color', 'weight', 'price')
    column_filters = ('name', 'color', 'weight', 'price')


class DeliveryAdmin(ModelView):
    column_filters = ('product_id', 'country', 'city', 'address')
