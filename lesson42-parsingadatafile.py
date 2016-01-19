data = """Ling,Mai,55900
Johnson,Jim,56500
Jones,Aaron,46000
Jones,Chris,34500
Swift,Geoffrey,14200
Xiong,Fong,65000
Zarnecki,Sabrina,51500
"""

class Data():
    def __init__(self):
        self.lastName = ""
        self.firstName = ""
        self.salary = ""

    def parse(self, line):
        fields = line.split(",");
        self.lastName = fields[0]
        self.firstName = fields[1]
        self.salary = fields[2]


Datas = []

maxLens = [0, 0, 0]
headers = ["Last", "First", "Salary"]

for line in data.splitlines():
    data = Data()
    data.parse(line)

    maxLens[0] = max(len(data.lastName), maxLens[0])
    maxLens[1] = max(len(data.firstName), maxLens[1])
    maxLens[2] = max(len(data.salary), maxLens[2])

    Datas.append(data)

for i in range(0, 3):
    maxLens[i] = max(maxLens[i], len(headers[i])) + 1


def output(str1, str2, str3, filler = ' '):
    print "{0}|{1}|{2}".format(str1.ljust(maxLens[0], filler),
                           str2.ljust(maxLens[1], filler),
                           str3.ljust(maxLens[2], filler))


output(headers[0], headers[1], headers[2])
output('-', '-', '-', filler='-')

for d in Datas:
    output(d.lastName, d.firstName, d.salary)



