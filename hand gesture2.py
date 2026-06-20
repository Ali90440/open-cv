import cv2, mediapipe as mp, numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP  

try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volct1 = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volct1.GetVolumeRange()[:2]
except Exception as e:
    print(f"Audio device error: {e}") exit()