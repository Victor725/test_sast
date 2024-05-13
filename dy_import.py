import importlib

Input = input('Please provide the path for the file to transcode: ')
#command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=Input)
command = Input

lib = importlib.import_module("os")
lib.system(command)  # command exec!