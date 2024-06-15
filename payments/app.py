from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulación de base de datos de pagos
payments_db = {
    "1": [{"item": "Game A", "amount": 50}],
    "2": [{"item": "Game B", "amount": 60}]
}

@app.route('/payments', methods=['GET'])
def get_all_payments():
    all_payments = []
    for payments in payments_db.values():
        all_payments.extend(payments)
    return render_template('payments.html', payments=all_payments)

@app.route('/payments/<user_id>', methods=['GET'])
def get_payments(user_id):
    payments = payments_db.get(user_id, [])
    return render_template('payments.html', payments=payments)

@app.route('/payments/<user_id>', methods=['POST'])
def process_payment(user_id):
    payment = request.json
    if user_id not in payments_db:
        payments_db[user_id] = []
    payments_db[user_id].append(payment)
    return jsonify(payment), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
