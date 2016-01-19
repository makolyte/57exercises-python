"""
to install feedparser just do "pip install feedparser".
see here: http://stackoverflow.com/a/8959399/1538717
"""
import feedparser

def getImages():
    feed = feedparser.parse("https://api.flickr.com/services/feeds/photos_public.gne?tags=dogs")
    images = []
    for entry in feed["entries"]:
        for link in entry["links"]:
            if (link["type"] == "image/jpeg"):
                images.append(link["href"])
    return images


def createHtmlFile():
    html = """
    <html>
        <body>
            {0}
        </body>
    </html>
    """

    imgTemplate = "<img src='{0}' alt='missing'>"

    imgHtml = ""

    images = getImages()

    for image in images:
        imgHtml += imgTemplate.format(image)

    html = html.format(imgHtml)


    with open("hello/flickr.html", 'a+') as f:
        f.write(html)


createHtmlFile()