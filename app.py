from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'Sarvanan',
        'items': [
            {
                'name': 'item1',
                'price': 20.0
            }

        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')

# Post /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'store': new_store})


# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return name + ' is not present'


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores});


# Post /store/<string:name>/item  {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'store': store})
        return 'store not present'


# Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['item']})
    return 'item is not present'


app.run(port=5000)
