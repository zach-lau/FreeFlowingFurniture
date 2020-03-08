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
		return None

def main(): 
	s = connect(SERVER_ADDRESS)
	if s == None:
		return 
	line = input()
	while line:
		s.sendall(bytes(line, 'utf-8'))
		line = str(input())
	s.close()
	print("Closing client")


if __name__ == '__main___':
	main()