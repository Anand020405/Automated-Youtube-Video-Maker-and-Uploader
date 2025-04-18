import pyttsx3

SCRIPT_FILE = "Scripts/script.txt"
def text_to_speech(file_name=SCRIPT_FILE):
    # Create a Narration on the text created
    engine = pyttsx3.init()
    with open("ideas.txt", "r") as idea_file:
        topic = idea_file.read()
    with open(f"Scripts/script.txt","r") as file:
        contents = file.read()
    engine.save_to_file(f"{topic}...\n{contents}", 'Audio/audio.mp3')
    engine.runAndWait()
    print("Text to Speech Completed")

if __name__ == "__main__":
    text_to_speech()