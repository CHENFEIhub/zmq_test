import zmq
import json

xpub_addr = 'tcp://127.0.0.1:5555'
context = zmq.Context()
subscriberSocket = context.socket(zmq.SUB)
subscriberSocket.connect(xpub_addr)
subscriberSocket.setsockopt_string(zmq.SUBSCRIBE, "fromPMS")

def subsribeMessage():
    [topic, json_data] = subscriberSocket.recv_multipart()
    print("Message Received!")
    message = json.loads(json_data)
    print(message)

while True:
    if subscriberSocket.poll(timeout=1000):
        subsribeMessage()

