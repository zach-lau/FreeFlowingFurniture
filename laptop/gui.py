#System libraries
import tkinter as tk 
import sys
sys.path.insert(1, '../common')
import socket
from cli import *

#User libraries
from motorcommands import *

key_to_command = {38: "left", 25: "forward", 40: "right", 39: "back", 65: "stop"}

class gui: 
    def __init__(self, socket):
        self._cli = cli(socket)
        pass

    def key_press(self, event):
        try:    
            input = key_to_command[event.keycode]
        except:
            input = "stop"
        self._cli.send_direction(input)
    
    def key_release(self, event):
        self._cli.send_direction("stop")

    def mainloop(self): 
        root = tk.Tk()
        label = tk.Label(text = "GUI", width = 100, height = 40)
        label.pack()
        root.bind('<KeyPress>', self.key_press)
        #root.bind('<KeyRelease>', self.key_release)
        root.mainloop()
