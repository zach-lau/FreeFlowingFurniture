CC = g++
FLAGS = `pkg-config opencv --cflags --libs`

all:
	@${CC} detectMarker.cpp -o aruco ${FLAGS}
	