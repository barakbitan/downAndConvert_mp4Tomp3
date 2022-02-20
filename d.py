from moviepy.editor import *
import pytube
import os
v = pytube.YouTube('https://youtu.be/NI92xMGVFEU?list=PLqbbtzuH24vSp2HDs9AKqilCp5qXwp4VW').streams.first().download()

videoclip = VideoFileClip(v)
audioclip = videoclip.audio
audioclip.write_audiofile('mp3_file.mp3')
audioclip.close()
videoclip.close()

