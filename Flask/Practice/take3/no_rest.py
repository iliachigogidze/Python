from flask import Flask, jsonify, request

app = Flask(__name__)

stores = []

@app.route('/stores')
def get_stores():
    return jsonify(stores), 200


@app.route('/store/<string:name>', methods=['POST'])
def add_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify('Store with the name {} already exists'.format(name)), 400
    data = request.get_json()
    new_store = {
        "name":name,
        "address":data['address'],
        "items":data['items']
    }
    stores.append(new_store)
    return jsonify(new_store), 201

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify('Store with the name {} does not exist'.format(name)), 404


@app.route('/items')
def get_items():
    items = []
    for store in stores:
        items += store['items']
    return jsonify(items)


@app.route('/<string:name>/<string:item_name>')
def get_item_from_store(name, item_name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items']), 200
    return jsonify('Store with the name {} does not exist'.format(name)), 404


@app.route('/store/<string:name>/<string:item_name>', methods=['POST'])
def create_item(name, item_name):
    for store in stores:
        if store['name'] == name:
            if item_name in store['items']:
                return jsonify('Item with the name {} already exists'.format(item_name)), 401
            data = request.get_json()
            new_item = {
                "name":data['name'],
                "price":data["price"]
            }
            store['items'].append(new_item)
            return jsonify(new_item), 201
    return jsonify('Store with the name {} does not exist'.format(name)), 404


# @app.route('/store/<string:name>/<string:item_name>', methods=['POST'])
# def add_item(name, item_name):
#     for store in stores:
#         if store['name'] == name:
#             for item in store['items']:
#                 if item['name'] == item_name:
#                     return jsonify('Item with name {} already exists'.format(item_name))
#             data = request.get_json()
#             new_item = {
#                 "name":item_name,
#                 "price":data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify(new_item)

#     return jsonify('Store with the name {} do not exist'.format(name))



app.run(debug=True, port=9000)