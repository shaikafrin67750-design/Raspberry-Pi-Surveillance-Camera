# Raspberry Pi Surveillance Camera using Python

import cv2
import time
from datetime import datetime

# Start Raspberry Pi camera

camera = cv2.VideoCapture(0)

if not camera.isOpened():
print("Camera could not be opened!")
exit()

# Motion detection setup

previous_frame = None
recording = False
video_writer = None
start_time = 0

print("Raspberry Pi Surveillance Camera Started")
print("Press 'q' to exit.")

while True:
ret, frame = camera.read()

```
if not ret:
    print("Unable to read camera.")
    break

# Resize frame
frame = cv2.resize(frame, (640, 480))

# Convert frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce noise
gray = cv2.GaussianBlur(gray, (21, 21), 0)

if previous_frame is None:
    previous_frame = gray
    continue

# Calculate difference between current and previous frame
difference = cv2.absdiff(previous_frame, gray)

# Threshold the difference
_, threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

motion_detected = False

for contour in contours:
    if cv2.contourArea(
```
