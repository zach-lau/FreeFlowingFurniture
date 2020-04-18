#System libraries
import sys
sys.path.insert(1, '../common')
import socket

# #User libraries
# from motorcommands import *


class cli:
	
	def __init__(self, sock):
		self._sock = sock

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