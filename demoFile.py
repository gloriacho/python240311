#demoFile.py

f = open("Demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("Demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.close()
