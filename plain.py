import subprocess
import os

def transcode_file():
    Input = input('Please provide the path for the file to transcode: ')
    command = 'ffmpeg -i output_file.mpg'
    #command = Input
    os.system(command)  # command exec!


transcode_file()