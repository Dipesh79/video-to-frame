from moviepy.editor import *

# video_name = input("Enter Video Name: ")

clip = VideoFileClip("demo.mp4")

duration = clip.duration
print(duration)
i=0
j=0
while(i<duration):
    clip.save_frame(f'demo{j}.png', t=i)
    i+=0.1
    j+=1

