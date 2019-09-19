import RPi.GPIO as GPIO
#choose the GPIO pins
fwd1 = 18  # pin 12
bwd1 = 24 #pin 18
fwd2 = 12 # pin 32
bwd2 = 20 # pin 38
# declare selected pin as output pin


GPIO.setmode(GPIO.BCM)
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)
sleep_time = .2

def forward():
  GPIO.output(fwd1, GPIO.HIGH)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.HIGH)
  GPIO.output(bwd2, GPIO.LOW)
def backward():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.HIGH)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.HIGH)
def left():
  GPIO.output(fwd1, GPIO.HIGH)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.LOW)
def right():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.HIGH)
  GPIO.output(bwd2, GPIO.LOW)
def stop():
  GPIO.output(fwd1, GPIO.LOW)
  GPIO.output(bwd1, GPIO.LOW)
  GPIO.output(fwd2, GPIO.LOW)
  GPIO.output(bwd2, GPIO.LOW)