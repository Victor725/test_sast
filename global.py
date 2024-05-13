#Tarpits 01 in 《Testability Tarpits:...》
import os

b = "id"
def F(a):
    global b
    os.system(b)
    b = a

t = input("Input command:")
s = "ls"
F(t)
F(s)