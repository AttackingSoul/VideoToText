import whisper
import moviepy.editor as mp

from pytube import YouTube
from pathlib import Path

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        videoFilePath = youtubeObject.download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")
    return videoFilePath

def VideoToAudio(videoFilePath):
    clip = mp.VideoFileClip(videoFilePath)
    audioFilePath = Path(videoFilePath).with_suffix(".mp3")
    clip.audio.write_audiofile(audioFilePath)
    if (Path(audioFilePath).exists()):
        return audioFilePath.as_posix()
    else:
        return ""
    
def AudioToText(audioFilePath):
    model = whisper.load_model("small")
    result = model.transcribe(audio=audioFilePath, task = 'translate')
    print(result["text"])

def main():
    link = input("Enter the YouTube video URL: ")
    videoFilePath = Download(link)
    if (not Path(videoFilePath).exists()):
        return

    audioFilePath = VideoToAudio(videoFilePath)
    if (not Path(audioFilePath).exists()):
        return

    AudioToText(audioFilePath)

if __name__ == '__main__':
    main()