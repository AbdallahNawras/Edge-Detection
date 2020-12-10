# Edge-Detection
Abdallah Nawras
12/02/2020

Canny edge detection
the Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.


Instructions
Installing python and libraries 

Python version: python 3.75

Required libraries to install:
numpy
matplotlib
opencv-python
opencv-contrib-python 

use terminal
		1. Install pip using following link
		https://phoenixnap.com/kb/install-pip-windows
		2. installing packages
                            Open the terminal and type this command 
 			Pip3 install yourpackage
Ex: pip3 install numpy
      Pip3 install opencv-python


Run the code 


Using webcam: 
Change the line number 26 to follow
	cap = cv2.VideoCapture(0)

Using USB camera: 
cap = cv2.VideoCapture(1)


Use terminal without IDE
Open cmd and navigate(cd) to the project location and the type 
	Python3 real-time_edge_detect.py
