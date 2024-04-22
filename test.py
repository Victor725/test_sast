import subprocess

def transcode_file():
    filename = input('Please provide the path for the file to transcode: ')
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!