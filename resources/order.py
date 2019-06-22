from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required, jwt_optional
from utils.shortcuts import custom_response, filter_data
from models.OrderModel import OrderModel, OrderSchema

schema = OrderSchema()

class Oders(Resource):

    @jwt_required
    def post(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'Volunteer':
            
            req_data = request.get_json().get('data')
            req_data['volunteer_id'] = claims.get('id')
            data, error = schema.load(req_data)

            if error:
                return custom_response(error, 400)

            order_in_db = OrderModel.get_by_existing(data.get('event_id'), claims.get('id'))
            if order_in_db:
                message = {'error': 'Você já se voluntariou nesse evento.'}
                return custom_response(message, 400)
            
            order = OrderModel(data)
            order.save()
            message = {'return':'Evento Cadastrado com sucesso'}
            return custom_response(message, 201)
        else:
            message = {'error': 'Você não possui permissão para realizar esta ação'}
            return custom_response(message, 400)
    
    @jwt_required
    def get(self):

        claims = get_jwt_claims()
        if claims.get('type') == 'Volunteer':
            pass

        if claims.get('type') == 'ONG':
            pass