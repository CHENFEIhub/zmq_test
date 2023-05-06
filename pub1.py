import zmq
import json
import time
timeout = time.time() + 3

xsub_addr = 'tcp://127.0.0.1:5556'
context = zmq.Context()
publisherSocket = context.socket(zmq.PUB)
publisherSocket.connect(xsub_addr)
publishName = "fromPMS".encode('utf-8')

message = {
    "name":"cf",
    "major":"dsai"
}

def publishMessage(message):
    publisherSocket.send_multipart([publishName, json.dumps(message).encode('utf-8')])
    print('Message sent!')
    print(message)

while True:
    if time.time() > timeout:
        break
    publishMessage(message)