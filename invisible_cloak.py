import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Load background image
background = cv2.imread(r"C:\Users\Aadarsh\Desktop\Python Projects\Invisible Cloak\background.jpg")

# Get webcam resolution
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cam_aspect = frame_width / frame_height

# Resize background while keeping aspect ratio
h, w = background.shape[:2]
bg_aspect = w / h

if bg_aspect > cam_aspect:
    # Background is wider than webcam → fit height, crop width
    new_height = frame_height
    new_width = int(bg_aspect * new_height)
    resized_bg = cv2.resize(background, (new_width, new_height))
    start_x = (new_width - frame_width) // 2
    background = resized_bg[:, start_x:start_x + frame_width]
else:
    # Background is taller → fit width, crop height
    new_width = frame_width
    new_height = int(new_width / bg_aspect)
    resized_bg = cv2.resize(background, (new_width, new_height))
    start_y = (new_height - frame_height) // 2
    background = resized_bg[start_y:start_y + frame_height, :]

print("Background image loaded & ready! Wear your cloak...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Do NOT flip (your background is already inverted)
    # frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define improved red cloak color range
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])


    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Clean mask with bigger kernel
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Invert mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract cloak area from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Extract non-cloak area from current frame
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Merge both
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
