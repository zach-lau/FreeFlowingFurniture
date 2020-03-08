#!/usr/bin/python3

#System libraries 
import sys
sys.path.insert(1, '../common')
import socket
import tkinter as tk

#User libraries
from motorcommands import *
from cli import *
from gui import *

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

def main(): 
	print("Connecting to server...")
	s = connect(SERVER_ADDRESS)
	if s == None:
		return 
	print("Connected to server")

	#Everything from here out uses the server
	try:
		print("Running gui")
		g = gui(s)
		g.mainloop() 
		# print("Starting cli")
		# cli(s)
	except:
		s.close()	


if __name__ == '__main__':
	main()
	print("Terminating program")