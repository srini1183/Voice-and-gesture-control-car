import socket
import open_py

client = socket.socket()

port = 8500

client.connect(('<Provide ip of raspberry pi>',port))
	
while True:
	data = open_py.record()
	print(data)
	client.send(data.encode())
	if data=='bye':
		break
	
client.close()
