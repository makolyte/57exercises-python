import os

namesStr = """Ling, Mai
Johnson, Jim
Zarnecki, Sabrina
Jones, Chris
Jones, Aaron
Swift, Geoffrey
Xiong, Fong
"""

names = []

for name in namesStr.splitlines():
    names.append(name)

names.sort()
namesStr = "";
for name in names:
    print(name)
    namesStr += name + "\r\n"

with open("D:\Temp\lesson41.txt", 'w') as f:
    f.writelines(namesStr)
