#Tarpits 22 in 《Testability Tarpits:...》
import os

class foo: 
    def __init__(self) -> None:
        self.command = ""

obj1=foo()
obj1.command="ls"
obj2=obj1
obj2.command = input()
os.system(obj2.command)