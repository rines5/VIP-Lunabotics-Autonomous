import cv2
from matplotlib import pyplot as plt

# xml file needs to be changed for what Lunabotics club intends to detect
data = cv2.CascadeClassifier('haarcascade_eye.xml')  # change of xml file takes place here

# citation: openCV tutorial by Augmented Startups
vid = cv2.VideoCapture(0)
if not vid.isOpened():
    exit()

while True:
    ret, img = vid.read()
    if not ret:
        break

    # adapting code from object detection from still image (parts from citation above)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    found = data.detectMultiScale(img_gray, minSize=(20, 20))

    if len(found) != 0:
        for(x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x, y), (x+width, y+height), (255, 0, 0), 2)
            cv2.imshow('Object Detection Example', img_rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
