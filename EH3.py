from socket import *
import random
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

packet_loss_prob = .1
while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    random_loss = random.random()
    if random_loss <= packet_loss_prob:
        print ("Packet Lost")
    else:
        # Generate random delay between 10ms and 20ms
        random_number = random.randint(10,20)
        random_delay = random_number / 1000.0

        start_time = time.perf_counter()
        while time.perf_counter() - start_time < random_delay:
            continue

        # The server responds
        serverSocket.sendto(message, address)