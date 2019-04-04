from flask import jsonify, request
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from utils.custom_response import custom_response
from models.ONGsModel import ONGsModel, ONGsSchema

schema = ONGsSchema()

class LoginOng(Resource):

    def post(self):
        req_data = request.get_json()
        data, error = schema.load(req_data, partial=True)

        if error:
            return custom_response(error, 400)

        if not data.get('username') or not data.get('password'):
            return custom_response({'error': 'you need username and password to sign in'}, 400)

        user = ONGsModel.get_by_username(data.get('username'))

        if not user:
            return custom_response({'error': 'invalid credentials'}, 400)

        password = schema.dump(user).data.get('password')

        if user and check_password_hash(password, data.get('password')):
            data = schema.dump(user).data
            data['type'] = 'ONG'
            return custom_response({'jwt_token': create_access_token(identity=data)}, 200)
        else:
            return custom_response({'error': 'invalid credentials'}, 400)
