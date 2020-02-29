# FreeFlowingFurniture
Software to move furniture using visual camera. The FFF project is now in its beginning stages. 
This software consists of three parts.
## 1. Software to run on pi  
The raspberry pi is the brains of the project. It has a visual camera to recognize the location of each piece of furniture and processes commands sent from the user. 
Currently this is set up for testing purposes. Go to the pi directory and edit hte IPADDRESS to the ip address of your pi. Then run `python server2.py` to start a server. 
## 2. Software to run on laptop  
The laptop currently runs a command line interface that will communicate with the raspberry pi over wifi.  
From the laptop you can connect to the pi by chaging to laptop/NetworkTests and running `python3 client2.py` after updating the ip address in the file. Anything typed in the terminal will be printed to the client console.
## 3. Software to run on furniture microcontroller  
The microcontroller software controls the movement of the individual robot given commands from the pi. For example, they pi can command it to go forward, back, turn left or turn right.
