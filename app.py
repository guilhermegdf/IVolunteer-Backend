import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from resources.signup_volunteer import SignupVolunter
from resources.signup_ong import SignupOng
from resources.login_volunteer import LoginVolunteer
from resources.login_ong import LoginOng
from resources.areas import AssistenciaSocial, EducacaoPesquisa, DevDefesaDireito, Cultura, Habitacao, MeioAmbiente, Saude
from resources.user_details import MyDetails, AccountDetails, UserSearch
from resources.events import Events, OneEvent
from resources.order import Oders

app = Flask(__name__)

cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL', 'postgresql://pmrdqcokniwazt:729e52602d279adb94184e4dcbc4257ce54bf18e2c07eb66eb6d4e9e68c2f1af@ec2-50-17-246-114.compute-1.amazonaws.com/dkb32pkrb37q9')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '#9FvjX%X/=A]?`=A;1ih[{:MY*kCgM'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)
api = Api(app)

@jwt.user_claims_loader
def add_claims_to_acess_token(identity):
    return{"id":identity.get('id'), "type":identity.get('type')}

api.add_resource(LoginVolunteer, '/login/volunteer')
api.add_resource(SignupVolunter, '/signup/volunteer')
api.add_resource(LoginOng, '/login/ong')
api.add_resource(SignupOng, '/signup/ong')
api.add_resource(MyDetails, '/my-details')
api.add_resource(AccountDetails, '/account-details/<int:id>')
api.add_resource(AssistenciaSocial, '/assistencia-social')
api.add_resource(EducacaoPesquisa, '/educacao-pesquisa')
api.add_resource(DevDefesaDireito, '/defesa-direito')
api.add_resource(Cultura, '/cultura')
api.add_resource(Saude, '/saude')
api.add_resource(Habitacao, '/habitacao')
api.add_resource(MeioAmbiente, '/meio-ambiente')
api.add_resource(UserSearch, '/search/<search_term>')
api.add_resource(Events, '/events')
api.add_resource(OneEvent, '/events/<int:id>')
api.add_resource(Oders, '/orders')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
