# Magical-Fingers

# Opencv


[OpenCV](https://opencv.org/) is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Opencv.

```bash
pip install opencv-python
```


# Mediapipe

[MediaPipe](https://google.github.io/mediapipe/) offers cross-platform, customizable ML solutions for live and streaming media.It provides various kinds of detection features such as Face Detection , Face Mesh , Iris , Hands , Pose etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Mediapipe.

```bash
pip install mediapipe
```

# PyAutoGUI



[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) lets your Python scripts control the mouse and keyboard to automate interactions with other applications.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyAutoGUI.

```bash
pip install PyAutoGUI
```




<!-- # NumPy


[NumPy](https://numpy.org/) is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NumPy.

```bash
pip install numpy
``` -->
<!-- # Pycaw


[Pycaw](https://github.com/AndreMiras/pycaw) is the library for audio controls

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pycaw.

```bash
pip install pycaw
``` -->


## Code

```
import cv2
from math import sqrt
import win32api
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

rclick = 0  #right click
click = 0   #left click
dclick = 0  #double click
scroll = 0  #scroll down


video = cv2.VideoCapture(0)


with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    #to manage smoothening according to camera quality,background disturbance
    while video.isOpened():
        _, picture = video.read()
```

### RESULTS
<img src="https://imgur.com/I1tt2T7.gif" width="500" height="300">



# Controls


1) Cursor Mode:-Open Hand<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) Move Cursor:- Index finger acts like a mouse cursor<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Left Click:-  Point thumb inwards (towards your palm)<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) Right click:- Join little finger and thumb
    


3) Scroll:<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a) scroll up:Join index finger and thumb finger<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) scroll down:Join middle finger and thumb finger<br/>
 
<!-- ## 🔗LINK TO THE VIDEO

https://drive.google.com/file/d/1bTrFoFH_yenro0C8AjXu9_BQFtGJy3Gg/view?usp=sharing -->
