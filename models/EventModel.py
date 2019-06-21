from marshmallow import fields, Schema
from models.ONGsModel import ONGsModel, ONGsSchema
from werkzeug.security import generate_password_hash
from db import db
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone('Brazil/East'))

class EventModel(db.Model):
    __tablename__ = 'tb_events'

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date, nullable=False)
    end = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(355), nullable=False)
    description = db.Column(db.String(355), nullable=False)
    created_at = db.Column(db.String(20))

    def __init__(self, data):

        self.ong_id = data.get('ong_id')
        self.start = data.get('start')
        self.end = data.get('end')
        self.title = data.get('title')
        self.description = data.get('description')
        self.created_at = pst_now.strftime("%d-%m-%Y %H:%M")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_events():
        return EventModel.query.all()

    @staticmethod
    def get_one_events(id):
        return EventModel.query.get(id)

    @staticmethod
    def get_by_title(value):
        return EventModel.query.filter_by(title=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    start = fields.Date()
    end = fields.Date()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.Str(dump_only=True)
    ong_id = fields.Int(required=True, load_only=True)
    ong = fields.Nested(ONGsSchema, required=False)
