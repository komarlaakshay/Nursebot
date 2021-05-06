# Nursebot
Its a robot nurse prototype which can be controlled through Bluetooth and is designed to dispense the tablets based on the patient identity which is detected by the face recognition algorithm

## The Idea
This pandemic Doctor and Nurses have given the best for the society
But they cannot be there every time as there is a difference in the ratio of patients and the doctor/nurses in order to assist them we have created this prototype which can detect the patient face and dispense the tablets prescribed by the doctor. 

## Components Required 
1) [ ] Raspberry pi 3B+

2)Raspberry picam

3)Arduino 

4)SG90 Servo

5)L293d motor driver module 

6)60 RPM BO Motor

7)Blutooth(HC-05)

8)Robot chassis

9)Connecting wires

10)Castor wheel

11)Foam Board

12)Batteries 9V
## Software required
Rasbian for pi

## Main Python Packages
1)pickle

2)PIL

3)CV2

4)eel

5)googleapiclient.discovery

6)google.oauth2


## Procedure
These are the steps to be followed
1)Build the chassis for the robot with 2 geared motor with wheels and a Castrol wheel, make the Bluetooth, Motor connections to the Arduino. We are using a Bluetooth control app to move the robot.

2)Download the openCV library for python and write a code to implement Facial recognition. Face recognition identifies faces and displays the name of the person. A small Raspberry Pi cam can be used for this purpose. The camera takes a specified number of photos.  A record of the person’s photos is maintained in a folder. These photos are used for the identifiaction of the patient for dispencing the tablet.

3) Now we use an API tool called Google Sheets. In this, we stored the data of the user, mainly their name and the number of tablets. We do this by creating a service account. The procedure to that can be found in the following link.

4) Then we have to create a GUI. We did this using HTML, CSS, JAVASCRIPT, and a python library called eel. The library is efficient and also we can create an easy-to-use GUI. The links to that will be given below.

## Working
The robot is controlled using Bluetooth and taken to the patient and the robot detects the patient identity and searches for the name in the google sheets and decides the number of tablets and dispenses the tablet by activating the servos. we can automate the robot control using the ROS but for now this is just a prototype to show the concept.

## Referance Links
EEL Library
https://medium.com/wronmbertech/create-html-user-interface-for-python-using-eel-library-bab101cc0f99

HTML
https://www.w3schools.com/howto/howto_make_a_website.asp

Google Sheets API
https://developers.google.com/sheets/api/quickstart/python

Open CV
https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/

PiCam Setting Up
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera


