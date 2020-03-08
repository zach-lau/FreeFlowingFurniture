#System libraries
import sys
sys.path.insert(1, '../common')
import socket

#User libraries
from motorcommands import *

def parseInput(line): 
	# Turns a users command line input into an appropriate integer output
	# If the command is not valid it will output 0 and notify the user of an unrecognized command
	max_out = 200
	if line == "forward": 
		left = max_out
		right = max_out
	elif line == "right":
		left = -max_out
		right = max_out
	elif line == "left":
		left = max_out
		right = -max_out
	elif line == "back": 
		left = -max_out
		right = -max_out
	else: 
		left = 0
		right = 0
		print("Unrecognized command")
	return (left, right)

def cli(sock):
	# A command line interface that talks with the server
	# sock : socket to communicate with 
	line = input()
	# left : left motor pwm from -255 to 255
	# right : right motor pwm from -255 to 255

	while line:
		left, right = parseInput(line)
		command = motor_command(left, right)
		try: 
			command.send(sock)
		except:
			print("Unable to send command")
		#sock.sendall(bytes(line, 'utf-8'))
		line = str(input())
	sock.close()
	print("Closing client")