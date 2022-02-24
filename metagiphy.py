from moviepy.editor import *
clip = VideoFileClip("sample.mp4")
clip=clip.subclip(0,3)
clip.write_gif("mygif.gif")
