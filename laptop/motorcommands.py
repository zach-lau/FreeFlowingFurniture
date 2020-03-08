import socket 
import struct

class motor_command: 
    def __init__(self, left = 0, right = 0, heartbeat = 1):
        self._heartbeat = heartbeat
        self._lefta = max(0, left)
        self._leftb  = max(0, -left)
        self._righta = max(0, right)
        self._rightb = max(0, -right)

    def send(self, socket): 
        print("Trying to send...")
        socket.sendall(struct.pack('!ii', self._lefta, self._leftb)) #, self._righta, self._rightb))