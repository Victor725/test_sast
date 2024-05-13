#Tarpits 04 in 《Testability Tarpits:...》
import os

t = input("Input command:")
command = "ls" if "/" in t else t
os.system(command)

command = "ls" if 1>0 else t
os.system(command)