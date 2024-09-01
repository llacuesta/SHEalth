from flask import Flask, request
from server_methods import *

# creating simple Flask app to receive requests
app = Flask(__name__)

# empty server instance
HE_server = HEServer()

# routes
@app.route('/send-context', methods=['POST'])
def receive_client_context():
    global HE_server
    print('Request Received')

    # initializing HE_server
    HE_server.generate_from_context(
        request.json.get('context').encode('cp437'),
        request.json.get('pubKey').encode('cp437')
    )

    # testing operation for client validation
    if HE_server:
        print(HE_server)
        return HE_server.validate_instance(
            request.json.get('cx').encode('cp437'),
            request.json.get('cy').encode('cp437')
        )
    else:
        return json.dumps({
            "success": False,
            "message": "Unable to generate HE server."
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)