# robotic_dog_controller.py
import voice_recognition
import command_processor
import obstacle_avoidance
import led_control
import time

try:
    while True:
        if obstacle_avoidance.distance() < 20:
            obstacle_avoidance.avoid_obstacle()
        command = voice_recognition.recognize_speech()
        if command:
            command_processor.process_command(command)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    led_control.cleanup()
    print("GPIO cleaned up and program ended.")
