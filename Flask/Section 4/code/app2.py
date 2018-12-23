from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

restaurants = []

class Restaurant(Resource):
    def post(self, name):
        print('hi')
        data = request.get_json()
        new_restaurant = {
            'name':name,
            'menu':data['menu'],
            'address':data['address']
        }
        print('hi2')
        
        restaurants.append(new_restaurant)
        print('hi3')
        
        return new_restaurant, 201

    def get(self, name):
        for restaurant in restaurants:
            if restaurant['name'] == name:
                return restaurant, 200
        else:
            return {'restaurant':None}, 404

class Restaurants(Resource):
    def get(self):
        return restaurants, 200

api.add_resource(Restaurant, '/restaurant/<string:name>')
api.add_resource(Restaurants, '/restaurants')

app.run(port=5001)