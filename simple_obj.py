#Tarpits 21 in 《Testability Tarpits:...》
import os

class foo:
    def __init__(self, command) -> None:
        self.command = command
    def getCmd(self):
        return self.command
    
command = input()
obj = foo(command)
os.system(obj.getCmd())