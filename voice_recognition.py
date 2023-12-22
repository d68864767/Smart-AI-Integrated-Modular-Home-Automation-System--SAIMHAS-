```python
import speech_recognition as sr
from communication import send_command_to_iot

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to listen for commands
def listen_for_commands():
    # Use microphone as source of input
    with sr.Microphone() as source:
        print("Listening for commands...")
        # Read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # Convert speech to text
        text = r.recognize_google(audio_data)
        return text

# Function to handle commands
def handle_commands(command):
    # Check for different commands and handle them
    # This is just a basic example, you would have more commands and more complex handling in a real system
    if "turn on the lights" in command:
        send_command_to_iot("lights", "on")
    elif "turn off the lights" in command:
        send_command_to_iot("lights", "off")
    # Add more commands as needed

# Main function
def main():
    while True:
        # Listen for commands
        command = listen_for_commands()

        # Handle commands
        handle_commands(command)

if __name__ == "__main__":
    main()
```
