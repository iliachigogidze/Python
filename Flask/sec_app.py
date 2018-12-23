from flask import Flask, jsonify, request

app = Flask(__name__)

stores =     [
        {
            'name': 'McDonald\'s',
            'items': 
            [
                {
                    'item_name':'Hamburger',
                    'price': 2.20
                }
            ]
        },
        {
            'name': 'Wendy\'s',
            'items':
            [
                {
                    'item_name':'Stelzenburger',
                    'price':3.50
                }
            ]
        }
    ]

#hello
@app.route('/home')
def home():
    return 'Hello darling'

#get all stores
@app.route('/stores')
def get_stores():
    return jsonify(stores)

#create a store
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    stores.append(data)
    return jsonify(data)

#get store
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)

#create item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['items'].append(data)
            return jsonify(store['items'])

    return 'Store was not found'

#get items
@app.route('/store/<string:name>/items')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return 'Store was not found'
    
app.run(port=5000)