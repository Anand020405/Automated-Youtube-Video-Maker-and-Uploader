from Idea_Maker import Ideas
from Script_Maker import Script_Maker
from Text_To_Speech import text_to_speech
from Speech_to_Video import Speech_to_video
from youtube_uploader import upload_to_youtube
import time


Max_Videos = 10
Video_Count = 1

while Video_Count <= Max_Videos:
    print(f"Video {Video_Count} started")
    Ideas()
    Script_Maker()
    text_to_speech()
    Speech_to_video()
    upload_to_youtube()
    Video_Count += 1
