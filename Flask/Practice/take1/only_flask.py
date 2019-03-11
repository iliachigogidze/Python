from flask import Flask, jsonify, request

app = Flask(__name__)

stores = []


@app.route('/stores')
def get_stores():
    return jsonify(stores)


@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name':data['name'],
        'address':data['address'],
        'items':data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store), 200
    return jsonify({"message ":"Store not found"}), 404


app.run(debug=True)








# {
# 	"name":"2 nabiji",
# 	"address":"Pekini 5",
# 	"items":[
# 		{
# 			"name":"bread",
# 			"price":1
# 		},
# 		{
# 			"name":"soap",
# 			"price":2.55
# 		}
# 		]
# }