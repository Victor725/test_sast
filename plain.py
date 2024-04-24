import subprocess
import os

def transcode_file():
    Input = input('Please provide the path for the file to transcode: ')
    command = 'ffmpeg -i output_file.mpg'
    #command = Input
    os.system(command)  # command exec!
    ping(command)


def ping(target):
    return subprocess.getstatusoutput('ping -c 1 %s' % target)


transcode_file()