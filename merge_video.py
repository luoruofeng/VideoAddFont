import sys
import os
import subprocess

ffmpeg = "/usr/local/bin/ffmpeg"

def getCommands(video_file, font,out_video_file):
    quotation = "\""
    return [
        ffmpeg,
        "-i",
        video_file,
        "-vf",
        "subtitles="+font+":force_style='Alignment=2,Fontsize=33,PrimaryColour=&H03fc0f&,BorderStyle=4,BackColour=&H80000000,OutlineColour=&H80000000,Outline=1,Shadow=0,MarginV=20'",
        "-c:a",
        "copy",
        out_video_file,
    ]

def add_font(video_file,zh_font,out_video_file):
    if subprocess.run(getCommands(video_file,zh_font,out_video_file)).returncode == 0:
        print ("cn font Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script when font is cn")
        quit()

