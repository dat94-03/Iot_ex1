from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Data storage (in-memory for simplicity)
data_store = []

# POST request to save data
@app.route('/api/request-data', methods=['POST'])
def handle_post_request():
    request_data = request.json
    device_id = request_data.get('deviceId')
    qr_code_id = request_data.get('qrCodeId')
    qr_code_value = request_data.get('qrCodeValue')

    # Save data to the in-memory data store
    new_data = {
        'deviceId': device_id,
        'qrCodeId': qr_code_id,
        'qrCodeValue': qr_code_value
    }
    data_store.append(new_data)

    return jsonify(new_data), 201  # Return 201 Created status code

# GET request to retrieve all data
@app.route('/api/request-data/all', methods=['GET'])
def get_all_data():
    if data_store:
        return jsonify(data_store)
    else:
        return 'No data available', 404  # Return 404 if no data is present

# GET request to retrieve data by deviceId
@app.route('/api/request-data/<device_id>', methods=['GET'])
def get_data_by_device_id(device_id):
    # Search for data with the matching deviceId
    matching_data = [item for item in data_store if item['deviceId'] == device_id]
    
    if matching_data:
        return jsonify(matching_data)
    else:
        return 'No data found for the given deviceId', 404  # Return 404 if not found
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))  # Render assigns the port
    app.run(host='0.0.0.0', port=port, debug=True)

