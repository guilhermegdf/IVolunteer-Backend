from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required, jwt_optional
from utils.shortcuts import custom_response
from models.EventModel import EventModel, EventSchema

schema = EventSchema()
schema_many = EventSchema(many=True)

class Events(Resource):

    @jwt_required
    def post(self):

        claims = get_jwt_claims()

        if claims.get('type') == 'ONG':
            
            req_data = request.get_json().get('data')
            req_data['ong_id'] = claims.get('id')
            data, error = schema.load(req_data)
            if error:
                return custom_response(error, 400)
            event_in_db = EventModel.get_by_title(data.get('title'))

            if event_in_db:
                message = {'error': 'Email already exist, please supply another email address'}
                return custom_response(message, 400)

        else:
            message = {'error': 'Você não possui permissão para realizar esta ação'}
            return custom_response(message, 400)
        event = EventModel(data)
        event.save()
        message = {'return':'Evento Cadastrado com sucesso'}
        return custom_response(message, 201)

    def get(self):
        res = EventModel.get_all_events()
        data = schema_many.dump(res).data
        return custom_response(data, 200)

class OneEvent(Resource):
    def get(self, id):
        res = EventModel.get_one_events(id)
        data = schema.dump(res).data
        data['ong_name'] = data['ong']['name']
        data['ong_id'] = data['ong']['id']
        return custom_response(data, 200)