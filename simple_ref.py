#Tarpits 8 in 《Testability Tarpits:...》
import os


t=["ls"]
command = t
t += [input("Input command:")]

os.system(";".join(command))