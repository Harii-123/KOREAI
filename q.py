from flask import Flask, jsonify, request
import json

with open('orders.json', 'r') as file:
    orders_data = json.load(file)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def displayOrderID():
    order_id = request.args.get('orderID')  # Extract the orderID from the query parameter in the URL
    if order_id is None:
        return jsonify({'error': 'OrderID parameter is missing'})
    try:
        order_id = int(order_id)  # Convert the orderID to an integer
    except ValueError:
        return jsonify({'error': 'Invalid OrderID'})
    order = None
    for item in orders_data:
        if item.get('orderID') == order_id:  # Check if the orderID matches
            order = item
            break
    if order:
        return jsonify(order)
    else:
        return jsonify({'error': 'Order not found'})

if __name__ == '__main__':
    app.run(debug=True)
