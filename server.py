import socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

int1 = 3
int2 = 5
int3 = 8
int4 = 10

GPIO.setup(int1,GPIO.OUT)
GPIO.setup(int2,GPIO.OUT)
GPIO.setup(int3,GPIO.OUT)
GPIO.setup(int4,GPIO.OUT)




def forward():
	global int1
	global int2
	global int3
	global int4
	GPIO.output(int1,GPIO.HIGH)
	GPIO.output(int4,GPIO.HIGH)
	GPIO.output(int2,GPIO.LOW)
	GPIO.output(int3,GPIO.LOW)

def backward():
	global int1
	global int2
	global int3
	global int4
	GPIO.output(int2,GPIO.HIGH)
	GPIO.output(int3,GPIO.HIGH)
	GPIO.output(int1,GPIO.LOW)
	GPIO.output(int4,GPIO.LOW)

def left():
	global int1
	global int2
	global int3
	global int4
	GPIO.output(int1,GPIO.LOW)
	GPIO.output(int4,GPIO.HIGH)
	GPIO.output(int2,GPIO.LOW)
	GPIO.output(int3,GPIO.LOW)

def right():
	global int1
	global int2
	global int3
	global int4
	GPIO.output(int1,GPIO.HIGH)
	GPIO.output(int4,GPIO.LOW)
	GPIO.output(int2,GPIO.LOW)
	GPIO.output(int3,GPIO.LOW)

def stop():
	global int1
	global int2
	global int3
	global int4
	GPIO.output(int1,GPIO.LOW)
	GPIO.output(int4,GPIO.LOW)
	GPIO.output(int2,GPIO.LOW)
	GPIO.output(int3,GPIO.LOW)
	

server = socket.socket()
port = 8500
server.bind(('',port))
server.listen(5)
c,addr = server.accept()

while True:
	data = c.recv(1024)
	print(data.decode())
	data = data.decode()
	if data == 'forward':
		forward()
	elif data == 'backward':
		backward()
	elif data == 'left':
		left()
	elif data == 'right':
		right()
	elif data == 'stop':
		stop()
	elif data=='bye':
		break

server.close()
	