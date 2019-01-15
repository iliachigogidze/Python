from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required

from security import authenticate, identity 

app = Flask(__name__)
app.secret_key = 'ilia'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    def post(self, name):
        data = request.get_json()
        for item in items:
            if name == item['name']:
                return {'message: ': 'Item already exists'}
    
        new_item = {
            'name':name,
            'price':data['price'],
            'made in':data['made in'],
            'quantity':data['quantity']
        } 
        items.append(new_item)
        return new_item, 201

    @jwt_required()
    def get(self, name):
        for item in items:
            if name == item['name']:
                return item, 200
        return {'message: ':None}, 404


class Items(Resource):
    def get(self):
        return items, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=8800, debug=True)