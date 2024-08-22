from flask import Flask
from flask_restful import Api
from models import db
from resources.registro import Register, Login
from .resources.usuario import UserProfile
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api = Api(app)
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(UserProfile, '/user')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
