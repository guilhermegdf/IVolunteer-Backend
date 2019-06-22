from flask import jsonify, request
from flask_restful import Resource, reqparse
from models.VolunteerModel import VolunteerModel, VolunteerSchema
from models.AreaModel import AreaModel, AreaSchema
from utils.shortcuts import custom_response


schema = VolunteerSchema()
schema_area = AreaSchema()
class SignupVolunter(Resource):

    def post(self):

        req_data = request.get_json()
        data, error = schema.load(req_data['data'])
        if error:
            return custom_response(error, 400)

        # check if email already exist in the db
        user_in_db = VolunteerModel.get_by_email(data.get('email'))
        if user_in_db:
            message = {'error': 'Este e-mail já esta cadastrado'}
            return custom_response(message, 200)

        # check if username already exist in the db
        user_in_db = VolunteerModel.get_by_username(data.get('username'))
        if user_in_db:
            message = {'error': 'Este nome de usuario já existe'}
            return custom_response(message, 200)

        user = VolunteerModel(data)
        user.save()

        data_area, error = schema_area.load(req_data['data'])
        data_area['volunteer_id'] = user.id
        area = AreaModel(data_area)
        area.save()

        message = {'return':'Volunteer register Okay'}
        return jsonify(message, 201)
