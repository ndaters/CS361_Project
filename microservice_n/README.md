# CS361-Microservice-1 Communication Contract

## Random Number Generator Microservice

Takes a request for a random number between 0 and the input value and returns a random number. 

Requests are sent with socket.send(packed data)

Packed data is created with:

import struct
packed_data = struct.pack("i", integer_to_send)

The response is received with socket.recv()

An example of sending requests and receiving responses is provided in the repository named "exaple_user_program.py". In the example, the program requests an integer as the max value 'Enter a maximum value for a requested random number: '. The microservice gives a status update 'Generating a random number between 0 and XX', the microservice then shares on its own window 'Your random number between 0 and XX is YY', this message is also sent to the receiver. 


## Ground rules/communication contract:

We will communicate through Discord.

We will respond to each other’s inquiries within 36 hours.

If you have not received a response within 36 hours, feel free to continue by making assumptions and inform the team of the assumptions you are making.

When available, we will inform our teammates of any personal roadblocks which may impact our time availability. (no need to specify why that is, just a clear understanding that you might not be available for a few days)

We will document our design decisions so that each member has a clear understanding of the connectivity between our microservices. (to prevent the need to reach out to each other so often)
