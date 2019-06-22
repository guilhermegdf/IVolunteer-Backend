from marshmallow import fields, Schema
from models.ONGsModel import ONGsModel, ONGsSchema
from models.VolunteerModel import VolunteerModel, VolunteerSchema
from models.EventModel import EventModel, EventSchema
from werkzeug.security import generate_password_hash
from db import db
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone('Brazil/East'))

class OrderModel(db.Model):
    __tablename__ = 'tb_orders'

    id = db.Column(db.Integer, primary_key=True)
    ong_id = db.Column(db.Integer, db.ForeignKey('tb_ongs.id'), nullable=False)
    ong = db.relationship("ONGsModel", uselist=False, backref="orders_ongs")
    volunteer_id = db.Column(db.Integer, db.ForeignKey('tb_volunteers.id'), nullable=False)
    volunteer = db.relationship("VolunteerModel", uselist=False, backref="orders_volunteer")
    event_id = db.Column(db.Integer, db.ForeignKey('tb_events.id'), nullable=False)
    event = db.relationship("EventModel", uselist=False, backref="orders_events")
    status = db.Column(db.Boolean)
    created_at = db.Column(db.String(20))


    def __init__(self, data):

        self.ong_id = data.get('ong_id')
        self.volunteer_id = data.get('volunteer_id')
        self.event_id = data.get('event_id')
        self.status = False
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
    def get_all_orders():
        return OrderModel.query.all()

    @staticmethod
    def get_one_events(id):
        return OrderModel.query.get(id)

    @staticmethod
    def get_by_existing(event_id, volunteer_id ):
        return OrderModel.query.filter_by(event_id=event_id, volunteer_id=volunteer_id).first()

    @staticmethod
    def get_all_completed():
        return OrderModel.query.filter_by(status=True)

    @staticmethod
    def get_all_pending():
        return OrderModel.query.filter_by(status=False)

    def __repr(self):
        return '<id {}>'.format(self.id)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    ong_id = fields.Int(required=True, load_only=True)
    ong = fields.Nested(ONGsSchema, required=False)
    volunteer_id = fields.Int(required=True, load_only=True)
    volunteer = fields.Nested(VolunteerSchema, required=False)
    event_id = fields.Int(required=True, load_only=True)
    event = fields.Nested(EventSchema, required=False)
    status = fields.Boolean(dump_only=True)
    created_at = fields.Str(dump_only=True)