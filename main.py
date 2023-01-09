# Created by Ravi Anand
# Posted on Github on 9 JAN 2023

# libraries needed
import mediapipe as mp
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
        image = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)

        #converting to RGB format for mediapipe

        image = cv2.flip(image, 1)

        imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # if there is a hand present in frame
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                #iterating over all marked points in hands
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

                    #Storing x and y coordinates of finger landmarks in use

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
                            #multiplied with 4 and 5 to adjust ratio between camera size and screen size

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

                   #start of main operation


                   #left click
                    try:

                        if middlefingertip_y < middlefingerpip_y  and thumbfingertip_x > thumbip_x :
                            click = click + 1
                            if click % 30 == 0:
                                #this is done to avoid multiple clicks due to continously running while loop
                                print("single click")
                                pyautogui.click()
                    except:
                        pass

                    #right click
                    try:
                        Distance2 = sqrt(
                            (pinkyfingertip_x - thumbfingertip_x) ** 2 + (pinkyfingertip_y - thumbfingertip_y) ** 2)

                        if Distance2 < 20:
                            rclick = rclick + 1
                            if rclick % 20 == 0:
                                print("right click")
                                pyautogui.rightClick()

                    except:
                        pass

                    # double click
                    try:
                        if middlefingertip_y > middlefingerpip_y and thumbfingertip_x > thumbip_x:
                            dclick = dclick + 1
                            if dclick % 80 == 0:
                                print("double click")
                                pyautogui.doubleClick()


                    except:
                        pass

                    #scroll down
                    try:
                        Distance = sqrt(
                            (indexfingertip_x - thumbfingertip_x) ** 2 + (indexfingertip_y - thumbfingertip_y) ** 2)

                        if Distance < 20:
                            pyautogui.scroll(-100)



                    except:
                        pass

                    #scroll up
                    try:
                        Distance3 = sqrt(
                            (middlefingertip_x - thumbfingertip_x) ** 2 + (middlefingertip_y - thumbfingertip_y) ** 2)

                        if Distance3 < 20:
                            pyautogui.scroll(100)



                    except:
                        pass







        cv2.imshow('Hand Tracking', image)

        #wait for 5 milliseconds for quitting
        #press e to exit
        if cv2.waitKey(5) & 0xFF == ord('e'):
            break

video.release()
