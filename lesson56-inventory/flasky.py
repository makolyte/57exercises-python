from flask import Flask, render_template, request, redirect, url_for
#import data classes and other classes

app = Flask(__name__)


class Item():
    SEPARATOR = unichr(28)
    DATA_FILE = "data/data.csv"
    def __init__(self):
        self.name = ""
        self.value = 0
        self.serial = ""
    def Save(self):
        with open(Item.DATA_FILE, "a+") as csv:
            csv.write(self.ToString())

    @staticmethod
    def GetItems():
        items = []
        with open(Item.DATA_FILE, 'r') as csv:
            for line in csv.readlines():
                lineArr = line.split(Item.SEPARATOR)
                item = Item()
                item.name = lineArr[0]
                item.serial = lineArr[1]
                item.value = lineArr[2]
                items.append(item)
        return items


    def ToString(self):
        return "{1}{0}{2}{0}{3}\n".format(Item.SEPARATOR, self.name, self.serial, self.value)

@app.route("/newitem/", methods=("GET", "POST"))
def newitem():
    page = "newitem.html"
    if request.method == "GET":
        return render_template(page)
    else:
        item = Item()
        item.name = request.form["itemname"]
        item.value = request.form["itemvalue"]
        item.serial = request.form["itemserial"]
        item.Save()
        return redirect(url_for("itemlist"))

@app.route("/")
@app.route("/itemlist/")
def itemlist():
    items = Item.GetItems()
    return render_template("itemlist.html", items=items)

if __name__ == '__main__':
    #CreateDB()
    app.secret_key = "super secret key"
    app.debug = True
    app.run(host='localhost', port=5555)