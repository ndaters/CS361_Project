#   Example how main program may call microservice
#   Connects REQ socket to tcp://localhost:5555


import zmq
import struct

context = zmq.Context()

#  Socket to talk to server
proceed = True
while proceed is True:

    integer_to_send = int(input("Enter a maximum value for a requested random number: "))

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    packed_data = struct.pack("i", integer_to_send)

    socket.send(packed_data)
    message = str(socket.recv())[1:]
    print(message)

