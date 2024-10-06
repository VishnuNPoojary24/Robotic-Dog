# command_processor.py
import servo_control
import led_control

def process_command(command):
    if "sit" in command:
        servo_control.sit()
    elif "stand" in command:
        servo_control.stand()
    elif "walk" in command:
        servo_control.walk()
    elif "wag tail" in command:
        servo_control.wag_tail()
    elif "nod head" in command:
        servo_control.nod_head()
    else:
        print("Command not recognized.")
    led_control.blink_led()  # Provide visual feedback on action completion
