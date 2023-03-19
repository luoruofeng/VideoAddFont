import sys
import os
import subprocess

ffmpeg = "/usr/local/bin/ffmpeg"

def getCommands(video_file, font):
    quotation = "\""
    return [
        ffmpeg,
        "-i",
        video_file,
        "-vf",
        "subtitles="+font+":force_style='Alignment=2,Fontsize=33,PrimaryColour=&H03fc0f&,BorderStyle=4,BackColour=&H80000000,OutlineColour=&H80000000,Outline=1,Shadow=0,MarginV=20'",
        "-c:a",
        "copy",
        "new_"+video_file,
    ]

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("you need 2 arguments:video name ,  zh font file, !!")
        quit()
    video_file = args[0]
    zh_font = args[1]

    

    if subprocess.run(getCommands(video_file,zh_font)).returncode == 0:
        os.remove(video_file)
        os.rename("new_"+video_file,video_file)
        print ("cn font Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script when font is cn")
        quit()

