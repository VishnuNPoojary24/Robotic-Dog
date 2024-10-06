import time
from adafruit_servokit import ServoKit

# Initialize 16-channel PWM controller
kit = ServoKit(channels=16)

# Functions to control the servo motors
def sit():
    print("Sitting...")
    # Adjust angles for each leg servo
    kit.servo[0].angle = 90   # Front-left upper
    kit.servo[1].angle = 120  # Front-left lower
    kit.servo[2].angle = 90   # Front-right upper
    kit.servo[3].angle = 120  # Front-right lower
    kit.servo[4].angle = 90   # Back-left upper
    kit.servo[5].angle = 120  # Back-left lower
    kit.servo[6].angle = 90   # Back-right upper
    kit.servo[7].angle = 120  # Back-right lower
    time.sleep(1)

def stand():
    print("Standing...")
    # Set servos for a standing position
    for i in range(8):
        kit.servo[i].angle = 90
    time.sleep(1)

def wag_tail():
    print("Wagging tail...")
    for _ in range(5):
        kit.servo[9].angle = 45  # Wag left
        time.sleep(0.5)
        kit.servo[9].angle = 135  # Wag right
        time.sleep(0.5)

def nod_head():
    print("Nodding head...")
    kit.servo[8].angle = 30   # Tilt head down
    time.sleep(0.5)
    kit.servo[8].angle = 90   # Return to neutral
    time.sleep(0.5)
    kit.servo[8].angle = 150  # Tilt head up
    time.sleep(0.5)
    kit.servo[8].angle = 90   # Return to neutral
    time.sleep(0.5)

def walk():
    print("Walking...")
    for _ in range(5):
        kit.servo[0].angle = 60
        kit.servo[1].angle = 120
        kit.servo[2].angle = 120
        kit.servo[3].angle = 60
        kit.servo[4].angle = 120
        kit.servo[5].angle = 60
        kit.servo[6].angle = 60
        kit.servo[7].angle = 120
        time.sleep(0.5)
        kit.servo[0].angle = 120
        kit.servo[1].angle = 60
        kit.servo[2].angle = 60
        kit.servo[3].angle = 120
        kit.servo[4].angle = 60
        kit.servo[5].angle = 120
        kit.servo[6].angle = 120
        kit.servo[7].angle = 60
        time.sleep(0.5)

if __name__ == "__main__":
    # Test all actions individually
    sit()
    stand()
    wag_tail()
    nod_head()
    walk()
