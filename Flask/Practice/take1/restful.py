from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

stores = []

class Stores(Resource):
    def get(self):
        return stores


class Store(Resource):
    def get(self, name):
        for store in stores:
            if store['name'] == name:
                return store, 200
        return "Store not found", 404

    def post(self, name):
        for store in stores:
            if store['name'] == name:
                return 'Store with the same name already exists', 400
        data = request.get_json()
        new_store = {
            'name':data['name'],
            'address':data['address'],
            'items':data['items']
        }
        stores.append(new_store)
        return new_store, 201
        


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')

app.run(port=9000, debug=True)