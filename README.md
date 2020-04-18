# FreeFlowingFurniture
Software to move furniture using visual camera. For a full description of the project pleaes seee the "Final Design Specification". Unfortunately work on the project was halted due to COVID-19. In its current form the software developed allows the user to manally control one of up to 10 robots using their keyboard. Using the command line interface they can control up to 255 different robots.  
This software consists of three parts.
## 1. Software to run on pi  
The raspberry pi is the brains of the project. It has a visual camera to recognize the location of each piece of furniture and processes commands sent from the user. 
Currently this is set up for testing purposes. Go to the pi directory and edit hte IPADDRESS to the ip address of your pi. Then run `python server2.py` to start a server. 
## 2. Software to run on laptop  
The laptop has a CLI and a GUI that can communicate with the raspberry pi over wifi.  
To run CLI from the laptop you can connect to the pi by chaging to laptop/NetworkTests and running `python3 client2.py` after updating the ip address in the file. Anything typed in the terminal will be printed to the client console. 
To run GUI from laptop run `python3 client2.py gui`. 
## 3. Software to run on furniture microcontroller  
The microcontroller software controls the movement of the individual robot given commands from the pi. For example, they pi can command it to go forward, back, turn left or turn right.
