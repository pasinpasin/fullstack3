from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.fakulteti import Fakulteti
from utils import hash_password

class FakultetiListResource(Resource):
    def get(self):
        data = []
        for fakulteti in Fakulteti.objects:
            
            data.append(fakulteti)
        return {'data': data}, HTTPStatus.OK
    def post(self):
        json_data = request.get_json()
        fakulteti = json_data.get('fakulteti')
      
        if Fakulteti.get_by_emertimi(fakulteti):
            return {'message': 'fakulteti already used'}, HTTPStatus.BAD_REQUEST
       
        newfakulteti = Fakulteti(
            
        )
        newfakulteti.save()
        data = {
            'id': newfakulteti.id,
            'emertimi': newfakulteti.emertimi,
            
        }
        return data, HTTPStatus.CREATED
