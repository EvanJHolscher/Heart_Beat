from socket import *
import time

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

last_ping = None
no_ping = 20
serverSocket.settimeout(no_ping)

while True:
    try: 
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        current_ping = time.time()
        if last_ping is not None:
            time_since_ping = current_ping-last_ping
        else: 
            time_since_ping = 0
        last_ping = time.time()
        print(f"Server received: {message.decode()} \n Last heartbeat received {time_since_ping} seconds ago")
        
        # The server responds
        serverSocket.sendto(message, address)

    except timeout:
            print ("No heartbeat after 20 seconds. Server quits. Server stops")
            break