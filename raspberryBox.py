import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
import time

motor = 16

recognizer = cv2.face.LBPHFaceRecognizer_create()
# yml 파일 read
recognizer.read('trainer/trainer.yml')
# haarcascade read
path = '../opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(path)
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# servoMotor function
def servoMotor(pin, degree, t):
    GPIO.setmode(GPIO.BOARD) # Set pin numbering to board reference, BCM refers to GPIO numbering
    GPIO.setup(pin, GPIO.OUT) # Set the pin for GPIO communication
    pwm = GPIO.PWM(pin, 50) # Servo motor uses PWM. Set pin 16 to a frequency of 50Hz

    pwm.start(3) # Initial start value, must be entered

    pwm.ChangeDutyCycle(degree) # Normally, values between 2 to 12 should be entered
    time.sleep(t) # Enter enough time for the servo motor to move. Too small a value may cause it to stop mid-motion

    # Clean up with the following two lines to prevent runtime errors in subsequent executions
    pwm.stop()
    GPIO.cleanup(pin)

open=False
while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1) # Flip vertically, horizontally
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gray scale
    
    # face detection
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )
    # draw rectangle on detected face image
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        # Confidence = 0 -> perfect matching
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # If box is closed and can recognize the user -> open the box
        if (not open and confidence < 75):
            open = True
            servoMotor(16, 11.0, 1) # open motor
            # Maintain open status for 5 seconds
            time.sleep(5)

