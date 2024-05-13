import subprocess
import os

def unsanitize_plus(command):
    return command[0:2]


def transcode_file():
    Input = input('Please provide the path for the file to transcode: ')
    command = 'ls "{source}" '.format(source=Input)
    #command = Input
    command = unsanitize_plus(command)
    os.system(command)  # command exec!
    ping(Input)


def ping(target):
    return subprocess.getstatusoutput('ping -c 1 %s' % target)


transcode_file()