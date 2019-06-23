from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required, jwt_optional
from utils.shortcuts import custom_response, filter_data
from models.OrderModel import OrderModel, OrderSchema

schema = OrderSchema()
order_schema = OrderSchema(many=True)

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
            res = OrderModel.get_by_volunteer(claims.get('id'))
            res_schema = order_schema.dump(res)
            return res_schema

        if claims.get('type') == 'ONG':
            res = OrderModel.get_by_ong(claims.get('id'))
            res_schema = order_schema.dump(res)
            return res_schema

class EditOrders(Resource):
    @jwt_required
    def delete(self, id):
        res = OrderModel.get_one(id)
        res.delete()
        message = {'response':'Solicitação recusada com sucesso.'}
    
    @jwt_required
    def put(self, id):
        req = request.get_json().get('data')
        res = OrderModel.get_one(id)
        print(req)
        print(res)
        res.update(req)
        message = {'response':'Atualizado com sucesso.'}
        return custom_response(message, 200)
