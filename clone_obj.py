#Tarpits 25 in 《Testability Tarpits:...》
import os
import copy

class foo: 
    def __init__(self) -> None:
        self.command = ""

obj1=foo()
obj1.command=input()
obj2 = copy.deepcopy(obj1)
os.system(obj2.command)