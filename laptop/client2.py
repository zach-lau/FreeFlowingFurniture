#!/usr/bin/python3
import tkinter as tk
import socket

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

def cli(sock):
	# A command line interface that talks with the server
	# sock : socket to communicate with 
	line = input()
	while line:
		sock.sendall(bytes(line, 'utf-8'))
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