import time
from servo import Servo

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=0)

while True:
   my_servo.writeMicroseconds(1000)
