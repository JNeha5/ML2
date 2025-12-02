import urllib.request
import numpy as np
import cv2

url = "https://plus.unsplash.com/premium_photo-1683910767532-3a25b821f7ae?q=80&w=508&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# 1. Download image bytes
with urllib.request.urlopen(url) as resp:
    image_bytes = resp.read()

# 2. Convert bytes to numpy array
image_array = np.asarray(bytearray(image_bytes), dtype="uint8")

# 3. Decode image with OpenCV
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

if image is not None:
    print("Image loaded, shape:", image.shape)
    # optionally show / process image
else:
    print("Could not decode image")
