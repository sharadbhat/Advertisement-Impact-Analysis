import cv2

camera_port = 0

ramp_frames = 30
 
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
    a, im = camera.read()
    return im

for i in range(ramp_frames):
    temp = get_image()
print("Taking image...")

camera_capture = get_image()
file = "image.jpg"

cv2.imwrite(file, camera_capture)

del(camera)
