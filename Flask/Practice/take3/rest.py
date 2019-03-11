from flask_restful import Resource, Api
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

stores = []

class Stores(Resource):
    def get(self):
        return stores, 200


class Store(Resource):
    def post(self, name):
        for store in stores:
            if store['name'] == name:
                return 'Store with the name {} already exists'.format(name), 400
        data = request.get_json()
        new_store = {
            "name":name,
            "address":data['address'],
            "items":data['items']
        }
        stores.append(new_store)
        return new_store, 201

    def get(self, name):
        for store in stores:
            if store['name'] == name:
                return store, 200
        return 'Store with the name {} does not exist'.format(name), 404


class Items(Resource):
    def get(self):
        items = []
        for store in stores:
            items += store['items']
        return items
        

class Item(Resource):
    def get(self, name):
        for store in stores:
            if store['name'] == name:
                return store['items'], 200
        return 'Store with the name {} does not exist'.format(name), 404


    def post(self, name, item_name):
        for store in stores:
            if store['name'] == name:
                if item_name in store['items']:
                    return 'Item with the name {} already exists'.format(item_name), 401
                data = request.get_json()
                new_item = {
                    "name":data['name'],
                    "price":data["price"]
                }
                store['items'].append(new_item)
                return new_item, 201
        return'Store with the name {} does not exist'.format(name), 404


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')
api.add_resource(Item, '/store/<string:name>')
api.add_resource(Items, '/items')

app.run(debug=True, port=9000)