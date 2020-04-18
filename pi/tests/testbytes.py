import struct
send = (1,3,4,5)
val = struct.pack("BBBB", *send)
print(val)