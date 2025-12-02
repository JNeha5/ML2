import cv2

# Path to your uploaded image
image_path = r"/mnt/data/6250a68e-ab7f-419b-9d43-5c467418415c.jpeg"

# Read the image
image = cv2.imread(image_path)

# Check if the image was loaded
if image is not None:
    print("Image shape:", image.shape)  # (height, width, channels)
else:
    print("Could not read image")
