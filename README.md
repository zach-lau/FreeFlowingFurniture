# FreeFlowingFurniture
Software to move furniture using visual camera. This software consists of three parts. 
## 1. Software to run on pi  
The raspberry pi is the brains of the project. It has a visual camera to recognize the location of each piece of furniture and processes commands sent from the user. 
## 2. Software to run on laptop  
The laptop currently runs a command line interface that will communicate with the raspberry pi over wifi. 
## 3. Software to run on furniture microcontroller  
The microcontroller software controls the movement of the individual robot given commands from the pi. For example, they pi can command it to go forward, back, turn left or turn right. 