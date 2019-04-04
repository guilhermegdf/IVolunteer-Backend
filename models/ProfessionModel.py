from marshmallow import fields, Schema
from db import db

class ProfessionModel(db.Model):
    __tablename__ = 'tb_professions'

    id = db.Column(db.Integer, primary_key=True)
    profession = db.Column(db.String(99), nullable=False)

    @staticmethod
    def get_all_professions():
        return ProfessionModel.query.all()

    @staticmethod
    def get_one_profession(id):
        return ProfessionModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)

class ProfessionSchema(Schema):
    id = fields.Int(dump_only=True)
    profession = fields.Str(required=True)
