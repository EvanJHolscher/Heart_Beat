import socket
import time
import random
import sys


def init_client(username):

    # Connect to server
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 12000
    cliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliSock.connect((SERVER_IP, SERVER_PORT))

    num_pings = 100
    packet_loss = 0
    timeout = 2.0
    cliSock.settimeout(timeout)

    for x in  range(num_pings):
        try:
            #Send Message to server every 2 to 25 seconds
            random_delay = random.randint(2,25)
            start_time = time.perf_counter()
            while time.perf_counter() - start_time < random_delay:
                continue
            message = f"Evan {username}: sent heartbeat to server {time.ctime(time.time())}"
            print(message)
            cliSock.send(message.encode())

        except socket.timeout:
            print (f"{username}: Request timed out")
            packet_loss+=1

    cliSock.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python EH4c.py <username>")
        sys.exit(1)
    username = sys.argv[1]
    init_client(username)