## 🧥 Invisible Cloak Project (OpenCV + Python)

This project recreates the famous “invisibility cloak” effect from Harry Potter ⚡ using Python, OpenCV, and NumPy.
When a red cloak (or any chosen color) is worn in front of the camera, that area becomes invisible and is replaced with the background.

# 📌 Features
- Real-time invisibility cloak effect using webcam.
- Replace cloak area with a custom background image.
- Adjustable HSV color ranges for different cloak colors.
- Morphological operations to remove noise.
- Lightweight, works on any system with Python + OpenCV.

# 🛠 Requirements
- Install dependencies from requirements.txt: pip install -r requirements.txt
- requirements.txt: opencv-python numpy

# 📂 Project Structure
Invisible-Cloak/
│── invisible_cloak.py      # Main project file
│── hsv_calibration.py      # Helper script to tune HSV ranges
│── background.jpg          # Background image
│── requirements.txt        # Dependencies
│── README.md               # Documentation


# ▶️ How to Run
- Clone / Download this repository
- Install dependencies: pip install -r requirements.txt
- Place your background image in the project folder.
- Example: background.jpg (use a 16:9 image for best results).
- Run the script: python invisible_cloak.py
- Wear a red cloak / cloth (or any color you tuned for).
- Press q to quit.

# ⚙️ How It Works
- Capture the live video from webcam.
- Convert each frame from BGR → HSV color space.
- Create a mask for the cloak’s color using HSV thresholds.
- Clean the mask with morphological operations (remove noise).
- Replace cloak area with the background image.
- Combine cloak area (from background) + non-cloak area (from webcam).




# 🚀 Applications
- Fun AR effects & live video filters.
- Background replacement in video calls.
- Learning project for OpenCV basics (masks, color detection, bitwise operations).
- Can be extended into AR/VR projects.


# Author
Aadarsh Jha | Linkedin : www.linkedin.com/in/aadarshjha09
