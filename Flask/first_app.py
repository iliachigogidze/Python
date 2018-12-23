from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name':'store name',
        'items': [
            {
                'name':'shpilka',
                'price':12.5
            }
        ]    
    }
]


@app.route('/')
def home():
    return 'Hello bitches'

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store1', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Store not found'})

app.run(port=5000)