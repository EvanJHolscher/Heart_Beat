**Part 1: UDP Pinger with No Delay and No Loss**

\1) My UDP pinger sends a determined number of messages from my client across the local

network to my server on port 127.0.0.1. For this exercise, 10 pings were sents. Right

before sending the message, real-world time and relative time were both set using

time.time() and time.perf\_counter() from the time library, respectively. Upon sending the

message to the server, we then get a response from the server, and end both times. The

client then subtracts the starting times from the ending times, giving two different relative

times. The perf\_counter is more precise and used to calculate the minimum, maximum,

and average RTT’s, and the time.time() function is used to print the results. This

happens 10 times, and each time the perf\_counter generated RTT is appended to a list.

The timeout is set to 2 seconds, and if a response is not found, the socket will timeout

and a packet\_loss counter will increase by 1. After all ping attempts are completed, the

RTT list’s maximum, average, and minimum are computed and displayed. The

packet\_loss percentage is then calculated by dividing the number of packets lost with

the total ping attempts, and then multiplying that value by 100. This value is also

displayed in the ping report.

\2) To specify the timeout value for the datagram socket, you first set a variable timeout to

the desired number of seconds. You then use cliSock.settimeout(timeout), where cliSock

is the socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM) object. Then, when

sending a message, you use the try-except method. Inside of the try block, you attempt

to complete whatever task is required. Then, you specify a “except socket.timeout”, and

increase the packet\_loss.

\3) To run code, you must have two terminals open\. One terminal is responsible for the

server, and the other for the client. Python must be installed. The server must be started

before the client. First, in terminal 1, use command: python udppingserver\_no\_loss.py.



<a name="br2"></a> 

Then, in terminal 2, use command: EH1.py.

\4) Client Code

import socket

import time

\# Connect to server

SERVER\_IP = "127.0.0.1"

SERVER\_PORT = 12000

cliSock = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)

cliSock.connect((SERVER\_IP, SERVER\_PORT))

num\_pings = 10

packet\_loss = 0

rtt\_times = []

timeout = 2.0 # Seconds

cliSock.settimeout(timeout)

print("")

for x in range(num\_pings):

try:

init\_time = time.time()

init\_min\_max\_time = time.perf\_counter()



<a name="br3"></a> 

#Send Message to server

message = f"Evan {x+1} {time.ctime(time.time())}"

cliSock.send(message.encode())

\# Get response from server and calculate RTT

response, server\_address = cliSock.recvfrom(1024)

end\_time = time.time()

end\_time\_min\_max = time.perf\_counter()

rtt = (end\_time - init\_time) \* 1000

rtt\_times.append((end\_time\_min\_max-init\_min\_max\_time)\*1000)

\# Print Results

print(f"Evan {x+1}: server reply: {response.decode()}, RTT = {rtt:.2f}

ms")

except socket.timeout:

print (f"Evan {x+1}: Request timed out")

packet\_loss+=1

cliSock.close()

\# Calculate mininum, maximum, and average RTT and packet loss percentage

min\_rtt = min(rtt\_times)

max\_rtt = max(rtt\_times)

average\_rtt = sum(rtt\_times) / len(rtt\_times)

packet\_loss\_percentage = (packet\_loss / num\_pings) \* 100

print ("\nPing Report")

print (f"Minimum RTT in milliseconds: {min\_rtt:.3f} ms")

print (f"Maximum RTT in milliseconds: {max\_rtt:.3f} ms")

print (f"Average RTT in milliseconds: {average\_rtt:.3f} ms")

print (f"Percentage packet loss rate: {packet\_loss\_percentage:.3f}%")

Server Code:

\# udppingserver\_no\_loss.py

from socket import \*

\# Create a UDP socket

serverSocket = socket(AF\_INET, SOCK\_DGRAM)

\# Assign IP address and port number to socket

serverSocket.bind(('', 12000))



<a name="br4"></a> 

while True:

\# Receive the client packet along with the address it is coming from

message, address = serverSocket.recvfrom(1024)

\# The server responds

serverSocket.sendto(message, address)

**Part 2: UDP Pinger with Delay**s

\1) My UDP Ping server simulates a 10ms to 20ms RTT delay by generating a random

number between 10 and 20, dividing that value by 1000, and then looping through a

time.perf\_counter() for that amount of time before sending a server response to the

client. At first, I tried using time.sleep(), but this was generating values far outside of

what was desired. This method achieves the desired effect, and does so after receiving

the message from the client, causing a 10ms to 20ms RTT delay.

\2) To run the code, use two different terminals\. Python must be installed\.

a) First, in Terminal 1, use command: python EH2.py

b) Then, in Terminal 2, use command: python EH1.py

