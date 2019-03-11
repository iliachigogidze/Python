from flask import Flask, jsonify, request

app = Flask(__name__)

stores = []


@app.route('/stores')
def get_stores():
    return jsonify(stores)



@app.route('/store/<string:name>', methods=['POST'])
def create_store(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            return jsonify('Store with the same name already exists.')
    new_store = {
        'name': name,
        'address': data['address'],
        'items':data['items']
    }
    stores.append(new_store)
    return jsonify(new_store), 201


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify('Store with the name {} doesn\'t exist'.format(name))


@app.route('/store/<string:name>/<string:item_name>', methods=['POST'])
def add_item(name, item_name):
    for store in stores:
        if store['name'] == name:
            for item in store['items']:
                if item['name'] == item_name:
                    return jsonify('Item with name {} already exists'.format(item_name))
            data = request.get_json()
            new_item = {
                "name":item_name,
                "price":data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify('Store with the name {} do not exist'.format(name))

app.run(port=9000, debug=True)