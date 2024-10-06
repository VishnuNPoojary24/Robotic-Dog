# led_control.py
import RPi.GPIO as GPIO
import time

LED_PIN = 17  # Example GPIO pin for LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink_led():
    GPIO.output(LED_PIN, True)
    time.sleep(0.5)
    GPIO.output(LED_PIN, False)
    time.sleep(0.5)

# Ensure proper cleanup of GPIO on program exit
def cleanup():
    GPIO.cleanup()
