import cv2
from ultralytics import YOLO
import pygame
import pandas as pd
import datetime
import os
import math
import numpy as np
import config

# ================= SETUP =================

model = YOLO("yolov8n.pt")

# VIDEO INPUT (make sure videos/demo.mp4 exists)
cap = cv2.VideoCapture("videos/demo.mp4")
print("VIDEO STATUS:", cap.isOpened())

# Line parameters
line_x = 400
line_y = 300
angle = 90          # degrees (90 = vertical)
length = 2000
thickness = 2
detect = True

# Sound
pygame.mixer.init()
pygame.mixer.music.load("sounds/alert.wav")

# Folders
os.makedirs("screenshots", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logfile = "logs/violations.csv"
if not os.path.exists(logfile):
    pd.DataFrame(columns=["Time"]).to_csv(logfile, index=False)

# ================= MAIN LOOP =================

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    danger = False

    # --------- Compute Rotated Line ----------
    rad = math.radians(angle)

    lx1 = int(line_x - length * math.cos(rad))
    ly1 = int(line_y - length * math.sin(rad))
    lx2 = int(line_x + length * math.cos(rad))
    ly2 = int(line_y + length * math.sin(rad))

    # Draw safety line
    cv2.line(frame, (lx1, ly1), (lx2, ly2), (0, 255, 0), thickness)

    # --------- Detection ----------
    if detect:
        results = model(frame, classes=[0], conf=config.CONFIDENCE)

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                # Cross product sign -> which side of line
                side = (lx2 - lx1) * (cy - ly1) - (ly2 - ly1) * (cx - lx1)

                # LEFT side = RED ZONE
                if side > 0:
                    danger = True
                    color = (0, 0, 255)
                else:
                    color = (0, 255, 0)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # --------- Dynamic Rotated RED ZONE ----------
    mask = frame.copy()

    # Image corners
    corners = [(0,0), (w,0), (w,h), (0,h)]
    red_pts = []

    # Keep corners that lie on RED side
    for pt in corners:
        side = (lx2 - lx1) * (pt[1] - ly1) - (ly2 - ly1) * (pt[0] - lx1)
        if side > 0:
            red_pts.append(pt)

    # Add line endpoints to close polygon
    red_pts.append((lx1, ly1))
    red_pts.append((lx2, ly2))

    if len(red_pts) >= 3:
        cv2.fillPoly(mask, [np.array(red_pts, np.int32)], (0, 0, 255))
        frame = cv2.addWeighted(mask, 0.15, frame, 0.85, 0)

    cv2.putText(frame, "RED ZONE", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # --------- Alert + Log ----------
    if danger:
        cv2.putText(frame, "MOVE TO SAFE SIDE!",
                    (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

        pygame.mixer.music.play()

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # CSV log
        pd.DataFrame([[now]]).to_csv(logfile, mode='a',
                                     header=False, index=False)

        # Screenshot
        cv2.imwrite(f"screenshots/{now}.jpg", frame)

    cv2.imshow("Railway Safety System", frame)

    # --------- Controls ----------
    k = cv2.waitKey(1) & 0xFF

    if k == ord('q'):
        break

    # Move line
    if k == ord('a'): line_x -= 5
    if k == ord('d'): line_x += 5
    if k == ord('w'): line_y -= 5
    if k == ord('s'): line_y += 5

    # Rotate line
    if k == ord('e'): angle += 2     # clockwise
    if k == ord('r'): angle -= 2     # anti-clockwise

    # Other
    if k == ord('z'): thickness += 1
    if k == ord('t'): detect = not detect

cap.release()
cv2.destroyAllWindows()



