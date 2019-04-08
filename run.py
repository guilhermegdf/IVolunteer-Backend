from db import db
from app import app
from flask_cors import CORS

db.init_app(app)
CORS(app)
