from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask, url_for, render_template, request, redirect, flash, jsonify

Base = declarative_base()
engine = create_engine("sqlite:///urls.db")

class URLs(Base):
    __tablename__ = "urls"
    shortURL = Column(Integer, primary_key=True)
    longURL = Column(String(255), nullable=False)


def createDB():

    Base.metadata.create_all(engine)


DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

def buildShortenGet():
    html = """
    <html>
        <body>
            <form action="/shorten" method="POST">
                <input type="text" name="url" placeholder="long URL">
                <input type="submit">
            </form>
        <body>
    </html>
    """
    return html

def shortenThisURL(url):
    shorty = session.query(URLs).filter(URLs.longURL == url).first()
    if not shorty:
        shorty = URLs()
        shorty.longURL = url
        session.add(shorty)
        session.commit()
        #this is where i should use message flashing
        #since it's immediately going to the list
        #but that's out of scope of this exercise


@app.route("/shorten", methods=("POST", "GET"))

def shorten():
    if request.method == "GET":
        return buildShortenGet()
    elif request.method == "POST":
        shortenThisURL(request.form["url"])
        return redirect(url_for("lister"))

@app.route("/<int:shortID>/") #apparnetly the trailing slash matters?
def shortReceiver(shortID):
    shorty = session.query(URLs).filter(URLs.shortURL == shortID).first()
    if shorty:
        return redirect("http://" + shorty.longURL)
        #why is this redirecting to a local path??!
    else:
        return redirect(url_for("lister"))

@app.route("/", methods=("POST", "GET"))
@app.route("/list", methods=("POST", "GET"))
def lister():
    html = """
    <html>
        <body>
            Long URL : Short URL
            <ul>
            {0}
            </ul>
        </body>
    </html>
    """

    htmlTemplate = """
    <li>
        {0} : <a href="/{1}" target="_blank">shorty</a>
    </li>
    """
    items = ""
    query = session.query(URLs).all()
    for shorty in query:
        items += htmlTemplate.format(shorty.longURL, shorty.shortURL)
    return html.format(items)

if __name__ == '__main__':
    app.secret_key = "super secret key"
    app.debug = True
    app.run(host='localhost', port=5555)





