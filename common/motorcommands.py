import socket 
import struct
import radio 

class motor_command: 

    def __init__(self, left = 0, right = 0, heartbeat = 1, id = 1):
        self._heartbeat = heartbeat
        self._id = id
        self._lefta = max(0, left)
        self._leftb  = max(0, -left)
        self._righta = max(0, right)
        self._rightb = max(0, -right)

    def send(self, radio): 
        print("Send command...")
        radio.write((self._id, self._lefta, self._leftb, self._righta, self._rightb))
       # print("%d %d %d %d %d %d" % (self._heartbeat, self._id, self._lefta, self._leftb, self._righta, self._rightb))
        # sock.sendall(struct.pack("!BBBBBB", self._heartbeat, self._id, self._lefta, self._leftb, self._righta, self._rightb))
