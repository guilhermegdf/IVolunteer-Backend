from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required
from utils.shortcuts import custom_response, filter_data
from models.VolunteerModel import VolunteerModel, VolunteerSchema
from models.ONGsModel import ONGsModel, ONGsSchema
from models.AreaModel import AreaModel, AreaSchema

volunteer_schema = VolunteerSchema()
ong_schema = ONGsSchema()

class MyDetails(Resource):

    @jwt_required
    def get(self):

        claims = get_jwt_claims()
 
        if claims.get('type') == 'ONG':
            res = ONGsModel.get_one_ong(claims.get('id'))
            data = ong_schema.dump(res)
        
        if claims.get('type') == 'Volunteer':
            res = VolunteerModel.get_one_volunteers(claims.get('id'))
            data = volunteer_schema.dump(res)
        
        else:
            data = {'error':'Not found ID'}
            return custom_response(data, 400)

        return custom_response(data, 200)

class AccountDetails(Resource):

    @jwt_required
    def get(self, id):

        claims = get_jwt_claims()
 
        if claims.get('type') == 'ONG':
            res = VolunteerModel.get_one_volunteers(id)
            data = volunteer_schema.dump(res)
        
        else:
            res = ONGsModel.get_one_ong(id)
            data = ong_schema.dump(res)
            return custom_response(data, 400)
