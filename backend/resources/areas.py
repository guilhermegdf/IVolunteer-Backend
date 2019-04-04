from flask import jsonify, request
from flask_restful import Resource, reqparse

from utils.custom_response import custom_response
from models.AreaModel import AreaModel, AreaSchema

schema = AreaSchema(many=True)

class AssistenciaSocial(Resource):

    def get(self):
        res = AreaModel.get_all_for_meio_ambiente()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class Cultura(Resource):

    def get(self):
        res = AreaModel.get_all_for_cultura()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class Saude(Resource):

    def get(self):
        res = AreaModel.get_all_for_saude()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class MeioAmbiente(Resource):

    def get(self):
        res = AreaModel.get_all_for_meio_ambiente()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class DevDefesaDireito(Resource):

    def get(self):
        res = AreaModel.get_all_for_dev_defesa_direito()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class Habitacao(Resource):

    def get(self):
        res = AreaModel.get_all_for_habitacao()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)

class EducacaoPesquisa(Resource):

    def get(self):
        res = AreaModel.get_all_for_educacao_pesquisa()
        res_schema = schema.dump(res)
        return custom_response({'jwt_token': res_schema.data}, 200)
