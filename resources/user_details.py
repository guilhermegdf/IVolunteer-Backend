from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_claims, jwt_required, jwt_optional
from utils.shortcuts import custom_response, filter_data
from models.VolunteerModel import VolunteerModel, VolunteerSchema
from models.ONGsModel import ONGsModel, ONGsSchema
from models.AreaModel import AreaModel, AreaSchema

volunteer_schema = VolunteerSchema()
ong_schema = ONGsSchema()
area_schema = AreaSchema()

class MyDetails(Resource):

    @jwt_required
    def get(self):

        claims = get_jwt_claims()
 
        if claims.get('type') == 'ONG':
            res = ONGsModel.get_one_ong(claims.get('id'))
            data = ong_schema.dump(res).data
        
        elif claims.get('type') == 'Volunteer':
            res = VolunteerModel.get_one_volunteers(claims.get('id'))
            data = area_schema.dump(res.options[0]).data
        else:
            data = {'error':'Not found ID'}
            return custom_response(data, 400)

        return custom_response(data, 200)

    @jwt_required
    def put(self):

        req_data = request.get_json().get('data')

        claims = get_jwt_claims()
 
        if claims.get('type') == 'ONG':
            data, error = ong_schema.load(req_data)
            if error:
                return custom_response(error, 400)

            ong = ONGsModel.get_one_ong(claims.get('id'))
            ong.update(data)

        elif claims.get('type') == 'Volunteer':
            data, error = volunteer_schema.load(req_data.get('volunteer'))
            
            if error:
                return custom_response(error, 400)
            
            volunteer = VolunteerModel.get_one_volunteers(claims.get('id'))
            volunteer.update(data)

            req_data['volunteer_id'] = claims.get('id')
            data, error = area_schema.load(req_data)
            
            if error:
                return custom_response(error, 400)
            area_data = {}
            for i in data:
                if i != 'volunteer':
                    area_data[i]=  data[i]
            areas = AreaModel.get_one_volunteer_area(claims.get('id'))
            areas.update(area_data)


        else:
            data = {'error':'Not found ID'}
            return custom_response(data, 400)

        return custom_response(data, 200)

class AccountDetails(Resource):

    @jwt_optional
    def get(self, id):
        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = VolunteerModel.get_one_volunteers(id)
            data = area_schema.dump(res.options[0]).data

        else:
            res = ONGsModel.get_one_ong(id)
            data = ong_schema.dump(res).data

        return custom_response(data, 200)

class UserSearch(Resource):
    def get(self, search_term):
        claims = get_jwt_claims()
        if claims.get('type') == 'ONG':
            res = VolunteerModel.get_by_filter(search_term)
            data = area_schema.dump(res.options[0]).data

        else:
            res = ONGsModel.get_by_filter(search_term)
            data = ong_schema.dump(res).data
        
        return custom_response(data, 200)