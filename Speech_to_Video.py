from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
import random

def Speech_to_video():
    # Converts the speech into final video
    audio = AudioFileClip("Audio/audio.mp3")
    audio_length = min(audio.duration,40)
    #print(audio_length)
    random_numbers = [random.randint(1, 34) for _ in range(20)]
    final_video = VideoFileClip(f"Videos Library/{random_numbers[0]}.mp4",audio=False)
    video_length = final_video.duration 
    x = 1
    while video_length < audio_length:
        clip1 = VideoFileClip(f"Videos Library/{random_numbers[x]}.mp4",audio=False)
        final_video = concatenate_videoclips([final_video, clip1])
        video_length = final_video.duration
        x+=1
    #print(video_length)
    final_video = final_video.subclip(0,audio_length)
    final_clip = final_video.set_audio(audio)
    new_w = int(final_clip.h * 9 / 16)
    new_h = final_clip.h
    x_center = final_clip.w / 2
    y_center = final_clip.h / 2
    cropped_clip = final_clip.crop(x_center=x_center, y_center=y_center, width=new_w, height=new_h)

    cropped_clip.write_videofile("output_video.mp4")
    print("Speech to Video Completed")

if __name__ == "__main__":
    Speech_to_video()