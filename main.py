from moviepy.editor import *


class CustomClip:

    def __init__(self) -> None:
        """Set Filename"""
        self.clip = None

    def set_audio_file(self, file: str, t_start=0, t_end=None):
        """set audio file"""
        self.clip = AudioFileClip(filename=file).subclip(t_start=t_start, t_end=t_end)

    def set_video_file(self, file: str, t_start=0, t_end=None):
        """set video file"""
        self.clip = VideoFileClip(filename=file).subclip(t_start=t_start, t_end=t_end)

    def extract_audio(self, new_file: str):
        """extract audio"""
        self.clip = self.clip.audio
        self.write_audio_file(new_file=new_file)

    def write_audio_file(self, new_file: str):
        """write audio file"""
        self.clip.write_audiofile(new_file)

    def write_video_file(self, new_file: str):
        """write audio file"""
        self.clip.write_videofile(new_file)

    def set_audio(self, audio_file, new_file):
        """set audio to video"""
        self.clip = self.clip.set_audio(audio_file)
        self.write_video_file(new_file=new_file)


obj = CustomClip()
obj.set_video_file("On & On - NCS.mp4", 0, 20)
obj.write_video_file("new.mp4")
