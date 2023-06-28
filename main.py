# Created by Ravi Anand
# Posted on Github on 9 JAN 2023

# libraries needed
import keyboard
import mediapipe as mp
import cv2
from math import sqrt
import win32api
import pyautogui


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

rclick = 0  # right click
click = 0  # left click
dclick = 0  # double click
scroll = 0  # scroll down
# Declare a flag variable for the volume control mode
volume_control_mode = False
volume_down = 0

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    _, picture = video.read()
    image = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)
    imageHeight, imageWidth, _ = image.shape
    cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Hand Tracking', cv2.WND_PROP_TOPMOST, 1)
    # to manage smoothening according to camera quality,background disturbance
    while video.isOpened():
        if keyboard.is_pressed('a'):
            volume_control_mode = not volume_control_mode  # toggle the variable's value
        _, picture = video.read()
        image = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)

        # converting to RGB format for mediapipe

        image = cv2.flip(image, 1)

        # imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # if there is a hand present in frame
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                # iterating over all marked points in hands
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(350, 90, 190), circle_radius=3),
                                          )

        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:

                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                           normalizedLandmark.y,
                                                                                           imageWidth, imageHeight)

                    point = str(point)

                    # Storing x and y coordinates of finger landmarks in use

                    if point == 'HandLandmark.THUMB_TIP':
                        try:
                            thumbfingertip_x = pixelCoordinatesLandmark[0]
                            thumbfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass



                    elif point == 'HandLandmark.INDEX_FINGER_TIP':
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos((indexfingertip_x * 4, indexfingertip_y * 5))
                            # multiplied with 4 and 5 to adjust ratio between camera size and screen size

                        except:
                            pass

                    elif point == 'HandLandmark.INDEX_FINGER_PIP':
                        try:
                            indexfingerpip_x = pixelCoordinatesLandmark[0]
                            indexfingerpip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass


                    elif point == 'HandLandmark.RING_FINGER_TIP':
                        try:
                            ringfingertip_x = pixelCoordinatesLandmark[0]
                            ringfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.PINKY_TIP':
                        try:
                            pinkyfingertip_x = pixelCoordinatesLandmark[0]
                            pinkyfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.MIDDLE_FINGER_TIP':
                        try:
                            middlefingertip_x = pixelCoordinatesLandmark[0]
                            middlefingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == 'HandLandmark.MIDDLE_FINGER_PIP':
                        try:
                            middlefingerpip_x = pixelCoordinatesLandmark[0]
                            middlefingerpip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass


                    elif point == 'HandLandmark.THUMB_IP':
                        try:
                            thumbip_x = pixelCoordinatesLandmark[0]
                            thumbip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    # start of main operation

                if volume_control_mode == False:
                    # left click
                    try:

                        if middlefingertip_y < middlefingerpip_y and thumbfingertip_x > thumbip_x:
                            click = click + 1
                            if click % 4 == 0:
                                # this is done to avoid multiple clicks due to continously running while loop
                                print("single click")
                                pyautogui.click()
                    except:
                        pass

                    # right click
                    try:
                        Distance2 = sqrt(
                            (pinkyfingertip_x - thumbfingertip_x) ** 2 + (pinkyfingertip_y - thumbfingertip_y) ** 2)

                        if Distance2 < 20:
                            rclick = rclick + 1
                            if rclick % 2 == 0:
                                print("right click")
                                pyautogui.rightClick()

                    except:
                        pass

                    # double click
                    try:
                        if middlefingertip_y > middlefingerpip_y and thumbfingertip_x > thumbip_x:
                            dclick = dclick + 1
                            if dclick % 5 == 0:
                                print("double click")
                                pyautogui.doubleClick()


                    except:
                        pass

                    # scroll down
                    try:
                        Distance = sqrt(
                            (indexfingertip_x - thumbfingertip_x) ** 2 + (indexfingertip_y - thumbfingertip_y) ** 2)

                        if Distance < 20:
                            pyautogui.scroll(-250)



                    except:
                        pass

                    # scroll up
                    try:
                        Distance3 = sqrt(
                            (middlefingertip_x - thumbfingertip_x) ** 2 + (middlefingertip_y - thumbfingertip_y) ** 2)

                        if Distance3 < 20:
                            pyautogui.scroll(250)
                    except:
                        pass

                if volume_control_mode:
                    # Increase volume if the thumb is above the index finger
                    try:
                            if thumbfingertip_y > indexfingertip_y:
                                # Add code to increase the volume here
                                pyautogui.press('volumeup')

                            # Decrease volume if the thumb is below the index finger
                            elif thumbfingertip_y < indexfingertip_y:
                                # Add code to decrease the volume here
                                volume_down = volume_down + 1
                                if volume_down % 3 == 0:
                                   pyautogui.press('volumedown')
                    except:
                        pass





        cv2.imshow('Hand Tracking', image)



        # wait for 5 milliseconds for quitting
        # press e to exit
        if cv2.waitKey(5) & 0xFF == ord('e'):
            break

video.release()
