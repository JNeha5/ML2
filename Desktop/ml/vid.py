import cv2
import sys

video_path = "video.mp4"

# Open the video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Could not open video {video_path}")
    sys.exit()

# Get FPS (fallback if 0)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 25  # default FPS if unknown
wait_time = int(1000 / fps)

print("Press 'q' to quit the video player.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video reached.")
        break

    cv2.imshow("Video", frame)

    # Wait for key; break if 'q' is pressed
    key = cv2.waitKey(wait_time) & 0xFF
    if key == ord('q'):
        print("Video stopped by user.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)  # ensure window closes properly
