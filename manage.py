from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db import db
from app import app

from models.VolunteerModel import VolunteerModel
from models.ONGsModel import ONGsModel
from models.ProfessionModel import ProfessionModel

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
