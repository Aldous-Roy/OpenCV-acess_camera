OpenCV Webcam Capture

This repository contains a Python script that uses OpenCV to capture and display video from a webcam. The script is designed to work with the default webcam (index 0) or an external webcam (index 1) on macOS.

Prerequisites

	1.	Python 3.x: Ensure you have Python 3 installed. You can download it from the official Python website.
	2.	OpenCV: Install the OpenCV library. You can do this using pip:
 pip install opencv-python
 Webcam Script
 The script cam.py opens a video capture stream from a specified webcam device and displays it in a window. You can press the q key to stop the video stream and close the window.
 If you want to use the default webcam (usually the internal webcam), use index 0
 If you want to use an external webcam, try index 1
 In my case the index 1 works feel free to change
 
