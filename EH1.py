import socket
import time

# Connect to server
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12000
cliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliSock.connect((SERVER_IP, SERVER_PORT))

num_pings = 50
packet_loss = 0
rtt_times = []
timeout = 2.0
cliSock.settimeout(timeout)


print("")
for x in range(num_pings):
    try:
        init_time = time.time()

        #Send Message to server
        message = f"Evan {x+1} {time.ctime(time.time())}"
        cliSock.send(message.encode())
        
        # Get response from server and calculate RTT
        response, server_address = cliSock.recvfrom(1024)
        end_time = time.time()
        rtt = (end_time - init_time) * 1000
        rtt_times.append(rtt)

        # Print Results
        print(f"Evan {x+1}: server reply: {response.decode()}, RTT = {rtt:.2f} ms")
        
    except socket.timeout:
        print (f"Evan {x+1}: Request timed out")
        packet_loss+=1

cliSock.close()

# Calculate mininum, maximum, and average RTT and packet loss percentage
min_rtt = min(rtt_times)
max_rtt = max(rtt_times)
average_rtt = sum(rtt_times) / len(rtt_times)
packet_loss_percentage = (packet_loss / num_pings) * 100


print ("\nPing Report")
print (f"Minimum RTT in milliseconds: {min_rtt:.3f} ms")
print (f"Maximum RTT in milliseconds: {max_rtt:.3f} ms")
print (f"Average RTT in milliseconds: {average_rtt:.3f} ms")
print (f"Percentage packet loss rate: {packet_loss_percentage:.3f}%")