from datetime import datetime

from . import db


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float, index=True, nullable=False)
    currency = db.Column(db.String(3), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    paid = db.Column(db.Boolean, default=False)
