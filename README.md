**Part 1: UDP Pinger with No Delay and No Loss**

\1) My UDP pinger sends a determined number of messages from my client across the local

network to my server on port 127.0.0.1. For this exercise, 10 pings were sent. Right

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


**Part 2: UDP Pinger with Delay**s

\1) My UDP Ping server simulates a 10ms to 20ms RTT delay by generating a random

number between 10 and 20, dividing that value by 1000, and then looping through a

time.perf\_counter() for that amount of time before sending a server response to the

client. At first, I tried using time.sleep(), but this was generating values far outside of

what was desired. This method achieves the desired effect, and does so after receiving

the message from the client, causing a 10ms to 20ms RTT delay.

\2) To run the code, use two different terminals. Python must be installed\.

a) First, in Terminal 1, use command: python EH2.py

b) Then, in Terminal 2, use command: python EH1.py

**Part 3: UDP Pinger with Delays and Packet Losses**

1) This UDP ping Server has an additional randomly generated number between 0 and 1\.

We then check if the random number is <= .1, and if it is, we do not send a response

back to the server. This causes the socket to timeout, and the packet to be lost. We also

include a random number that is used to determine a delay between 10 and 20 ms for

the server response.

\2) To run the code, use two different terminals\. Python must be installed\.

a) First, in Terminal 1, use command: python EH3.py

b) Then, in Terminal 2, use command: python EH1.py


**Part 4: HeartBeat Monitor Using Python**

1) To run the code, commands in three terminals are necessary:

a) Terminal 1 (Server) command: python EH4s.py

b) Terminal 2 (Client1) command: python EH4c.py client1

c) Terminal 3 (Client2) command: python EH4c.py client2



Server stops")

break

