from models.VolunteerModel import VolunteerModel, VolunteerSchema
from marshmallow import fields, Schema
from db import db

class AreaModel(db.Model):
    __tablename__ = 'tb_area'

    id = db.Column(db.Integer, primary_key=True)
    assistencia_social = db.Column(db.Boolean)
    cultura = db.Column(db.Boolean)
    saude = db.Column(db.Boolean)
    meio_ambiente = db.Column(db.Boolean)
    dev_defesa_direito = db.Column(db.Boolean)
    habitacao = db.Column(db.Boolean)
    educacao_pesquisa = db.Column(db.Boolean)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('tb_volunteers.id'), nullable=False)
    volunteer = db.relationship("VolunteerModel", uselist=False, backref="options")

    def __init__(self, data):

        self.volunteer_id = data.get('volunteer_id')
        self.assistencia_social = data.get('assistencia_social')
        self.cultura = data.get('cultura')
        self.saude = data.get('saude')
        self.meio_ambiente = data.get('meio_ambiente')
        self.dev_defesa_direito = data.get('dev_defesa_direito')
        self.habitacao = data.get('habitacao')
        self.educacao_pesquisa = data.get('educacao_pesquisa')

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
    def get_one(id):
        return AreaModel.query.get(id)

    @staticmethod
    def get_all_areas():
        return AreaModel.query.all()

    @staticmethod
    def get_all_for_assistencia_social():
        return AreaModel.query.filter_by(assistencia_social=True)

    @staticmethod
    def get_all_for_cultura():
        return AreaModel.query.filter_by(cultura=True)

    @staticmethod
    def get_all_for_saude():
        return AreaModel.query.filter_by(saude=True)

    @staticmethod
    def get_all_for_meio_ambiente():
        return AreaModel.query.filter_by(meio_ambiente=True)

    @staticmethod
    def get_all_for_dev_defesa_direito():
        return AreaModel.query.filter_by(dev_defesa_direito=True)

    @staticmethod
    def get_all_for_habitacao():
        return AreaModel.query.filter_by(habitacao=True)

    @staticmethod
    def get_all_for_educacao_pesquisa():
        return AreaModel.query.filter_by(educacao_pesquisa=True)

    @staticmethod
    def get_one_volunteer_area(value):
        return AreaModel.query.filter_by(volunteer_id=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)

class AreaSchema(Schema):
    id = fields.Int(dump_only=True)
    assistencia_social = fields.Boolean(required=True)
    cultura = fields.Boolean(required=True)
    saude = fields.Boolean(required=True)
    meio_ambiente = fields.Boolean(required=True)
    dev_defesa_direito = fields.Boolean(required=True)
    habitacao = fields.Boolean(required=True)
    educacao_pesquisa = fields.Boolean(required=True)
    volunteer_id = fields.Int(required=True)
    volunteer = fields.Nested(VolunteerSchema, required=False)