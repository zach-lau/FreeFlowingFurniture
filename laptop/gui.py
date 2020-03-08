#System libraries
import tkinter as tk 
import sys
sys.path.insert(1, '../common')
import socket
from cli import *

#User libraries
from motorcommands import *

commands = {38: "left", 25: "forward", 40: "right", 39: "back", 65: "stop"}

class gui: 
    def __init__(self, socket):
        self._socket = socket
        pass

    def key_press(self, event):
        try:    
            input = commands[event.keycode]
        except:
            input = "stop"
        left, right = parseInput(input)
        command = motor_command(left, right)
        try: 
            command.send(self._socket)
        except:
            print("Unable to send command")
    
    def key_release(self, event):
        command = motor_command(0,0)
        try: 
            command.send(self._socket)
        except:
            print("Unable to send command")

    def mainloop(self): 
        root = tk.Tk()
        label = tk.Label(text = "GUI", width = 100, height = 40)
        label.pack()
        root.bind('<KeyPress>', self.key_press)
        #root.bind('<KeyRelease>', self.key_release)
        root.mainloop()
