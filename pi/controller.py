# Controlls the pi and parses inputs

import sys
import socket 
import RF24
sys.path.insert(1, '../common')
from motorcommands import *

class controller:
    
	def __init__(self, connection, radio):

		self._functions = { 
			"set_bot": self.set_bot, 
			"left" : self.left, 
			"right" : self.right, 
			"back" : self.back, 
			"forward" : self.forward, 
			"stop" : self.stop, 
			"quit" : self.quit
		}

		self._conn = connection
		self._radio = radio
		self._bot = 1
		
		
	def quit(self):
		exit(0)
			
	def left(self):
		self.send_direction("left")

	def right(self):
		self.send_direction("right")
	
	def forward(self):
		self.send_direction("forward")
	
	def back(self):
		self.send_direction("back")

	def stop(self):
		self.send_direction("stop")

	def set_bot(self, new_id):
		self._bot = int(new_id)

	def send_direction(self, direction):
		print("Sending direction")
		max_out = 200
		if direction == "forward": 
			left = max_out
			right = max_out
		elif direction == "right":
			left = -max_out
			right = max_out
		elif direction == "left":
			left = max_out
			right = -max_out
		elif direction == "back": 
			left = -max_out
			right = -max_out
		elif direction == "stop":
			left = 0
			right = 0
		else: 
			left = 0
			right = 0
			print("Unrecognized command")
		print("Sending motor command")
		cmd = motor_command(left, right, id = self._bot)
		cmd.send(self._radio)


	def parse_input(self, line):
		args = line.strip().split()
		# Get the function to run from the dictionary 
		if(args[0] in self._functions):
			func = self._functions[args[0]]
			print("\nCalling function %s with arguments: %s" % (func.__name__, (' '.join(args[1:]))))
			try:
				func(*args[1:])
			except:
				print("Error executing command")
			
	def run(self): 
		while 1:
			#Receive from laptop
			data = self._conn.recv(32)
			#print(data)
			try:
				if not data:
					return
				line = data.decode('utf-8')
				print("Received command: " + line)
				self.parse_input(line)
			
			except:
				print("Error with command")
				return
