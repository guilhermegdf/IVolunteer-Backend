from marshmallow import fields, Schema
from models.ProfessionModel import ProfessionModel
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone('Brazil/East'))

class VolunteerModel(db.Model):
    __tablename__ = 'tb_volunteers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(355), nullable=False)
    email = db.Column(db.String(355), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(355), nullable=False)
    city = db.Column(db.String(355), nullable=False)
    state = db.Column(db.String(355), nullable=False)
    profession_id = db.Column(db.Integer, db.ForeignKey('tb_professions.id'), nullable=False)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)

    def __init__(self, data):

        self.username = data.get('username')
        self.password = generate_password_hash(data.get('password'))
        self.name = data.get('name')
        self.email = data.get('email')
        self.phone = data.get('phone')
        self.birth = data.get('birth')
        self.address = data.get('address')
        self.city = data.get('city')
        self.state = data.get('state')
        self.profession_id = data.get('profession_id')
        self.status = True
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
    def get_all_volunteers():
        return VolunteerModel.query.all()

    @staticmethod
    def get_one_volunteers(id):
        return VolunteerModel.query.get(id)

    @staticmethod
    def get_by_email(value):
        return VolunteerModel.query.filter_by(email=value).first()

    @staticmethod
    def get_by_username(value):
        return VolunteerModel.query.filter_by(username=value).first()

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr(self):
        return '<id {}>'.format(self.id)

class VolunteerSchema(Schema):
  username = fields.Str(required=True)
  password = fields.Str(required=True)
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  phone = fields.Str(required=True)
  birth = fields.Date()
  address = fields.Str(required=True)
  city = fields.Str(required=True)
  state = fields.Str(required=True)
  profession_id = fields.Int(required=True)
  status = fields.Boolean(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
