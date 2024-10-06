# obstacle_avoidance.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 23  # Example GPIO pin for trigger
ECHO = 24  # Example GPIO pin for echo

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Calculate the distance from an object
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2
    return distance

def avoid_obstacle():
    if distance() < 20:
        print("Obstacle detected! Avoiding...")
        # Example: Stop movement or redirect
        servo_control.stand()
        servo_control.walk()
