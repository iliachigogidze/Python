from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404


    def post(self, name):
        data = request.get_json()
        new_item = {
            'name':name,
            'price': data['price']
        }
        items.append(new_item)
        return new_item, 201

api.add_resource(Items, '/item/<string:name>')

app.run(port=5000, debug=True)