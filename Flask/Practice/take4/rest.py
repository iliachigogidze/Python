from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

stores = []

class Stores(Resource):
    def get(self):
        return stores, 200
    

class Store(Resource):
    def get(self, name):
        for store in stores:
            if store['name'] == name:
                return store, 200
        return 'No store with the {} name'.format(name), 404
    

    def post(self, name):
        for store in stores:
            if store['name'] == name:
                return 'Store {} already exists'.format(name), 400
        data = request.get_json()
        new_store = {
            "name":name,
            "address":data['address'],
            "items":data['items']
        }
        stores.append(new_store)
        return new_store, 201
    

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')

app.run(debug=True, port=9000)