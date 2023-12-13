import cv2

# Create a video capture object and configure the camera settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width of the video frame
cap.set(4, 480)  # Set the height of the video frame

# Load the Haar Cascade model for face detection
# This model is used to detect faces in the video frame
path = '../opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml'
face_detector = cv2.CascadeClassifier(path)

# Prompt the user to enter their ID and start the face capture process
face_id = input('\n Enter user ID and press <return> ==> ')
print("\n [INFO] Initializing face capture. Look at the camera and wait ...")

# Initialize a counter for the number of face images captured
count = 0

# Main loop for continuous face detection and image capture
while True:
    # Capture frame-by-frame from the camera
    ret, img = cap.read()

    # Convert the captured image to grayscale for the face detection process
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    # Loop through all the faces found and draw rectangles around them
    # Also, save the face images to a specified directory
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around each face
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])  # Save the captured face image
        count += 1  # Increment the image count

    # Display the resulting frame with detected faces in a window
    cv2.imshow('image', img)

    # Break the loop if 'ESC' key is pressed
    k = cv2.waitKey(100) & 0xff
    if k == 27:  # 27 is the ASCII code for the ESC key
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
