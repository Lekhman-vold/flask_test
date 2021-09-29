from app import db
from datetime import datetime, timezone


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    color = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    delivery_id = db.relationship('Delivery', backref='product', lazy=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(tz=timezone.utc))

    def __repr__(self):
        return '<Product %r>' % self.name

