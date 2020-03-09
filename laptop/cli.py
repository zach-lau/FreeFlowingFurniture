#System libraries
import sys
sys.path.insert(1, '../common')
import socket

# #User libraries
# from motorcommands import *


class cli:
	
	def __init__(self, sock):
		self._sock = sock
	# 	self._functions = { 
	# 		"move": self.move, 
	# 		"set_bot": self.set_bot, 
	# 		"left" : self.left, 
	# 		"right" : self.right, 
	# 		"back" : self.back, 
	# 		"forward" : self.forward, 
	# 		"stop" : self.stop
	# 	}	
	
	# def left(self):
	# 	self.send_direction("left")

	# def right(self):
	# 	self.send_direction("right")
	
	# def forward(self):
	# 	self.send_direction("forward")
	
	# def back(self):
	# 	self.send_direction("back")

	# def stop(self):
	# 	self.send_direction("stop")

	# def set_bot(self):
	# 	pass

	# def send_direction(self, direction):
	# 	max_out = 200
	# 	if direction == "forward": 
	# 		left = max_out
	# 		right = max_out
	# 	elif direction == "right":
	# 		left = -max_out
	# 		right = max_out
	# 	elif direction == "left":
	# 		left = max_out
	# 		right = -max_out
	# 	elif direction == "back": 
	# 		left = -max_out
	# 		right = -max_out
	# 	elif direction == "stop":
	# 		left = 0
	# 		right = 0
	# 	else: 
	# 		left = 0
	# 		right = 0
	# 		print("Unrecognized command")
	# 	command = motor_command(left, right)
	# 	print(left)
	# 	print(right)
	# 	try: 
	# 		command.send(self._sock)
	# 	except:
	# 		print("Unable to send command")

	# def move(self, direction):
	# 	self.send_direction(direction)

	
	# def parse_input(self, line):
	# 	args = line.strip().split()
	# 	# print("Args is ")
	# 	# print(args)
	# 	# Get the function to run from the dictionary 
	# 	if(args[0] in self._functions):
	# 		func = self._functions[args[0]]
	# 		print("Func is ")
	# 		print(func.__name__)
	# 		print("args are")
	# 		print(*args[1:])
	# 		func(*args[1:])

	def send(self, line):
		self._sock.sendall(bytes(line, 'utf-8'))
	def run(self):
		# A command line interface that talks with the server
		# sock : socket to communicate with 
		line = input()
		# left : left motor pwm from -255 to 255
		# right : right motor pwm from -255 to 255

		while line:
			self.send(line)
			line = str(input())

		self._sock.close()
		print("Closing client")