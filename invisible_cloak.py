import cv2
import numpy as np


cap = cv2.VideoCapture(0)


background = cv2.imread(r"#Enter path to your background image")


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cam_aspect = frame_width / frame_height


h, w = background.shape[:2]
bg_aspect = w / h

if bg_aspect > cam_aspect:
    
    new_height = frame_height
    new_width = int(bg_aspect * new_height)
    resized_bg = cv2.resize(background, (new_width, new_height))
    start_x = (new_width - frame_width) // 2
    background = resized_bg[:, start_x:start_x + frame_width]

else:
    
    new_width = frame_width
    new_height = int(new_width / bg_aspect)
    resized_bg = cv2.resize(background, (new_width, new_height))
    start_y = (new_height - frame_height) // 2
    background = resized_bg[start_y:start_y + frame_height, :]


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    
    mask_inv = cv2.bitwise_not(mask)

    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

