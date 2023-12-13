# RaspberryBox Project:

Lockers that can be automatically opened and closed only with trained human faces with face recognition and face training using opencv.

## Securing Face Datasets:
First, collect datasets for face training.

  ``python3 faceDataSet.py``

![image](https://github.com/opensource-sw-team64/TermProject/assets/95958894/2b130986-6f55-4d93-916a-4fb06e88e433)


  ![image](https://github.com/opensource-sw-team64/TermProject/assets/95958894/2cef4162-52c9-4ec1-b10b-34fccc1f2c60)


## Training:
Second, the collected datasets are used to train the face.

  ``python3 training.py``

![image](https://github.com/opensource-sw-team64/TermProject/assets/95958894/07b03a8d-103e-44b5-9edc-cf60ce2cdbe8)


## raspberryBox:
A code that configures the locker with a box that can replace the actual locker, opens the door automatically when a trained person's face is recognized, and closes the door automatically when there is no persons'face, or if it is not a trained person's face.

  ``python3 raspberryBox.py``


[Demo](https://youtu.be/wCUNufFC90k)

## Requirements:

1. python(3.x)
2. opencv(4.1.2)
3. opencv-contrib-python(4.1.2)
4. Raspberry Pi 4
5. Raspberry Pi Camera Module2
6. putty

## Raspberry Pi Setting
[Setting](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up) -> Follow the order, but see the link below for OS installation
[Os](https://munjjac.tistory.com/6) -> Follow the ssh usage, user name, and password setting
