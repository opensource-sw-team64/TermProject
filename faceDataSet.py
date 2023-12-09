import cv2

# 비디오 캡처 객체 생성 및 카메라 설정
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
