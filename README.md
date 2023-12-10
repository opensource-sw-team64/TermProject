# RaspberryBox Project:

Lockers that can be automatically opened and closed only with trained human faces with face recognition and face training using opencv.

## Securing Face Datasets:
First, collect datasets for face training.

  ``python3 faceDataSet.py``

## Training:
Second, the collected datasets are used to train the face.

  ``python3 training.py``

## raspberryBox:
A code that configures the locker with a box that can replace the actual locker, opens the door automatically when a trained person's face is recognized, and closes the door automatically when there is no persons'face, or if it is not a trained person's face.

  ``python3 raspberryBox.py``

## Requirements:

1. python(3.x)
2. opencv(4.1.2)
3. opencv-contrib-python(4.1.2)
4. Raspberry Pi 4
5. Raspberry Pi Camera Module2
6. putty
