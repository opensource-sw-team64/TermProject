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

# Main loop for face detection and image saving
count = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        count += 1

    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

