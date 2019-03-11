from flask import Flask, jsonify, request

app = Flask(__name__)

stores = []

@app.route('/stores')
def get_stores():
    return jsonify(stores), 200

@app.route('/store/<string:name>', methods=['POST'])
def create_store(name):
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
    return jsonify('There is no store with the name {}'.format(name))


@app.route('/items')
def get_items():
    items = []
    for store in stores:
        items += store['items']
    return jsonify(items), 200


@app.route('/store/<string:name>/<string:item_name>', methods=['POST'])
def create_item(name, item_name):
    for store in stores:
        if store['name'] == name:
            data = request.get_json()
            if item_name in store['items']:
                return jsonify('Item with name {} already exists'.format(item_name))
            new_item = {
                "name":item_name,
                "price":data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item), 201
    return jsonify('Store with the name {} do not exist'.format(name)), 400

@app.route('/store/')

app.run(debug=True, port=9000)