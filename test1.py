import subprocess
import os

Input = input('Please provide the path for the file to transcode: ')
#command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=Input)
command = Input
os.system(command)  # command exec!
subprocess.getstatusoutput('ping -c 1 %s' % Input)