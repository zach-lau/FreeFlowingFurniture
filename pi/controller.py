# Controlls the pi and parses inputs

import socket 

class controller:
    
    def __init__(self, connection):
        self._conn = connection

    def run(self): 
        try:
            #Receive from laptop
            data = self._conn.recv(32)
            #print(data)
            try:
                print(data)
                if not data:
                    return
            except:
                print("Couldn't parse data")
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