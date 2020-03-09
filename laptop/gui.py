#System libraries
import tkinter as tk 
import sys
sys.path.insert(1, '../common')
import socket
from cli import *

#User libraries
# from motorcommands import *

key_to_direction = {
    38: "left", 
    25: "forward", 
    40: "right", 
    39: "back", 
    65: "stop",
    }

numbers = {
    19 : 0, 
    10 : 1, 
    11 : 2, 
    12 : 3, 
    13 : 4, 
    14 : 5, 
    15 : 6, 
    16 : 7, 
    17 : 8, 
    18 : 9
}
class gui: 
    def __init__(self, socket):
        self._cli = cli(socket)
        pass

    def key_press(self, event):
        keycode = event.keycode
        try:   
            print(keycode) 
            if keycode in key_to_direction:
                input = key_to_direction[event.keycode]
            elif keycode in numbers:
                input = "set_bot %d" % numbers[event.keycode]
            else:
                input = "stop"
        except:
            input = "stop"
        self._cli.send(input)
    
    def key_release(self, event):
        self._cli.send(input)

    def run(self): 
        root = tk.Tk()
        label = tk.Label(text = "GUI", width = 100, height = 40)
        label.pack()
        root.bind('<KeyPress>', self.key_press)
        #root.bind('<KeyRelease>', self.key_release)
        root.mainloop()
