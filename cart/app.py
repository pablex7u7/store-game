from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulación de base de datos de carritos
carts_db = {
    "1": [{"item": "Game A", "quantity": 1}],
    "2": [{"item": "Game B", "quantity": 2}]
}

@app.route('/cart', methods=['GET'])
def get_all_carts():
    all_carts = []
    for cart in carts_db.values():
        all_carts.extend(cart)
    return render_template('cart.html', carts=all_carts)

@app.route('/cart/<user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts_db.get(user_id, [])
    return render_template('cart.html', carts=cart)

@app.route('/cart/<user_id>', methods=['POST'])
def add_to_cart(user_id):
    item = request.json
    if user_id not in carts_db:
        carts_db[user_id] = []
    carts_db[user_id].append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
