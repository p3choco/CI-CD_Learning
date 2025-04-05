from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []
current_id = 1

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

@app.route('/orders', methods=['POST'])
def create_order():
    global current_id
    data = request.json
    order = {
        "order_id": current_id,
        "user_id": data.get("user_id"),
        "status": data.get("status", "NEW"),
        "amount": data.get("amount", 0)
    }
    orders.append(order)
    current_id += 1
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    for o in orders:
        if o['order_id'] == order_id:
            return jsonify(o), 200
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
