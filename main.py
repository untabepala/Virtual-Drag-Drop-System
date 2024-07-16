import cv2
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

# Rectangle position and size
cx, cy, w, h = 150, 150, 200, 200

while True:
    success, img = video.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)
    lmList = []  # Initialize lmList to ensure it is always defined

    if hands:
        lmList = hands[0]['lmList']

    if lmList:
        #l, _, _ = detector.findDistance(8, 12, img)[0] < 30
        cursor = lmList[8]
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            colorR = (0, 255, 0)
            # Update rectangle position
            cx, cy = cursor[0], cursor[1]
            # Boundary checks to keep the rectangle within the frame
            cx = max(w // 2, min(cx, img.shape[1] - w // 2))
            cy = max(h // 2, min(cy, img.shape[0] - h // 2))
        else:
            colorR = (255, 0, 255)

    cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)

    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Release the video capture and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
