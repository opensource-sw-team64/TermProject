import cv2

# 비디오 캡처 객체 생성 및 카메라 설정
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

# Load the Haar Cascade model for face detection
path = '../opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml'
face_detector = cv2.CascadeClassifier(path)

# Get user ID input and print initialization message
face_id = input('\n enter user id end press <return> ==> ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
