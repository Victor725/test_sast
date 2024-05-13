#Tarpits 16 in 《Testability Tarpits:...》
import os

def fun(*args):
    for i in args:
        os.system(i)

fun("ls", input("Input command:"))