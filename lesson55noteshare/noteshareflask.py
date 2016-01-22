from flask import Flask, render_template, request, redirect, url_for
from database_setup import GetSession, Note, CreateDB

app = Flask(__name__)

session = GetSession()

def newNote():
    return render_template("noteshare.html")

def getNote(noteid):
    note = session.query(Note).filter(Note.id==noteid).first()
    return note

@app.route("/edit/", methods=("GET", "POST"))
@app.route("/edit/<int:noteid>/", methods=("GET", "POST"))
def noteshare(noteid=None):
    if request.method == "GET":
        if not noteid:
            return newNote()
        else:
            note = getNote(noteid)
            if note:
                return render_template("noteshare.html", note=note)
            else:
                return newNote()

    else:
        note = None
        if noteid:
            note = getNote(noteid)
        else:
            note = Note()
        note.noteText = request.form["noteText"]
        session.add(note)
        session.commit()
        return redirect(url_for("homePage"))

@app.route("/")
def homePage():
    html = """
    <html>
        <body>
            <a href='/edit'>Add new note</a>
            <ul>
                {0}
            </ul>
        </body>
    </html>
    """

    liTemplate = "<li>{0}</li>" #TODO add link to viewing the note here
    list = ""
    for note in session.query(Note).all():
        list += liTemplate.format(note.noteText[:15])

    return html.format(list)


if __name__ == '__main__':
    CreateDB()
    app.secret_key = "super secret key"
    app.debug = True
    app.run(host='localhost', port=5555)
