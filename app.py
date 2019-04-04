import os
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from key import token
from resources.signup_volunteer import SignupVolunter
from resources.signup_ong import SignupOng
from resources.login_volunteer import LoginVolunteer
from resources.login_ong import LoginOng
from resources.areas import AssistenciaSocial, EducacaoPesquisa, DevDefesaDireito, Cultura, Habitacao, MeioAmbiente, Saude

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL', 'postgresql://postgres:folklore2@localhost/db_ivolunteer')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = token

jwt = JWTManager(app)
api = Api(app)

@jwt.user_claims_loader
def add_claims_to_acess_token(identity):
    return{"id":identity.get('id'), "type":identity.get('type')}

api.add_resource(LoginVolunteer, '/login/volunteer')
api.add_resource(SignupVolunter, '/signup/volunteer')
api.add_resource(LoginOng, '/login/ong')
api.add_resource(SignupOng, '/signup/ong')
api.add_resource(AssistenciaSocial, '/assistencia-social')
api.add_resource(EducacaoPesquisa, '/educacao-pesquisa')
api.add_resource(DevDefesaDireito, '/defesa-direito')
api.add_resource(Cultura, '/cultura')
api.add_resource(Saude, '/saude')
api.add_resource(Habitacao, '/habitacao')
api.add_resource(MeioAmbiente, '/meio-ambiente')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
