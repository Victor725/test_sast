import os


def transcode_file():
    Input = input('Please provide the path for the file to transcode: ')
    input_list = [Input, "ls"]
    command = input_list[0]
    #command = Input
    os.system(command)  # command exec!
    command = input_list[1]
    os.system(command)

transcode_file()