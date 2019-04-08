from flask import jsonify, request
from flask_restful import Resource, reqparse
from utils.shortcuts import custom_response, filter_data
from models.AreaModel import AreaModel, AreaSchema
from flask_cors import cross_origin

schema = AreaSchema(many=True)

class AssistenciaSocial(Resource):

    def get(self):

        res = AreaModel.get_all_for_assistencia_social()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class Cultura(Resource):

    def get(self):
        res = AreaModel.get_all_for_cultura()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class Saude(Resource):

    def get(self):
        res = AreaModel.get_all_for_saude()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class MeioAmbiente(Resource):
    @cross_origin
    def get(self):
        res = AreaModel.get_all_for_meio_ambiente()
        res_schema = schema.dump(res)

        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class DevDefesaDireito(Resource):

    def get(self):
        res = AreaModel.get_all_for_dev_defesa_direito()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class Habitacao(Resource):

    def get(self):
        res = AreaModel.get_all_for_habitacao()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)

class EducacaoPesquisa(Resource):

    def get(self):
        res = AreaModel.get_all_for_educacao_pesquisa()
        res_schema = schema.dump(res)
        return custom_response({'response': filter_data(res_schema, 'volunteer')}, 200)
