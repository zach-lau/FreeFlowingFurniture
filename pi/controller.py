# Controlls the pi and parses inputs

import socket 
import RF24

class controller:
    
	def __init__(self, connection, radio):

		self._functions = { 
			"set_bot": self.set_bot, 
			"left" : self.left, 
			"right" : self.right, 
			"back" : self.back, 
			"forward" : self.forward, 
			"stop" : self.stop
		}

		self._conn = connection
		self._radio = radio
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

	def set_bot(self):
		pass

	def send_direction(self, direction):
		print("Sendig direction")
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
		command = motorcommand(left, right)


	def parse_input(self, line):
		args = line.strip().split()
		print("Args is ")
		print(args)
		# Get the function to run from the dictionary 
		if(args[0] in self._functions):
			func = self._functions[args[0]]
			print("Func is ")
			print(func.__name__)
			print("args are")
			print(*args[1:])
			func(*args[1:])

	def run(self): 
		while 1:
			try:
				#Receive from laptop
				data = self._conn.recv(32)
				#print(data)
				try:
					if not data:
						return
					print(data)
					line = data.decode('utf-8')
					self.parse_input(line)
				
				except:
					return
				try:
					#Send to arduino nano
					#output = bytes(received, "ASCII")
					output = []
					for i in range(1,6):
					    output.append(received[i])
					radio.write(bytes(output))
					print(output)
				except:
					print("Couldn't send to nano")
			except:
			    print("\nError")
			    return
