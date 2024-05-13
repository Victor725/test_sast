#Tarpits 10 in 《Testability Tarpits:...》
import os

class foo:
    def __init__(self) -> None:
        self.k = ["ls"]
    def getk(self):
        return self.k

t = input("Input command:")
obj = foo()

command = obj.getk()
obj.k += [t]

print(command)
os.system(";".join(command))