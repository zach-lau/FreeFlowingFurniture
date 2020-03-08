#!/usr/bin/python3
import sys
sys.path.insert(1, '../common')
import tkinter as tk
import socket
from motorcommands import *

SERVER_ADDRESS = "192.168.1.65"

def connect(server_address):
	# Connect to the server at the given address
	# server_address : local ip of the server
	# return : The socket if successful, None if could not connect 
	try:
		#Connect to the pi 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((server_address, 5005))
		return s
	except: 
		print("Error making socket")
		return None

def parseInput(line): 
	# Turns a users command line input into an appropriate integer output
	# If the command is not valid it will output 0 and notify the user of an unrecognized command

	if line == "forward": 
		left = 255
		right = 255
	elif line == "right":
		left = -255
		right = 255
	elif line == "left":
		left = 255
		right = -255
	elif line == "back": 
		left = -255
		right = -255
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

def main(): 
	print("Connecting to server...")
	s = connect(SERVER_ADDRESS)
	if s == None:
		return 
	print("Connected to server")

	#Everything from here out uses the server
	try: 
		cli(s)
	except:
		s.close()	


if __name__ == '__main__':
	main()
	print("Terminating program")