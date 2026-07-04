import cv2, time, pyautogui
import mediaPipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


SCROLL_SPEED = 300
SCROOL_DELAY = 1
CAM-WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    
    for tips in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)