\3) UDP Ping Server:

from socket import \*

import random

import time

\# Create a UDP socket

serverSocket = socket(AF\_INET, SOCK\_DGRAM)

\# Assign IP address and port number to socket

serverSocket.bind(('', 12000))



<a name="br5"></a> 

while True:

\# Receive the client packet along with the address it is coming from

message, address = serverSocket.recvfrom(1024)

\# Generate random delay between 10ms and 20ms

random\_number = random.randint(10,20)

random\_delay = random\_number / 1000.0

start\_time = time.perf\_counter()

while time.perf\_counter() - start\_time < random\_delay:

continue

\# The server responds

serverSocket.sendto(message, address)



<a name="br6"></a> 

**Part 3: UDP Pinger with Delays and Packet Losses**

\1) This UDP ping Server has an additional randomly generated number between 0 and 1\.

We then check if the random number is <= .1, and if it is, we do not send a response

back to the server. This causes the socket to timeout, and the packet to be lost. We also

include a random number that is used to determine a delay between 10 and 20 ms for

the server response.

\2) To run the code, use two different terminals\. Python must be installed\.

a) First, in Terminal 1, use command: python EH3.py

b) Then, in Terminal 2, use command: python EH1.py



<a name="br7"></a> 

\3) UDP Ping Server with Delay and Losses

from socket import \*

import random

import time

\# Create a UDP socket

serverSocket = socket(AF\_INET, SOCK\_DGRAM)

\# Assign IP address and port number to socket

serverSocket.bind(('', 12000))

packet\_loss\_prob = .1

while True:

\# Receive the client packet along with the address it is coming from

message, address = serverSocket.recvfrom(1024)

random\_loss = random.random()

if random\_loss <= packet\_loss\_prob:

print ("Packet Lost")

else:

\# Generate random delay between 10ms and 20ms

random\_number = random.randint(10,20)

random\_delay = random\_number / 1000.0

start\_time = time.perf\_counter()

while time.perf\_counter() - start\_time < random\_delay:

continue

\# The server responds

serverSocket.sendto(message, address)

**Part 4: HeartBeat Monitor Using Python**

\1) To run the code, commands in three terminals are necessary:

a) Terminal 1 (Server) command: python EH4s.py

b) Terminal 2 (Client1) command: python EH4c.py client1

c) Terminal 3 (Client2) command: python EH4c.py client2

\2) Run-time screen captures

a) Client sending heartbeat pings to server



<a name="br8"></a> 



<a name="br9"></a> 

b) Server prints the received heartbeat pings from the client, and the time interval



<a name="br10"></a> 

c) Server detects absence of client heartbeats and quits



<a name="br11"></a> 

\3) Code Listings

a) Client code

import socket

import time

import random

import sys

def init\_client(username):

\# Connect to server

SERVER\_IP = "127.0.0.1"

SERVER\_PORT = 12000

cliSock = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)

cliSock.connect((SERVER\_IP, SERVER\_PORT))

num\_pings = 100

packet\_loss = 0

timeout = 2.0



<a name="br12"></a> 

cliSock.settimeout(timeout)

for x in range(num\_pings):

try:

#Send Message to server every 2 to 25 seconds

random\_delay = random.randint(2,25)

start\_time = time.perf\_counter()

while time.perf\_counter() - start\_time < random\_delay:

continue

message = f"Evan {username}: sent heartbeat to server

{time.ctime(time.time())}"

print(message)

cliSock.send(message.encode())

except socket.timeout:

print (f"{username}: Request timed out")

packet\_loss+=1

cliSock.close()

if \_\_name\_\_ == "\_\_main\_\_":

if len(sys.argv) != 2:

print("Usage: python EH4c.py <username>")

sys.exit(1)

username = sys.argv[1]

init\_client(username)

b) Server code

from socket import \*

import time

\# Create a UDP socket

serverSocket = socket(AF\_INET, SOCK\_DGRAM)

\# Assign IP address and port number to socket

serverSocket.bind(('', 12000))

last\_ping = None



<a name="br13"></a> 

no\_ping = 20

serverSocket.settimeout(no\_ping)

while True:

try:

\# Receive the client packet along with the address it is

coming from

message, address = serverSocket.recvfrom(1024)

current\_ping = time.time()

if last\_ping is not None:

time\_since\_ping = current\_ping-last\_ping

else:

time\_since\_ping = 0

last\_ping = time.time()

print(f"Server received: {message.decode()} \n Last

heartbeat received {time\_since\_ping} seconds ago")

\# The server responds

serverSocket.sendto(message, address)

except timeout:

print ("No heartbeat after 20 seconds. Server quits.

Server stops")

break

