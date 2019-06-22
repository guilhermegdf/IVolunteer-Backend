from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.ONGsModel import ONGsModel, ONGsSchema
from utils.shortcuts import custom_response, get_lat_long
from pycpfcnpj import cpfcnpj

schema = ONGsSchema()

class SignupOng(Resource):

    def post(self):
        req_data = request.get_json().get('data')
        data, error = schema.load(req_data)
        if error:
            return custom_response(error, 400)

        user_in_db = ONGsModel.get_by_email(data.get('email'))
        if user_in_db:
            message = {'error': 'Este e-mail já esta cadastrado'}
            return custom_response(message, 202)

        # check if username already exist in the db
        user_in_db = ONGsModel.get_by_username(data.get('username'))
        if user_in_db:
            message = {'error': 'Este nome de usuario já existe'}
            return custom_response(message, 202)

        if cpfcnpj.validate(data.get('cnpj')):

            user_in_db = ONGsModel.get_by_cnpj(data.get('cnpj'))
            if user_in_db:
                message = {'error': 'CNPJ já cadastrado, insira um novo valor'}
                return custom_response(message, 202)

        else:
            message = {'error': 'CNPJ inválido'}
            return custom_response(message, 202)

        data = {**data, **get_lat_long(data.get('address'))}
        user = ONGsModel(data)
        user.save()
        message = {'return':'ONG register Okay'}
        return custom_response(message, 201)
