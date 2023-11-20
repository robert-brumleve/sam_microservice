import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to the receiver

data = {
    "readyForCopying": True,
    "json_data": {
        "name": "value1",
        "description": "value2",
        "category": "value3",
        "price": "value4"
    }
}

json_data = json.dumps(data)  # Convert the dictionary to JSON

socket.send_string(json_data)  # Send the combined JSON data

# Wait for the response
response = socket.recv_string()
print("Received:", response)

socket.close()
