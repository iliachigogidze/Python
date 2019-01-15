from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

unis = []

class Unis(Resource):
    def get(self):
        return unis

class Uni(Resource):
    def get(self, name):
        for uni in unis:
            if uni['name'] is name:
                return uni, 200
        return {'Uni: ', None}, 404

    def put(self, name):
        

api.add_resource(Unis, '/universities')
api.add_resource(Uni, '/university/<string:name>')

app.run(debug=True)