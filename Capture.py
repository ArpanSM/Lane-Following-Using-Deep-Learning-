# used the code mentioned below to capture a series of images at an interval of .5 seconds. 
#Then you place the robot at different positions on the track and capture a series of images.
#capture the images for the three directions, place them in separate folders with names forward, 
#left, and right respectively.


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480) # set the resolution
camera.framerate = 32 # set the frame rate
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warm up
time.sleep(0.1)
 
# capture frames from the camera
start = 1
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  # grab the raw NumPy array representing the image, then initialize the timestamp and occupied/unoccupied text
  image = frame.array
  # show the frame
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF
  cv2.imwrite(str(start) + ".jpg", image)
  start = start + 1
 
  # clear the stream in preparation for the next frame
  rawCapture.truncate(0)
 
  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break
  time.sleep(.5)