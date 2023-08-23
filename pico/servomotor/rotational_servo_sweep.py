import time
from servo import Servo

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=16)

while True:
    my_servo.write(90)  # Set the Servo to the mid-point (90 is half way between zero and 180 degrees)
    time.sleep_ms(1000)  # Wait for 1 second
    
    my_servo.write(0)  # Set the Servo to the left most position
    time.sleep_ms(1000)  # Wait for 1 second
    
    my_servo.write(180)  # Set the Servo to the right most position
    time.sleep_ms(1000)  # Wait for 1 second