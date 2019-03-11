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
        return 'Store with the name {} does not exist'.format(name), 404

    
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


class Item(Resource):
    def post(self, name, item_name):
        for store in stores:
            if store['name'] == name:
                for item in store['items']:
                    if item['name'] == item_name:
                        return 'Item with the name {} already exists'.format(item_name), 400
                data = request.get_json()

                new_item = {
                    "name":item_name,
                    "price":data['price']
                }
                store['items'].append(new_item)
                return new_item, 201

        return 'Store with the name {} does not exist'.format(name), 400 



api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/store/<string:name>/<string:item_name>')

app.run(debug=True, port=9000)