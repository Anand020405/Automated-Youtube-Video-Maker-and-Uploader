import pyautogui
import time
import webbrowser

youtube_channel_link = "https://studio.youtube.com/channel/UCbmUcKbCXwPbDlWyon-xqUg"


def upload_to_youtube(link = youtube_channel_link):
    # Uploads the video to youtube
    time.sleep(1)
    webbrowser.open(link)
    time.sleep(10)
    # Coordinates of the Create Button X: 2388, Y: 219
    pyautogui.click(2388, 219)
    time.sleep(0.1)
    # Coordinates of the Upload Videos Button X: 2368, Y: 2873
    pyautogui.click(2329, 284)
    time.sleep(0.1)
    # Coordinates of the Select Files Button X: 1277, Y: 1064
    pyautogui.click(1280, 1050)
    time.sleep(1)
    pyautogui.typewrite("output_video.mp4")
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(7)
    with open("ideas.txt","r") as ideas_file:
        title = ideas_file.read()
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.typewrite(title)
    time.sleep(0.1)
    # Coordinates of the Description X: 1162, Y: 761
    pyautogui.click(1162, 761)
    time.sleep(0.1)
    with open("Scripts/script.txt","r") as script_file:
        description = script_file.read()
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.typewrite(description)
    time.sleep(1)
    pyautogui.click(1931, 1364)
    time.sleep(1)
    pyautogui.scroll(-1000)
    # Coordinates of the No click box X: 649 Y: 1127
    time.sleep(10)
    pyautogui.click(649, 1127)
    # Coordinates of the Next button X: 1923 Y: 1475
    time.sleep(10)
    pyautogui.click(1923, 1475)
    time.sleep(5)
    pyautogui.click(1923, 1475)
    time.sleep(10)
    pyautogui.click(1923, 1475)
    # Coordinates of the Public Click Box X: 713 Y: 879
    time.sleep(5)
    pyautogui.click(713, 879)
    time.sleep(1)
    pyautogui.click(1923, 1475)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')

    print("Video Uploaded to Youtube")

if __name__ == "__main__":
    upload_to_youtube()

    
    