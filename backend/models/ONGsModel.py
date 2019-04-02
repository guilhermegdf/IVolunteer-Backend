from marshmallow import fields, Schema
from db import db
from werkzeug.security import generate_password_hash
import datetime
import pytz


utc_now = pytz.utc.localize(datetime.datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone('Brazil/East'))


class ONGsModel(db.Model):
    __tablename__ = 'tb_ongs'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    area_atuacao = db.Column(db.String(355), nullable=False)
    email = db.Column(db.String(355), nullable=False)
    data_abertura = db.Column(db.Date, nullable=True)
    responsavel = db.Column(db.String(355), nullable=False)
    address = db.Column(db.String(355), nullable=False)
    city = db.Column(db.String(355), nullable=False)
    state = db.Column(db.String(355), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(355), nullable=False)
    descricao = db.Column(db.String(355), nullable=False)
    status = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)

    def __init__(self, data):

        self.username = data.get('username')
        self.password = generate_password_hash(data.get('password'))
        self.cnpj = data.get('cnpj')
        self.area_atuacao = data.get('area_atuacao')
        self.email = data.get('email')
        self.data_abertura = data.get('data_abertura')
        self.responsavel = data.get('responsavel')
        self.address = data.get('address')
        self.city = data.get('city')
        self.state = data.get('state')
        self.phone = data.get('phone')
        self.name = data.get('name')
        self.descricao = data.get('descricao')
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
    def get_all_ong():
        return VolunteerModel.query.all()

    @staticmethod
    def get_one_ong(id):
        return VolunteerModel.query.get(id)

    @staticmethod
    def get_by_email(value):
        return ONGsModel.query.filter_by(email=value).first()

    @staticmethod
    def get_by_cnpj(value):
        return ONGsModel.query.filter_by(cnpj=value).first()

    @staticmethod
    def get_by_username(value):
        return ONGsModel.query.filter_by(username=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)

class ONGsSchema(Schema):
  username = fields.Str(required=True)
  password = fields.Str(required=True, load_only=True)
  cnpj = fields.Str(required=True)
  area_atuacao = fields.Str(required=True)
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  data_abertura = fields.Date()
  responsavel = fields.Str(required=True)
  address = fields.Str(required=True)
  city = fields.Str(required=True)
  state = fields.Str(required=True)
  phone = fields.Str(required=True)
  name = fields.Str(required=True)
  status = fields.Boolean(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
  descricao = fields.Str(required=True)
