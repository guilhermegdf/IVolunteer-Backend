from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.ONGsModel import ONGsModel, ONGsSchema
from utils.shortcuts import custom_response
from pycpfcnpj import cpfcnpj

schema = ONGsSchema()

class SignupOng(Resource):

    def post(self):
        req_data = request.get_json()
        data, error = schema.load(req_data)

        if error:
            return custom_response(error, 400)

        # check if email already exist in the db
        user_in_db = ONGsModel.get_by_email(data.get('email'))
        if user_in_db:
            message = {'error': 'Email already exist, please supply another email address'}
            return custom_response(message, 400)

        # check if username already exist in the db
        user_in_db = ONGsModel.get_by_username(data.get('username'))
        if user_in_db:
            message = {'error': 'User already exist, please supply another username'}
            return custom_response(message, 400)

        if cpfcnpj.validate(data.get('cnpj')):

            user_in_db = ONGsModel.get_by_cnpj(data.get('cnpj'))
            if user_in_db:
                message = {'error': 'CNPJ already exist, please supply another cnpj'}
                return custom_response(message, 400)

        else:
            message = {'error': 'invalid CPNJ'}
            return custom_response(message, 400)

        user = ONGsModel(data)
        user.save()
        message = {'return':'ONG register Okay'}
        return custom_response(message, 201)
