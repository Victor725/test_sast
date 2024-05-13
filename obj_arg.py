#Tarpits 23 in 《Testability Tarpits:...》
import os

class foo: 
    def __init__(self) -> None:
        self.command = ""

def f(a,b):
    a.command=b

obj1=foo()
obj1.command="ls"
f(obj1,input())
os.system(obj1.command)