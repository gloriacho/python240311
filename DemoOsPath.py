#DemoOSPath.py

import random

print(random.random())
print(random.random())

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print(random.sample( range(20),10))
print(random.sample( range(20),10))

print("----------------")
lotto = list(range(1,46))
print(lotto)
random.shuffle(lotto)
print(lotto)

from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))
if exists("c:\\python310\\python.exe"):
    print("O")
else:
    print("X")

print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))

from os import *
print("파일크기:{0}".format(name))


import glob
print("현재폴더{0}".format(getcwd()))
chdir("..")
chdir("c:\\work")
lst = glob.glob("*.py")
for item in lst:
    print(item)