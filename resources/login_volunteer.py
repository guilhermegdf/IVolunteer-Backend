from flask import jsonify, request
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from utils.shortcuts import custom_response
from models.VolunteerModel import VolunteerModel, VolunteerSchema

schema = VolunteerSchema()

class LoginVolunteer(Resource):

    def post(self):
        req_data = request.get_json()
        data, error = schema.load(req_data, partial=True)

        if error:
            return custom_response(error, 400)

        if not data.get('username') or not data.get('password'):
            return custom_response({'error': 'you need username and password to sign in'}, 400)

        user = VolunteerModel.get_by_username(data.get('username'))

        if not user:
            return custom_response({'error': 'invalid credentials'}, 400)

        password = schema.dump(user).data.get('password')
        if user and check_password_hash(password, data.get('password')):
            data = schema.dump(user).data
            data['type'] = 'Volunteer'
            return custom_response({'jwt_token': create_access_token(identity=data)}, 200)
        else:
            return custom_response({'error': 'invalid credentials'}, 400)
