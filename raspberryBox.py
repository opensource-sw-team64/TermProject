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

# servoMotor 함수
def servoMotor(pin, degree, t):
    GPIO.setmode(GPIO.BOARD) # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
    GPIO.setup(pin, GPIO.OUT) # GPIO 통신할 핀 설정
    pwm=GPIO.PWM(pin, 50) # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정

    pwm.start(3) # 초기 시작값, 반드시 입력해야됨

    pwm.ChangeDutyCycle(degree) # 보통 2~12 사이의 값을 입력하면됨
    time.sleep(t) # 서보모터가 이동할만큼의 충분한 시간을 입력. 너무 작은 값을 입력하면 이동하다가 멈춤

    # 아래 두줄로 깨끗하게 정리해줘야 다음번 실행할때 런타임 에러가 안남
    pwm.stop()
    GPIO.cleanup(pin)
