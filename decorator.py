import os
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        os.system(args[0])  # command exec!
        func(*args, **kwargs)
    return wrapper

@decorator
def print_command(command):
    print(command)


print_command(input())