from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

studios = []

class Studios(Resource):
    def get(self):
        return studios, 200

class Studio(Resource):
    def post(self, name):
        data = request.get_json()
        for studio in studios:
            if studio['name'] == name:
                return {'message':'this studio already exists'}

        new_studio = {
            'name':data['name'],
            'country':data['country'],
            'movies':[]
        }
        studios.append(new_studio)
        return new_studio, 201

    def get(self, name):
        for studio in studios:
            if studio['name'] == name:
                return studio, 200
        return {'studio': None}, 404
    
    def delete(self, name):
        for i, studio in studios:
            if studio['name'] == name:
                del studio[i]
                return {'message':'deleted'}, 204
            else:
                return {'studio': None}, 404
    
    


api.add_resource(Studios, '/studios')
api.add_resource(Studio, '/studio/<string:name>')

app.run(port=8000, debug=True)