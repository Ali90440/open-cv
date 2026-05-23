import cv2
import numpy as np

def apply_filters(image, ftype):
    """Apply a filter to the image based on the filter type."""
    img= image.copy()
    if ftype == 'red tint':
        img[:, :, 1] = img[:, :, 0] = 0
    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == "blue_tint" :
        img[:, :, 1] = img[:, :, 2] = 0
    
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: camera couldn't not be opened.")
        return
    ftype = "original"
    print("Keys: r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t= Cartoon, q=Quit")
    while True:
        ret, frame= cap.read()
        if not ret:
            print("Cant recieve frame")
            break
        out = apply_filters(frame, ftype)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r '):
            ftype = "red tint"
        elif key == ord('g'):
            ftype = "green tint"
        elif key == ord('b'):
            ftype = "blue tint"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()