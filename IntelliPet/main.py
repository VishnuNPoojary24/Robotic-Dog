#Voice Command Integration
import speech_recognition as sr
import servo_control

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

def handle_command(command):
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

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if command:
            handle_command(command)
