import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")  # Bind to the port

while True:
    # Wait for a request
    json_data = socket.recv_string()
    print("Received:", json_data)

    # Process the JSON data
    data = json.loads(json_data)
    print("readyForCopying:", data['readyForCopying'])
    print("JSON Data:", data['json_data'])
    if data['readyForCopying']:
        del data['json_data']['category']
        data['readyForCopying'] = False

    # Send a response
    response_json = json.dumps(data)
    socket.send_string(response_json)
