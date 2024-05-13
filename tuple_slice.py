import os


def transcode_file():
    Input = input('Please provide the path for the file to transcode: ')
    input_tp = (Input, "ls")
    command = input_tp[0]
    #command = Input
    os.system(command)  # command exec!
    command = input_tp[1]
    os.system(command)

transcode_file()