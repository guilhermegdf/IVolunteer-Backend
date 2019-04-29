from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required, jwt_optional
from utils.shortcuts import custom_response, filter_data
from models.AreaModel import AreaModel, AreaSchema
from models.ONGsModel import ONGsModel, ONGsSchema

schema = AreaSchema(many=True)
ong_schema = ONGsSchema(many=True)

class AssistenciaSocial(Resource):

    @jwt_optional
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_assistencia_social()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('assistencia_social')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)

class Cultura(Resource):

    @jwt_optional
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_cultura()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('cultura')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)

class Saude(Resource):

    @jwt_optional
    def get(self):
        claims = get_jwt_claims()
        
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_saude()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('saude')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)

class MeioAmbiente(Resource):

    @jwt_optional
    def get(self):
        claims = get_jwt_claims()

        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_meio_ambiente()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('meio-ambiente')
            data = ong_schema.dump(res)

        return custom_response(data, 200)

class DevDefesaDireito(Resource):

    @jwt_optional
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_dev_defesa_direito()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('dev_defesa_direito')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)

class Habitacao(Resource):

    @jwt_optional
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_habitacao()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('habitacao')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)

class EducacaoPesquisa(Resource):

    @jwt_optional
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = AreaModel.get_all_for_educacao_pesquisa()
            res_schema = schema.dump(res)
            data =filter_data(res_schema, 'volunteer')

        else:
            res = ONGsModel.get_by_area('educacao_pesquisa')
            data = ong_schema.dump(res)
            
        return custom_response(data, 200)
